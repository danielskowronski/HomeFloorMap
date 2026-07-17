import os
import requests
from flask import Flask, jsonify, send_from_directory, abort
from pathlib import Path
from config import AppConfig, load_config

CONF_PATH = os.environ.get("HFM_CONF_PATH", "../example_config/")

cfg = load_config(CONF_PATH + '/hfm.yaml')
app = Flask(__name__, static_folder="static", static_url_path="")


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/floorplan.svg")
def floorplan():
    return send_from_directory(CONF_PATH, "floorplan.svg")


@app.route("/sensorsMapping.json")
def sensorDefs():
    return send_from_directory(CONF_PATH, "sensorsMapping.json")


@app.route("/sensorsAppearance.json")
def config():
    return send_from_directory(CONF_PATH, "sensorsAppearance.json")

@app.route("/settings.json")
def settings():
    return send_from_directory(CONF_PATH, "settings.json")


def prom_results_parse(prom_results):
  results={}
  #results["last_updated"]="TBD"
  for sensor, entity in cfg.sensorMap.sensor.items():
    results[sensor]=-9999
    for r in prom_results:
      if r["metric"].get("domain", "") == "sensor" and r["metric"].get("entity", "") == f"sensor.{entity}" and len(r["value"])==2:
        results[sensor]=float(r["value"][1])
  for sensor, entity in cfg.sensorMap.cover.items():
    results[sensor]=0
    for r in prom_results:
      if r["metric"].get("domain", "") == "cover" and r["metric"].get("entity", "") == f"cover.{entity}" and len(r["value"])==2:
        results[sensor]=int(r["value"][1])
  for sensor, entity in cfg.sensorMap.binary_sensor.items():
    results[sensor]=False
    for r in prom_results:
      if r["metric"].get("domain", "") == "binary_sensor" and r["metric"].get("entity", "") == f"binary_sensor.{entity}" and len(r["value"])==2:
        results[sensor]=r["value"][1]=="1"
  for sensor, entity in cfg.sensorMap.climate.items():
    results[sensor]={"off": False, "heat": False, "target": -9999, "current": -9999}
    #results[f"{sensor}_off"]=False
    #results[f"{sensor}_heat"]=False
    #results[f"{sensor}_target"]=-9999
    #results[f"{sensor}_current"]=-9999
    for r in prom_results:
      if r["metric"].get("domain", "") == "climate" and r["metric"].get("entity", "") == f"climate.{entity}" and len(r["value"])==2:
          if r["metric"].get("__name__","")=="homeassistant_climate_mode" and r["metric"].get("mode","")=="off":
            #results[f"{sensor}_off"]=r["value"][1]=="1"
            results[sensor]["off"]=r["value"][1]=="1"
          elif r["metric"].get("__name__","")=="homeassistant_climate_mode" and r["metric"].get("mode","")=="heat":
            #results[f"{sensor}_heat"]=r["value"][1]=="1"
            results[sensor]["heat"]=r["value"][1]=="1"
          elif r["metric"].get("__name__","")=="homeassistant_climate_target_temperature_celsius":
            #results[f"{sensor}_target"]=float(r["value"][1])
            results[sensor]["target"]=float(r["value"][1])
          elif r["metric"].get("__name__","")=="homeassistant_climate_current_temperature_celsius":
            #results[f"{sensor}_current"]=float(r["value"][1])
            results[sensor]["current"]=float(r["value"][1])
  for window, sensors in cfg.sensorMerge.window.items():
    sum=0
    for sensor in sensors:
      if results.get(sensor, False):
        sum=sum+1
    results[window]=sum
  for rain_id, sensors in cfg.sensorMerge.rain.items():
    results[rain_id]={
      "day": results.get(sensors.day),
      "hour": results.get(sensors.hour),
      "min15": results.get(sensors.min15)
    }
  return results

@app.route("/sensorsValues.json")
def proxy_sensors_prom():
    try:
      resp = requests.get(
          f"{cfg.prom.url}/api/v1/query",
          params={"query": cfg.prom.query }
      )
      results = resp.json()["data"]["result"]
      results_parsed = prom_results_parse(results)
      return jsonify(results_parsed)
    except Exception as e:
      raise e
      return abort(
            502, description=f"Failed to fetch sensor data from Prometheus: {e}."
        )


@app.route("/sensorsValuesDirect.json")
def proxy_sensors():
    payload = {
        "template": Path(CONF_PATH + "/sensorsRequest.j2").read_text(),
        "variables": {},
    }
    headers = {
        "Authorization": f"Bearer {cfg.ha.token}",
        "Content-Type": "application/json",
    }
    try:
        resp = requests.post(
            f"{cfg.ha.url}/api/template", json=payload, headers=headers, timeout=10
        )
        resp.raise_for_status()
    except requests.RequestException as e:
        print("Error proxying to Home Assistant:", e)
        return abort(
            502, description="Failed to fetch sensor data from Home Assistant."
        )

    try:
        result = resp.json()
    except ValueError:
        print("Invalid JSON from HA /api/template:", resp.text)
        return abort(502, description="Invalid JSON from Home Assistant.")

    return jsonify(result)


if __name__ == "__main__":
    app.run(host=cfg.server.host, port=cfg.server.port, debug=cfg.server.debug)

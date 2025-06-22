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


@app.route("/sensorsValues.json")
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

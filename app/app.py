import os
import requests
from flask import Flask, jsonify, send_from_directory, abort
from pathlib import Path

conf_path = "../example_config/"
conf_path = "../../HomeFloorMapDATA/"

app = Flask(__name__, static_folder="static", static_url_path="")

ha_template = Path(conf_path + "/sensorRequest.j2").read_text()

HA_BASE = os.environ.get("HFM_HA_URL")
HA_TOKEN = os.environ.get("HFM_HA_TOKEN")


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/floorplan.svg")
def floorplan():
    return send_from_directory(conf_path, "floorplan.svg")


@app.route("/sensorDefs.json")
def sensorDefs():
    return send_from_directory(conf_path, "sensorDefs.json")


@app.route("/sensorValues.json")
def proxy_sensors():
    payload = {"template": Path(conf_path + "/sensorRequest.j2").read_text(), "variables": {}}
    headers = {
        "Authorization": f"Bearer {HA_TOKEN}",
        "Content-Type": "application/json",
    }
    try:
        resp = requests.post(
            f"{HA_BASE}/api/template", json=payload, headers=headers, timeout=10
        )
        resp.raise_for_status()
    except requests.RequestException as e:
        breakpoint()
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
    app.run(host="0.0.0.0", port=9002, debug=True)

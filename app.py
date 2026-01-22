from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

# Plan A: Using Open-Notify for the ISS (Reliable for demos)
SATELLITE_API = "http://api.open-notify.org/iss-now.json"

@app.get("/")
def mission_control():
    try:
        # Fetching real-time telemetry from a third-party REST API
        response = requests.get(SATELLITE_API, timeout=5)
        data = response.json()
        
        lat = data['iss_position']['latitude']
        lon = data['iss_position']['longitude']
        timestamp = data['timestamp']

        return jsonify({
            "mission": "AggieSat-IBM Edge Simulation",
            "satellite": "ISS (Zarya)",
            "telemetry": {
                "latitude": lat,
                "longitude": lon,
                "timestamp": timestamp,
                "status": "NOMINAL"
            },
            "infrastructure": "IBM Code Engine / Containerized"
        })
    except Exception as e:
        return jsonify({"error": "Telemetry downlink lost", "details": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

from flask import Flask, render_template, jsonify
import requests
import os

app = Flask(__name__)

# External Satellite API (Open-Notify ISS Tracker)
SATELLITE_API = "http://api.open-notify.org/iss-now.json"

@app.route("/")
def index():
    # Serves the React frontend
    return render_template("index.html")

@app.route("/api/telemetry")
def get_telemetry():
    try:
        # Fetching real-time coordinates from space
        response = requests.get(SATELLITE_API, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        return jsonify({
            "mission": "AggieSat-IBM Edge Simulation",
            "satellite": "ISS (Zarya)",
            "latitude": data['iss_position']['latitude'],
            "longitude": data['iss_position']['longitude'],
            "timestamp": data['timestamp'],
            "status": "NOMINAL"
        })
    except Exception as e:
        return jsonify({"status": "OFFLINE", "error": str(e)}), 500

if __name__ == "__main__":
    # IBM Code Engine provides the PORT environment variable
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

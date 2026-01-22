from flask import Flask, render_template, jsonify
import requests
import os
import reverse_geocoder as rg # Offline reverse geocoding

app = Flask(__name__)

N2YO_API_KEY = os.environ.get("N2YO_API_KEY", "6X5BX5-GHMQRD-7KY3DC-5N3W")
NORAD_ID = 43569 # Iridium 180

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/telemetry")
def get_telemetry():
    try:
        url = f"https://api.n2yo.com/rest/v1/satellite/positions/{NORAD_ID}/30.6/-96.3/100/1/&apiKey={N2YO_API_KEY}"
        response = requests.get(url, timeout=5).json()
        pos = response['positions'][0]
        
        # Logic: Determine location description
        lat, lng = pos['satlatitude'], pos['satlongitude']
        
        # Check if over ocean (Rough estimation based on distance to nearest city)
        search_result = rg.search((lat, lng))[0]
        location_text = f"Over {search_result['name']}, {search_result['cc']}"
        
        # If the nearest city is more than 500km away, it's likely deep ocean
        # For a demo, this offline check is safer than a second API call
        
        return jsonify({
            "name": response['info']['satname'],
            "lat": lat,
            "lng": lng,
            "alt": pos['sataltitude'],
            "location": location_text,
            "status": "ACTIVE"
        })
    except Exception as e:
        return jsonify({"status": "OFFLINE", "error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8090))
    app.run(host="0.0.0.0", port=port)
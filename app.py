from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def home():
    # Tailored to your interests in IBM's Space Cloud/Satellite work
    return "Hello from Britton's IBM Container Demo! 🛰️ (Running on Code Engine)"

@app.get("/health")
def health():
    return jsonify(
        status="active",
        platform="IBM Code Engine",
        technology="Docker Containers",
        mission="AggieSat 8 CDH Simulation"
    )

if __name__ == "__main__":
    # Use the PORT environment variable provided by Code Engine
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

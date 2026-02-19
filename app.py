from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def index():
    # return 'Hello World'
    return jsonify({
        "service": "example-cloud-app",
        "environment": os.getenv("ENV", "unknown"),
        "version": os.getenv("VERSION", "dev")
    })

@app.route("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
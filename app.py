from flask import Flask, jsonify, request
import os

app = Flask(__name__)

APP_NAME = "student-ml-api"
APP_VERSION = "1.0.0"          # bump this per release
MODEL_VERSION = "model-1"

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "application": APP_NAME,
        "version": APP_VERSION
    }), 200

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)

    if data is None or "value" not in data:
        return jsonify({"error": "Missing 'value' field"}), 400

    value = data["value"]
    if not isinstance(value, (int, float)):
        return jsonify({"error": "'value' must be a number"}), 400

    prediction = value * 2   # simple placeholder "model"

    return jsonify({
        "input": value,
        "prediction": prediction
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
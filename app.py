from flask import Flask, request, jsonify
from flask_cors import CORS
from preprocessing.cleaning_data import preprocess
from predict.prediction import predict
from vendors.utils import PREDICT_QUERY_JSON
import os

app = Flask(__name__)
CORS(app)


@app.get("/")
def index():
    return "alive?", 200


@app.get("/predict")
def predict_page():
    return jsonify(PREDICT_QUERY_JSON)


@app.post("/predict")
def predict_endpoint():
    # deal with empty POST request and invalid JSON
    if not request.content_type or not request.content_type.startswith(
        "application/json"
    ):
        return (
            jsonify(message="🚫 Invalid content-type. Must be application/json."),
            400,
        )

    data = request.get_json().get("data")
    if data is None:
        return jsonify(message="🚫 Missing data object"), 400

    processed_data = preprocess(data)
    if processed_data["error"] is not None:
        return jsonify(processed_data), 400

    return jsonify(predict(processed_data))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

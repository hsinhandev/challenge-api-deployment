from flask import Flask, request, jsonify
from flask_cors import CORS
from preprocessing.cleaning_data import preprocess
from predict.prediction import predict
from vendors.utils import PREDICTQUERY_EXAMPLE
import os

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def index():
    return "alive?", 200


@app.route("/predict", methods=["GET", "POST"])
def predict_page():
    if request.method == "POST":
        # deal with empty POST request and invalid JSON
        if not request.content_type or not request.content_type.startswith(
            "application/json"
        ):
            return (
                jsonify(message="🚫 Invalid content-type. Must be application/json."),
                400,
            )

        data = request.get_json().get("data")

        if not data:
            return jsonify(message="🚫 Missing data object"), 400

        processed_data = preprocess(data)
        if processed_data["error"] is not None:
            return jsonify(processed_data), 400

        return jsonify(predict(processed_data))

    elif request.method == "GET":
        return f"<p>Post format as follow:</p><pre>{PREDICTQUERY_EXAMPLE}</pre>"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port)

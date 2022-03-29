from flask import Flask, request, jsonify
from preprocessing.cleaning_data import preprocess
from predict.prediction import predict
from vendors.utils import API_HINT

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "Alive", 200


@app.route("/predict", methods=["GET", "POST"])
def predict_page():
    if request.method == "POST":
        data = request.get_json().get("data")

        if not data:
            return jsonify(message="Message goes here"), 401

        processed_data = preprocess(data)
        response = predict(processed_data)

        if response["error"] is not None:
            return jsonify(response), 401

        return jsonify(response)

    elif request.method == "GET":
        return f"<p>Post format as follow:</p><pre>{API_HINT}</pre>"


@app.errorhandler(401)
def bad_request():
    """Bad request."""
    return "Go away!", 401


if __name__ == "__main__":
    app.run()

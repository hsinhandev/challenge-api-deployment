from flask import Flask, request, jsonify
from preprocessing.cleaning_data import preprocess
from predict.prediction import predict


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "Alive", 200


@app.route("/predict", methods=["GET", "Post"])
def predict_page():
    if request.method == "POST":
        data = request.get_json().get("data")

        if not data:
            return jsonify(message="Message goes here"), 401
        processed_data = preprocess(data)

        response = predict(processed_data)
        print(f"predict price {response =}")
        return "response", 200
    elif request.method == "GET":
        message = """
        {
            "data": {
                "area": int,
                "property-type": "APARTMENT" | "HOUSE" | "OTHERS",
                "rooms-number": int,
                "zip-code": int,
                "land-area": Optional[int],
                "garden": Optional[bool],
                "garden-area": Optional[int],
                "equipped-kitchen": Optional[bool],
                "full-address": Optional[str],
                "swimming-pool": Optional[bool],
                "furnished": Optional[bool],
                "open-fire": Optional[bool],
                "terrace": Optional[bool],
                "terrace-area": Optional[int],
                "facades-number": Optional[int],
                "building-state": Optional[
                    "NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"
                ],
            }
        }
        """
        return f"<p>Post format as follow:</p><pre>{message}</pre>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

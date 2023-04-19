#en222yu

from flask import Flask, jsonify, request
from flask_cors import CORS
from model import Character
from performance import PerformanceMiddleware
from database import (
    fetch_one_character,
    fetch_all_characters,
    #create_character,
    #update_character,
    #remove_character,
)

app = Flask(__name__)
CORS(app)

# Add performance middleware
app.wsgi_app = PerformanceMiddleware(app.wsgi_app)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/characters/")
def get_characters():
    response = fetch_all_characters()
    character_dicts = [c.dict() for c in response]  # convert each Character object to a dictionary
    return jsonify(character_dicts)

@app.route("/character/<int:id>", methods=["GET"])
def get_character_by_id(id):
    response = fetch_one_character(id)
    if response:
        return jsonify(response.dict())
    return jsonify({"error": f"There is no character with the id {id}"}), 404

# @app.route("/character/", methods=["POST"])
# def post_character():
#     character = Character(**request.json)
#     response = create_character(character.dict())
#     if response:
#         return jsonify(response)
#     return jsonify({"error": "Something went wrong"}), 400

# @app.route("/character/<int:id>", methods=["PUT"])
# def put_character(id):
#     status = request.json.get("status")
#     image = request.json.get("image")
#     url = request.json.get("url")
#     response = update_character(id, status, image, url)
#     if response:
#         return jsonify(response)
#     return jsonify({"error": f"There is no character with the id {id}"}), 404

# @app.route("/character/<int:id>", methods=["DELETE"])
# def delete_character(id):
#     response = remove_character(id)
#     if response:
#         return jsonify({"message": "Successfully deleted character"})
#     return jsonify({"error": f"There is no character with the id {id}"}), 404

if __name__ == "__main__":
    app.run(debug=True)

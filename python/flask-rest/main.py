#en222yu

from flask import Flask, jsonify, request
from flask_cors import CORS
from model import Character
from performance import PerformanceMiddleware
from database import (
    fetch_one_character,
    fetch_all_characters
)

app = Flask(__name__)
CORS(app)

# Add performance middleware
app.wsgi_app = PerformanceMiddleware(app.wsgi_app)

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

if __name__ == "__main__":
    app.run(debug=True)

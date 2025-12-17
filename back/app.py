from flask import Flask, make_response, jsonify, request
from dotenv import find_dotenv, load_dotenv
from os import environ, path, getenv

app = Flask(__name__)

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


def require_token(func):            #decorator to make the authentication
    def wrapper(*args, **kwargs):
        auth = request.headers["Authorization"]

        if not auth or not auth.startswith("Bearer "):
            message = {"error": "missing token"}
            return jsonify(message), 401

        token = auth.split(" ")[1]

        if token != getenv("TOKEN"):
            message = {"error": "invalid token"}
            return message, 401

        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper


@app.route("/", methods=["GET"])        #index route with nothing relevant
def index():
    social_media = {"instagram": "felipe.040", "tiktok": "felipica2"}
    return make_response(jsonify(social_media))



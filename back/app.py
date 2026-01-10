from flask import Flask, make_response, jsonify, request
from dotenv import find_dotenv, load_dotenv
from os import environ, path, getenv

app = Flask(__name__)

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


def require_token(func):            #decorator to make the authentication
    def wrapper(*args, **kwargs):
        try:
            auth = request.headers["Authorization"]

        except Exception as e:
            if str(e) == r"'HTTP_AUTHORIZATION'":
                message: dict = {"error": "i think you didnt put the authorization field within the headers"}
                return jsonify(message), 400
            else:
                print("else")
                message: dict = {"error": "something is wrong with the headers you sent"}
                jsonify(message), 400

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
    social_media = {"instagram": "felipe.040", "github": "felipe060"}
    return make_response(jsonify(social_media))


@app.route("/verify_user", methods=["POST"])
@require_token
def verify_user():
    """Route that verifies if the user and password are correct"""

    print("\napp.py verify_user() being called\n")

    content_type = str(request.headers["Content-Type"]).lower()

    from sidetasks import verify_header
    verify_content_type = verify_header(content_type=content_type)

    if verify_content_type != True:
        return jsonify(verify_content_type), 400

    else:
        json_received = request.json        #put the json received on a variable

        from sidetasks import verifies_user                     #importa a funcao la do sidetasks.py
        result_user = verifies_user(json_data=json_received)    #attaches the result of this function to a variable
        return jsonify(result_user)                             #tarde te amei, beleza tao antiga e tao nova


@app.route("/add_user", methods=["POST"])
@require_token
def add_user():
    print("\napp.py add_user() being called\n")

    content_type = str(request.headers["Content-Type"]).lower()

    from sidetasks import verify_header
    verify_content_type = verify_header(content_type=content_type)

    if verify_content_type != True:
        return jsonify(verify_content_type), 400

    else:
        json_received = request.json

        from sidetasks import adds_user
        result_user = adds_user(json_data=json_received)
        return jsonify(result_user)


@app.route("/send_code_reset_password")
@require_token
def send_code_reset_password():
    print("app.py send_code_reset_password() being called\n")
    return "send_email route"


@app.route("/reset_password_verify_email", methods=["POST"])
@require_token
def reset_password_verify_email():
    print("\napp.py alter_password() being called\n")

    content_type = str(request.headers["Content-Type"]).lower()

    from sidetasks import verify_header
    verify_content_type = verify_header(content_type=content_type)

    if verify_content_type != True:
        return jsonify(verify_content_type), 400

    else:
        json_received = request.json
        print("app.py alter_password() json_received -->", json_received)
        print("app.py alter_password() json_received type -->", type(json_received))

        from sidetasks import resets_password_verify_email
        result_alter_password = resets_password_verify_email(json_data=json_received)
        print("app.py alter_password() result_alter_password -->", result_alter_password)
        print("app.py alter_password() result_alter_password type -->", type(result_alter_password))
        return jsonify(result_alter_password)


@app.route("/emaail", methods=["POST"])
def emaail():
    json_received = request.json
    from sidetasks import sends_email
    enviar = sends_email(email=json_received["email"], code=json_received["code"])
    return jsonify(enviar)


app.run(host="0.0.0.0", debug=False)

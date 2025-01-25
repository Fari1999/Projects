from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Max Mustermann",
        "email": "Max.Mustermann@mail.de"
    }


    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

@app.route("/create-user", methods = ["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug=True)

#http://127.0.0.1:5000/get-user/123?extra=%22hello%22 gibt dir sowas: Running on http://127.0.0.1:5000 und dann /get-user/123?extra=%22hello%22 z.B. dran hängen

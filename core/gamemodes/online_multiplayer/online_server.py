from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

log = logging.getLogger("werkzeug")

status = {
    "state": "lobby",
    "players": {}
}


@app.route("/data")
def data():
    return jsonify(status)


@app.route("/join", methods=["POST"])
def join():
    data = request.get_json()

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in status["players"]:
        return jsonify({"error": "Username already exists"}), 409

    status["players"][username] = {
        "score": 0,
        "slogan": "",
        "done": False,
        "active": True
    }

    return jsonify({
        "message": "Joined successfully",
        "username": username
    }), 201


def set_no_server_logging(state):
    if state:
        log.setLevel(logging.ERROR)
    else:
        log.setLevel(logging.DEBUG)


def start_server(port):
    app.run(
        host="127.0.0.1",
        port=port,
        debug=False,
        use_reloader=False
    )


if __name__ == "__main__":
    start_server(5000)
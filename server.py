from flask import Flask, jsonify

app = Flask(__name__)

status = {
    "spelare": 0
}

@app.route("/data")
def data():
    return jsonify(status)


def start_server():
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)


if __name__ == "__main__":
    start_server()
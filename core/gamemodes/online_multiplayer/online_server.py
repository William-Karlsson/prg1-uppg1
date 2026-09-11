from flask import Flask, jsonify, request
import logging
import datetime
import time
import random

app = Flask(__name__)

log = logging.getLogger("werkzeug")

status = {
    "state": "lobby",
    "total_pot": 0,
    "players": {},
    "winner": ""
}

@app.route("/data")
def data():
    remove_inactive_players()
    check_round_finished()
    return jsonify(status)

# Används för att se till att spelare fortfarande är kopplade till servern
@app.route("/update_time", methods=["POST"])
def update_time():
    data = request.get_json()

    username = data.get("username")
    time = data.get("time")

    if username is None:
        return jsonify({"error": "Username is required"}), 400

    if time is None:
        return jsonify({"error": "Time is required"}), 400
    
    status["players"][username]["recorded_time"] = time

    return jsonify({
        "message": "Updated time successfully",
        "username": username
    }), 201

@app.route("/add_bet", methods=["POST"])
def add_bet():
    data = request.get_json()

    username = data.get("username")
    amount = data.get("amount")

    if username is None:
        return jsonify({"error": "Username is required"}), 400

    if amount is None:
        return jsonify({"error": "Amount is required"}), 400
    
    status["players"][username]["bet"] += amount
    status["total_pot"] += amount

    return jsonify({
        "message": "Updated total bet successfully",
        "username": username
    }), 201

@app.route("/submit_score", methods=["POST"])
def submit_score():
    data = request.get_json()

    username = data.get("username")
    score = data.get("score")

    if username is None:
        return jsonify({"error": "Username is required"}), 400

    if score is None:
        return jsonify({"error": "Score is required"}), 400
    
    status["players"][username]["score"] = score
    status["players"][username]["done"] = True

    return jsonify({
        "message": "Updated score successfully",
        "username": username
    }), 201

@app.route("/join", methods=["POST"])
def join():
    data = request.get_json()

    username = data.get("username")
    slogan = data.get("slogan")

    if username is None:
        return jsonify({"error": "Username is required"}), 400

    if username in status["players"]:
        return jsonify({"error": "Username already exists"}), 409
    
    if slogan is None:
        return jsonify({"error": "Slogan is required"}), 400

    status["players"][username] = {
        "score": 0,
        "bet": 0,
        "slogan": slogan,
        "done": False,
        "recorded_time": 0
    }

    return jsonify({
        "message": "Joined successfully",
        "username": username
    }), 201

@app.route("/start_game", methods=["POST"])
def start_game():
    status["state"] = "in_game"

    return jsonify({
        "message": "Started successfully"
    }), 201

@app.route("/stop_game", methods=["POST"])
def stop_game():
    status["total_pot"] = 0
    status["winner"] = ""
    status["players"] = {}
    status["state"] = "lobby"

    return jsonify({
        "message": "Ended successfully"
    }), 201

def set_no_server_logging(state):
    if state:
        log.setLevel(logging.ERROR)
    else:
        log.setLevel(logging.DEBUG)

def remove_inactive_players():
    current_time = int(datetime.datetime.utcnow().timestamp())

    try:
        for username in list(status["players"]):
            recorded_time = status["players"][username]["recorded_time"]

            if current_time - recorded_time > 30 and recorded_time > 0:
                del status["players"][username]
    except Exception as e:
        print(e)

def check_round_finished():
    try:
        finished_amount = 0

        for username in list(status["players"]):
            done = status["players"][username]["done"]

            if done:
                finished_amount += 1

        if finished_amount > 0 and finished_amount == len(list(status["players"])):
            closest_distance = min(
                abs(player["score"] - 21)
                for player in status["players"].values()
            )

            closest_players = [
                username
                for username, player in status["players"].items()
                if abs(player["score"] - 21) == closest_distance
            ]

            winner = random.choice(closest_players)

            status["state"] = "finished"
            status["winner"] = winner


    except Exception as e:
        print(e)
    
def start_server(port):
    app.run(
        host="0.0.0.0",
        port=port,
        debug=False,
        use_reloader=False
    )
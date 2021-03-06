from flask import Flask, request
from flask import jsonify
import random, json

app = Flask(__name__)

candidates = {
    "Linda": {
        "head": "7",
        "body": "9"
        },
    "CarlFan51": {
        "head": "9",
        "body": "14"
        },
    "BatgirlZoe": {
        "head": "4",
        "body": "15"
        },
    "JohnGabby": {
        "head": "2",
        "body": "12"
        }
    }

candidates_base = {
    "Linda": {
        "head": "7",
        "body": "9"
        },
    "CarlFan51": {
        "head": "9",
        "body": "14"
        },
    "BatgirlZoe": {
        "head": "4",
        "body": "15"
        },
    "JohnGabby": {
        "head": "2",
        "body": "12"
        }
    }

answers = {
        "gaming": {
            "JohnGabby": [1,3,1,0,1,2,1,2,1,2],
            "CarlFan51": [1,3,1,0,2,3,1,2,1,2],
            "BatgirlZoe": [1,3,1,0,2,3,1,1,2,3],
            "Linda": [3,2,1,2,1,2,1,2,1,2]
        },
        "godot": {
            "JohnGabby": [2,1,0,2,0,1,2,3,0,2],
            "CarlFan51": [2,1,0,2,3,1,2,2,0,2],
            "BatgirlZoe": [2,1,0,2,0,1,2,2,0,3],
            "Linda": [2,1,0,2,0,1,2,2,0,2]

        },
        "surprise": {
            "JohnGabby": [3,0,1,2,1,3,2,0,1,3],
            "CarlFan51": [2,0,1,2,1,1,2,0,1,3],
            "BatgirlZoe": [2,0,1,0,1,3,2,0,1,3],
            "Linda": [2,0,1,3,1,3,2,0,1,3]
        }
    }
answers_base ={
        "gaming": {
            "JohnGabby": [1,3,1,0,1,2,1,2,1,2],
            "CarlFan51": [1,3,1,0,2,3,1,2,1,2],
            "BatgirlZoe": [1,3,1,0,2,3,1,1,2,3],
            "Linda": [3,2,1,2,1,2,1,2,1,2]
        },
        "godot": {
            "JohnGabby": [2,1,0,2,0,1,2,3,0,2],
            "CarlFan51": [2,1,0,2,3,1,2,2,0,2],
            "BatgirlZoe": [2,1,0,2,0,1,2,2,0,3],
            "Linda": [2,1,0,2,0,1,2,2,0,2]

        },
        "surprise": {
            "JohnGabby": [3,0,1,2,1,3,2,0,1,3],
            "CarlFan51": [2,0,1,2,1,1,2,0,1,3],
            "BatgirlZoe": [2,0,1,0,1,3,2,0,1,3],
            "Linda": [2,0,1,3,1,3,2,0,1,3]
        }
    }

@app.route("/reset")
def reset():
    key = request.args['key']
    if key == "pls":
        global candidates
        global answers
        candidates = candidates_base
        answers = answers_base
        save_all()
        return("Reset OK")
    else:
        return("Fuck off")

@app.route("/test")
def testf():
    return jsonify(answers)

@app.route("/fghj", methods = ["GET", "POST",])
def add_answers():
    global candidates
    global answers
    content = request.json
    if content["key"] == "dlt52k":
        if content["name"] == "Anonymous": return("No")
        if not content["name"] in candidates:
            candidates[content["name"]] = {
                "body" : content["body"],
                "head" : content["head"],
                content["category"] : content["answers"]
                }

        if not content["name"] in answers[content["category"]]:
            answers[content["category"]][content["name"]] = content["answers"]
        save_all()
        return("OK")
    else:
        return("No")

@app.route("/is_unique")
def is_unique():
    global candidates
    name_to_check = request.args['name']
    unique = name_to_check in candidates
    return unique

@app.route("/")
def hello():
    return "5000"

@app.route("/get_answers")
def get_answers():
    return jsonify(answers)

@app.route("/get_candidates")
def get_candidates():
    return jsonify(candidates)

@app.route("/get_lobbies")
def get_lobby():
    lobbies = {"lobbies": {}}
    for category in ["gaming", "godot", "surprise"]:
        lobbies["lobbies"][category] = []
        sampling = random.sample(list(answers[category]), k=4)
        for k in sampling:
            candidate = {
                "name": k,
                "body": candidates[k]["body"],
                "head": candidates[k]["head"],
                "answers": answers[category][k]
            }
            lobbies["lobbies"][category].append(candidate)

    return jsonify(lobbies)

@app.route("/ping")
def ping():
    return "pong"

@app.route("/save")
def save_all():
    save_candidates()
    save_answers()
    return "ok"

def save_candidates():    
    with open('candidates.json', 'w') as outfile:
        json.dump(candidates, outfile)

def save_answers():    
    with open('answers.json', 'w') as outfile:
        json.dump(answers, outfile)

def load_all():
    load_candidates()
    load_answers()

def load_candidates():
    with open('candidates.json') as json_file:
        global candidates
        candidates = json.load(json_file)

def load_answers():
    with open('answers.json') as json_file:
        global answers
        answers = json.load(json_file)

if __name__ == "__main__":
    load_all()
    app.run()

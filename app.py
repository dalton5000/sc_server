from flask import Flask, request
from flask import jsonify
import random, json

app = Flask(__name__)

candidates = {
    "Linda": {
        "body": "9",
        "head": "7"
        },
    "Larry": {
        "body": "2",
        "head": "2"
        },
    "Zoe": {
        "body": "7",
        "head": "4"
        },
    "Randy": {
        "body": "4",
        "head": "10"
        }
    }

candidates_base = {
    "Randy": {
        "body": "9",
        "head": "7"
        },
    "Larry": {
        "body": "2",
        "head": "2"
        },
    "Zoe": {
        "body": "7",
        "head": "4"
        },
    "Linda": {
        "body": "4",
        "head": "10"
        }
    }

answers = {
        "gaming": {
            "Randy": [2,2,1,2,1,2,1,2,1,2],
            "Larry": [3,2,1,2,1,2,1,2,1,2],
            "Zoe": [3,2,1,2,1,2,1,2,1,2],
            "Linda": [3,2,1,2,1,2,1,2,1,2]
        },
        "godot": {
            "Randy": [3,2,1,2,1,2,1,2,1,2],
            "Larry": [3,2,1,2,1,2,1,2,1,2],
            "Zoe": [3,2,1,2,1,2,1,2,1,2],
            "Linda": [3,2,1,2,1,2,1,2,1,2]

        },
        "surprise": {
            "Randy": [3,2,1,2,1,2,1,2,1,2],
            "Larry": [3,2,1,2,1,2,1,2,1,2],
            "Zoe": [3,2,1,2,1,2,1,2,1,2],
            "Linda": [3,2,1,2,1,2,1,2,1,2]
        }
    }
answers_base = {
        "gaming": {
            "Randy": [2,2,1,2,1,2,1,2,1,2],
            "Larry": [3,2,1,2,1,2,1,2,1,2],
            "Zoe": [3,2,1,2,1,2,1,2,1,2],
            "Linda": [3,2,1,2,1,2,1,2,1,2]
        },
        "godot": {
            "Randy": [3,2,1,2,1,2,1,2,1,2],
            "Larry": [3,2,1,2,1,2,1,2,1,2],
            "Zoe": [3,2,1,2,1,2,1,2,1,2],
            "Linda": [3,2,1,2,1,2,1,2,1,2]

        },
        "surprise": {
            "Randy": [3,2,1,2,1,2,1,2,1,2],
            "Larry": [3,2,1,2,1,2,1,2,1,2],
            "Zoe": [3,2,1,2,1,2,1,2,1,2],
            "Linda": [3,2,1,2,1,2,1,2,1,2]
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

@app.route("/add_answers", methods = ["GET", "POST",])
def add_answers():
    global candidates
    content = request.json
    if content["key"] == "dlt5k":
        if content["name"] == "Anonymous": return("No")
        if not content["name"] in candidates:
            candidates[content["name"]] = {
                "body" : content["body"],
                "head" : content["body"],
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
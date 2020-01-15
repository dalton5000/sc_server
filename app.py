from flask import Flask, request
from flask import jsonify
import random

app = Flask(__name__)

candidates = {
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
            "Randy": [3,2,1,2,1,2,1,2,1,2],
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
        # candidates = candidates_base
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
        if not content["name"] in candidates:
            candidates[content["name"]] = {
                "body" : content["body"],
                "head" : content["body"],
                content["category"] : content["answers"]
                }

        if not content["name"] in answers[content["category"]]:
            answers[content["category"]][content["name"]] = content["answers"]

        return("OK")
    else:
        return("Fuck off")

@app.route("/is_unique")
def is_unique():
    global candidates
    name_to_check = request.args['name']


@app.route("/")
def hello():
    return "Hello from Dalton!"

@app.route("/get_all")
def get_candidates():
    return jsonify(candidates)

@app.route("/get_lobby")
def get_lobby():
    category = request.args["category"]
    sampling = random.choices(answers[category], k=3)
    lobby = []

    return jsonify(sampling)

if __name__ == "__main__":
    app.run()


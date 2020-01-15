from flask import Flask, request
from flask import jsonify
app = Flask(__name__)

test = {}

candidates = {
    "Randy": {
        "body": "9",
        "head": "7",
        "gaming": "3,2,1,2,1,2,1,2,1,2",
        "godot": "3,2,1,2,1,2,1,2,1,2",
        "surprise": "3,2,1,2,1,2,1,2,1,2",
        },
    "Larry": {
        "body": "2",
        "head": "2",
        "gaming": "2,2,1,2,1,2,1,2,1,2",
        "godot": "3,2,1,2,1,2,1,2,1,2",
        "surprise": "3,2,1,2,1,2,1,2,1,2",
        },
    "Zoe": {
        "body": "7",
        "head": "4",
        "gaming": "1,2,1,2,1,2,1,2,1,2",
        "godot": "3,2,1,2,1,2,1,2,1,2",
        "surprise": "3,2,1,2,1,2,1,2,1,2" }
        ,
    "Linda": {
        "body": "4",
        "head": "10",
        "gaming": "2,2,1,2,1,2,1,2,1,2",
        "godot": "3,2,1,2,1,2,1,2,1,2",
        "surprise": "3,2,1,2,1,2,1,2,1,2",
        },
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
    return jsonify(test)

@app.route("/add_answers", methods = ["GET", "POST",])
def add_answers():
    global test
    test = request.json
    global candidates
    content = request.json
    print(content)
    # else:
    #     return("Fuck off")

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
    p_set = get_player_set()
    return jsonify(candidates)

if __name__ == "__main__":
    app.run()


def get_player_set():
    p_set = []
    for i in range(0,4):
        string = "Somename,8,8;1,2,1,2,1,2,1,2,1,2"
        p_set.append(string)
    return p_set
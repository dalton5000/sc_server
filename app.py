from flask import Flask, request
from flask import jsonify
app = Flask(__name__)

candidates = [
    "Dalton,8,8;1,2,1,2,1,2,1,2,1,2",
    "Donald,2,2;1,2,1,2,1,2,1,2,1,2",
]

@app.route("/add_candidate")
def add_candidate():
    data = request.args['data'].split("#")
    print(data)
    return jsonify(data)
    # if data[0] == "dlt5k":
    #     candidate_string = data[1]

    #     print("added " + candidate_string)
    #     candidates.append(candidate_string)
    #     return("Thank you")
    # else:
    #     return("Fuck off")

@app.route("/")
def hello():
    return "Hello from Dalton!"

@app.route("/get_all_candidates")
def get_candidates():
    return jsonify(candidates)

@app.route("/get_lobby")
def get_lobby():
    p_set = get_player_set()
    return jsonify(p_set)

if __name__ == "__main__":
    app.run()


def get_player_set():
    p_set = []
    for i in range(0,4):
        string = "Somename,8,8;1,2,1,2,1,2,1,2,1,2"
        p_set.append(string)
    return p_set
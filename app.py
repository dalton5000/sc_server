from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Dalton!"

@app.route("/get_set")
def get_set():
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
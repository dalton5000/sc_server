from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Dalton!"

@app.route("/get_set")
    p_set = get_player_set()
    return p_set

if __name__ == "__main__":
    app.run()


def get_player_set():
    p_set = []
    for i in 4:
        string = "Somename,8,8;1,2,1,2,1,2,1,2,1,2"
        p_set.append(string)
    return p_set
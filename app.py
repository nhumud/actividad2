from flask import Flask

app = Flask(__name__)

@app.route("/status", methods=['GET'])
def status():
    return ('', 204)


@app.route("/info", methods=['GET'])
def info():
    server = {"url": "https://actividad2-nicolas-humud.herokuapp.com/"}
    return (server, 200)


@app.route("/security", methods=['DELETE'])
def security():
    return ('', 401)
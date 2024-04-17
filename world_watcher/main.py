import json

from flask import Flask

from .world_checker import poll_servers

app = Flask(__name__)


@app.route("/watcher")
def watcher():
    result = {"online": poll_servers(80.00, 10)}
    return json.dumps(result)

import json

from flask import Flask

from .world_checker import poll_servers

app = Flask(__name__)


@app.route("/watcher")
def watcher():
    result = {
        "online": poll_servers(
            threshhold=0.8,
            pool_size=10,
        )
    }
    return json.dumps(result)

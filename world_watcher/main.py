import datetime as dt
import json

from flask import Flask

from .cache import cache
from .world_checker import poll_servers

app = Flask(__name__)


def update_cache():
    cache["status"] = poll_servers(threshhold=0.8, pool_size=10)
    cache["last_update"] = dt.datetime.now()


@app.route("/watcher")
def watcher():
    if not cache["status"]:
        update_cache()

    if cache["last_update"]:
        time_since_last_update = dt.datetime.now() - cache["last_update"]
        if time_since_last_update.seconds > 60:
            update_cache()

    result = {"online": cache["status"]}
    return json.dumps(result)

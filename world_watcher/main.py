import datetime as dt
import json

from flask import Flask, render_template

from .cache import cache
from .world_checker import poll_servers

app = Flask(__name__)


async def update_cache():
    cache["status"] = await poll_servers(threshhold=0.8, pool_size=10)
    cache["last_update"] = dt.datetime.now()


async def check_cache():
    if cache["status"] is None or cache["last_update"] is None:
        await update_cache()
        return

    if cache["last_update"]:
        time_since_last_update = dt.datetime.now() - cache["last_update"]
        if time_since_last_update.seconds > 60:
            await update_cache()


@app.route("/watcher")
async def watcher():
    await check_cache()
    result = {"online": cache["status"]}
    return json.dumps(result)


@app.route("/")
async def index():
    await check_cache()
    return render_template("index.html", status="OSRS is online!" if cache["status"] else "OSRS is offline.")


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()

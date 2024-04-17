import datetime as dt
from typing import TypedDict


class OSRSServerStatusCache(TypedDict):
    status: None | bool
    last_update: None | dt.datetime


cache: OSRSServerStatusCache = {
    "status": None,
    "last_update": None,
}

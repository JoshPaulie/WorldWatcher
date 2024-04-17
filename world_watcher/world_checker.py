import random
import statistics

from ping import ping

# OSRS server IPs for the first 100 servers (Worlds 300 - 400)
worlds_servers = [f"oldschool{n}.runescape.com" for n in range(1, 101)]


def poll_servers(threshhold: float, size: int):
    """Determines if OSRS world servers are online by randomly polling a number of worlds."""
    server_pool = random.choices(worlds_servers, k=size)
    pool_response_times = [ping(address) for address in server_pool]
    pool_online_results = statistics.mean([bool(response_time) for response_time in pool_response_times])
    if pool_online_results > threshhold:
        return True
    return False


print(poll_servers(0.80, 10))

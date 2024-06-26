import asyncio
import random
import statistics

from .ping import ping

# OSRS server IPs for the first 100 servers (Worlds 300 - 400)
worlds_servers = [f"oldschool{n}.runescape.com" for n in range(1, 101)]


async def poll_servers(*, threshhold: float, pool_size: int) -> bool:
    """Determines if OSRS world servers are online by randomly polling a number of worlds. If the percent of worlds online (ie. respond back) exceeds the threshhold, the game is considered 'online'"""
    # Random selection of servers to query
    server_pool = random.choices(worlds_servers, k=pool_size)

    # Create tasks for each server ping
    tasks = [asyncio.create_task(ping(address)) for address in server_pool]

    # Wait for all tasks to complete
    await asyncio.gather(*tasks)

    # Collect results from tasks
    pool_response_times = [task.result() for task in tasks]

    # Determine % of servers that responded
    pool_response_results = statistics.mean([bool(response_time) for response_time in pool_response_times])

    # If exceeds theshhold, game is considered 'online'
    if pool_response_results > threshhold:
        return True
    return False

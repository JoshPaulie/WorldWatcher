import asyncio
import os
import re


class NonPosixEnvironment(Exception):
    pass


async def ping(address: str) -> float | None:
    """(Very) crude wrapping around unix ping binary. Returns server response time in milliseconds, or None if the server is unavailable in someway.

    Assumptions:
        - All unix/posix environments use the same (or similar enough) ping binary
        - This ping exits with error if host can't be resolved
        - Passed address eventually resolves to IPv4
    """
    if os.name != "posix":
        raise NonPosixEnvironment("Function only wraps posix ping command")

    process = await asyncio.create_subprocess_exec(
        "ping",
        "-c",
        "1",
        address,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()

    if process.returncode != 0:
        # It seems ping helpfully exits with an error if the response took too long,
        # or if the server is unavailable.
        return None

    ping_result = stdout.decode()
    response_ms = re.search(r"time=(\d+\.\d+)", ping_result)
    if response_ms:
        return float(response_ms.group(1))
    # Covers: Ping doesn't get response, but doesn't exit with error for some reason
    return None

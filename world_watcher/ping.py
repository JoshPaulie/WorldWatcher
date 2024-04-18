import os
import re
import subprocess


class NonPosixEnvironment(Exception):
    pass


async def ping(address: str) -> float | None:
    """(Very) crude wrapping around unix ping binary. Returns server response time in milliseconds

    Assumptions:
        - All unix/posix environments use the same (or similar enough) ping binary
        - This ping exits with error if host can't be resolved
        - Passed address eventually resolves to IPv4
    """
    if os.name != "posix":
        raise NonPosixEnvironment("Function only wraps posix ping command")

    try:
        ping_result = subprocess.check_output(["ping", "-c", "1", address], stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        # Covers: Ping command exits with error.
        # Likely because the server couldn't be resolved (unknown host)
        return None

    ping_result = ping_result.decode()
    response_ms = re.search(r"time=(\d+\.\d+)", ping_result)
    if response_ms:
        return float(response_ms.group(1))
    # Covers: Server took too long to reply
    # Covers: Server is unavailable
    return None

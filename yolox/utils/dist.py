"""
multi-gpu communication
"""
from paddle import distributed as dist


def get_rank() -> int:
    return dist.get_rank()


from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Process:
    pid: str
    arrival: int
    burst: int
    priority: int
    original_index: int
    remaining: int = field(init=False)
    start_time: Optional[int] = None
    finish_time: Optional[int] = None

    def __post_init__(self):
        self.remaining = self.burst

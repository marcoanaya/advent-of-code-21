from dataclasses import dataclass
from typing import Optional, TypeVar

@dataclass
class Index:
    i: int = 0
    def get(self) -> int:
        return self.i
    def inc(self, n: int) -> int:
        self.i += n
        return self.i
    def __str__(self) -> str:
        return f"Index({self.i})"

T = TypeVar('T')
def unwrap(x: Optional['T']) ->  'T':
    assert x is not None
    return x

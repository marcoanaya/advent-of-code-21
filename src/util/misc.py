from dataclasses import dataclass

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

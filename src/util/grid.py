

from queue import PriorityQueue
from typing import Any, Callable, DefaultDict, Generator, Optional


class Grid(list):
    def shortest_path(self, start: Optional[tuple[int, int]]=None, end: Optional[tuple[int, int]]=None) -> int:
        start = start or (0, 0)
        end = end or (len(self) - 1, len(self[0]) - 1)
        cache = DefaultDict[tuple[int, int], float](lambda: float('inf'), {start: 0})
        pq = PriorityQueue[tuple[int, tuple[int, int]]]()
        pq.put((0, start))

        seen: set[tuple[int, int]] = set()
        while not pq.empty():
            val, (i, j) = pq.get()
            if (i, j) == end:
                return val
            if (i, j) in seen:
                continue
            seen.add((i,j))

            def f(n: int, m: int) -> None:
                if (new_val := val + self[n][m]) < cache[(n, m)]:
                    cache[(n, m)] = new_val
                    pq.put((new_val, (n, m)))
            any(self.neighbormap(i, j, f, diag=False))

        raise Exception(f"end: {end} not found.")

    def apply(self, f: Callable[[Any], Any]) -> None:
        for i in range(len(self)):
            for j in range(len(self[0])):
                self[i][j] = f(self[i][j])

    def neighbormap(self, i: int, j: int, f: Callable[[int, int], Any], diag:bool=True) -> Generator[Any, None, None]:
        yield from (f(n, m) for n,m in self.get_directions(i, j, diag) if self.is_inbounds(n, m))

    def flatmap(
        self, f: Callable[[int, int], Any], cond: Callable[[int, int], bool]=lambda i, j: True
    ) -> Generator[Any, None, None]:
        yield from (f(i, j) for i in range(len(self)) for j in range(len(self[0])) if cond(i, j))

    @staticmethod
    def get_directions(i: int, j: int, diag: bool) -> list[tuple[int, int]]:
        return [
            (n, m) for m in range(j-1, j+2) for n in range(i-1, i+2)
            if ((n != i or m != j) if diag else (n != i) != (m != j))
        ]

    def is_inbounds(self, i: int, j: int) -> bool:
        return 0 <= i < len(self) and 0 <= j < len(self[0])

    def __str__(self) -> str:
        return '\n'.join(','.join(map(str, r)) for r in self)

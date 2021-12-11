

from typing import Any, Callable, Generator


class Grid(list):
    def apply(self, f: Callable[[Any], Any]) -> None:
        for i in range(len(self)):
            for j in range(len(self[0])):
                self[i][j] = f(self[i][j])
    
    def neighbormap(self, i: int, j: int, f: Callable[[int, int], Any]) -> Generator[Any, None, None]:
        yield from (f(n, m) for n,m in self.get_directions(i, j) if self.is_inbounds(n, m))
    
    def flatmap(
        self, f: Callable[[int, int], Any], cond: Callable[[int, int], bool]=lambda i, j: True
    ) -> Generator[Any, None, None]:
        yield from (f(i, j) for i in range(len(self)) for j in range(len(self[0])) if cond(i, j))

    def get_directions(self, i: int, j: int) -> list[tuple[int, int]]:
        return [(n, m) for m in range(j-1, j+2) for n in range(i-1, i+2) if (n != i or m != j)]

    def is_inbounds(self, i: int, j: int) -> bool:
        return 0 <= i < len(self) and 0 <= j < len(self[0])
    
    def __str__(self) -> str:
        return '\n'.join(','.join(map(str, r)) for r in self)
from typing import Any, Callable, Generator
from .abstract_day import AbstractDay
from ..util.file_util import FileUtil

class Day11(AbstractDay):
    @staticmethod
    def input(file_name: str) -> Any:
        return Day11.Octopi(FileUtil.file_to_list(file_name, f=lambda x: list(map(int, x))))

    @staticmethod
    def one(data: 'Day11.Octopi') -> int:
        return data.simulate()[0]

    @staticmethod
    def two(data: 'Day11.Octopi') -> int:
        return data.simulate(cond=lambda _: any(data.flatmap(lambda i, j: data[i][j])))[1]
    
    class Octopi(list):
        def simulate(self, cond: Callable[[int], bool]=lambda c: c < 100) -> tuple[int, int]:
            count, flashes = 0, 0
            while cond(count):
                self.apply(lambda x: x+1)
                seen: set[tuple[int, int]] = set()
                flashes += sum(self.flatmap(lambda i, j: self.flash_nine(i, j, seen), cond=lambda i, j: self[i][j] > 9))
                count += 1
                self.apply(lambda x: 0 if x > 9 else x)
            return flashes, count

        def apply(self, f: Callable[[Any], Any]) -> None:
            for i in range(len(self)):
                for j in range(len(self[0])):
                    self[i][j] = f(self[i][j])

        def flash_nine(self, i: int, j: int, seen: set[tuple[int, int]], is_nine:bool=True) -> int:
            if (i, j) in seen:
                return 0
            self[i][j] += not is_nine
            if self[i][j] <= 9:
                return 0
            seen.add((i, j))
            return 1 + sum(self.neighbormap(i, j, lambda n, m: self.flash_nine(n, m, seen, is_nine=False)))
        
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
            return '\n'.join(''.join(map(str, r)) for r in self)

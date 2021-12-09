import math
from typing import Any, Callable, Generator
from .abstract_day import AbstractDay
from ..util.file_util import FileUtil

class Day9(AbstractDay):
    @staticmethod
    def input(file_name: str) -> 'Day9.HeightMap':
        return Day9.HeightMap(FileUtil.file_to_list(file_name, f=lambda x: list(map(int, x))))

    @staticmethod
    def one(data: 'Day9.HeightMap') -> int:
        return sum(data.flatmap(lambda i, j: data[i][j] + 1, cond=data.is_low_point))

    @staticmethod
    def two(data: 'Day9.HeightMap') -> int:
        seen: set[tuple[int, int]] = set()
        return math.prod(sorted(data.flatmap(lambda i, j: data.search_basin(i, j, seen)))[-3:])

    class HeightMap(list):
        def is_low_point(self, i: int, j: int) -> bool:
            return all(self.neighbormap(i, j, lambda n, m: self[n][m] > self[i][j]))

        def search_basin(self, i: int, j: int, seen: set[tuple[int, int]]) -> int:
            if self[i][j] == 9 or (i, j) in seen:
                return 0
            seen.add((i, j))
            return 1 + sum(self.neighbormap(i, j, lambda n, m: self.search_basin(n, m, seen)))

        def flatmap(
            self, f: Callable[[int, int], Any], cond: Callable[[int, int], bool]=lambda i, j: True
        ) -> Generator[Any, None, None]:
            yield from (f(i, j) for i in range(len(self)) for j in range(len(self[0])) if cond(i, j))

        def neighbormap(self, i: int, j: int, f: Callable[[int, int], Any]) -> Generator[Any, None, None]:
            yield from (f(n, m) for n,m in self.get_directions(i, j) if self.is_inbounds(n, m))

        def is_inbounds(self, i: int, j: int) -> bool:
            return 0 <= i < len(self) and 0 <= j < len(self[0])

        @staticmethod
        def get_directions(i: int, j: int) -> list[tuple[int, int]]:
            return [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]

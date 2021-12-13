import math
from .abstract_day import AbstractDay
from ..util.file_util import FileUtil
from ..util.grid import Grid

class Day9(AbstractDay):
    @classmethod
    def input(cls, file_name: str) -> 'Day9.HeightMap':
        return Day9.HeightMap(FileUtil.file_to_list(file_name, f=lambda x: list(map(int, x))))

    @classmethod
    def one(cls, data: 'Day9.HeightMap') -> int:
        return sum(data.flatmap(lambda i, j: data[i][j] + 1, cond=data.is_low_point))

    @classmethod
    def two(cls, data: 'Day9.HeightMap') -> int:
        seen: set[tuple[int, int]] = set()
        return math.prod(sorted(data.flatmap(lambda i, j: data.search_basin(i, j, seen)))[-3:])

    class HeightMap(Grid):
        def is_low_point(self, i: int, j: int) -> bool:
            return all(self.neighbormap(i, j, lambda n, m: self[n][m] > self[i][j]))

        def search_basin(self, i: int, j: int, seen: set[tuple[int, int]]) -> int:
            if self[i][j] == 9 or (i, j) in seen:
                return 0
            seen.add((i, j))
            return 1 + sum(self.neighbormap(i, j, lambda n, m: self.search_basin(n, m, seen)))

        @staticmethod
        def get_directions(i: int, j: int) -> list[tuple[int, int]]:
            return [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]

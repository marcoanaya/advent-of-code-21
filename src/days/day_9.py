import math
from .abstract_day import AbstractDay
from ..util.file_util import FileUtil

class Day9(AbstractDay):
    @staticmethod
    def input(file_name: str) -> list[list[int]]:
        return FileUtil.file_to_list(file_name, f=lambda x: list(map(int, x)))

    @staticmethod
    def one(data: list[list[int]]) -> int:
        count = 0
        for i in range(len(data)):
            for j in range(len(data[i])):
                if all(
                    data[n][m] > data[i][j]
                    for n,m in Day9.get_directions(i, j)
                    if 0 <= n < len(data) and 0 <= m < len(data[i])
                ):
                    count += data[i][j] + 1
        return count

    @staticmethod
    def two(data: list[list[int]]) -> int:
        seen = set()
        basins=[]
        def helper(i: int, j: int) -> int:
            if not (0 <= i < len(data) and 0 <= j < len(data[i])):
                return 0
            if data[i][j] == 9 or (i, j) in seen:
                return 0
            seen.add((i, j))
            return 1 + sum(helper(n, m) for n, m in Day9.get_directions(i, j))

        for i in range(len(data)):
            for j in range(len(data[i])):
                basins.append(helper(i, j))
        return math.prod(sorted(basins)[-3:])

    @staticmethod
    def get_directions(i: int, j: int) -> list[tuple[int, int]]:
        return [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]

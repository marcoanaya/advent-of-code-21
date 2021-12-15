from .abstract_day import AbstractDay
from ..util.file_util import FileUtil
from ..util.grid import Grid

class Day15(AbstractDay):
    @classmethod
    def input(cls, file_name: str) -> 'Day15.Cavern':
        return Day15.Cavern(FileUtil.file_to_list(file_name, f=lambda x: list(map(int, list(x)))))

    @classmethod
    def one(cls, cavern: 'Day15.Cavern') -> int:
        return cavern.shortest_path()
    @classmethod
    def two(cls, cavern: 'Day15.Cavern') -> int:
        big_cavern = cavern.scale(5)
        return big_cavern.shortest_path()

    class Cavern(Grid):
        def scale(self, n: int) -> 'Day15.Cavern':
            return Day15.Cavern([[self.get_scaled(i, j) for j in range(len(self[0]) * n)]for i in range(len(self) * n)])

        def get_scaled(self, i: int, j: int) -> int:
            return (((i // len(self) + j // len(self[0]) + self[i % len(self)][j % len(self[0])]) - 1) % 9) + 1

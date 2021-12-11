from .abstract_day import AbstractDay
from ..util.file_util import FileUtil

class Day6(AbstractDay):
    @classmethod
    def input(cls, file_name: str) -> list[int]:
        return FileUtil.file_to_list(file_name, f=int, delim=',')

    @classmethod
    def one(cls, data: list[int]) -> int:
        return cls.FishTracker(data).simulate(80)

    @classmethod
    def two(cls, data: list[int]) -> int:
        return cls.FishTracker(data).simulate(256)

    class FishTracker:
        def __init__(self, fishes: list[int]) -> None:
            self.fish_tracker = [0] * 9
            for fish in fishes:
                self.fish_tracker[fish] += 1

        def simulate(self, days: int) -> int:
            for _ in range(days):
                new_parents = self.fish_tracker[0]
                self.fish_tracker[:-1] = self.fish_tracker[1:]
                self.fish_tracker[6] += new_parents
                self.fish_tracker[8] = new_parents
            return sum(self.fish_tracker)
        
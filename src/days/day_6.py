from .abstract_day import AbstractDay
from ..util.file_util import FileUtil

class Day6(AbstractDay):
    @staticmethod
    def input(file_name: str) -> list[int]:
        return FileUtil.file_to_list(file_name, f=int, delim=',')

    @staticmethod
    def one(data: list[int]) -> int:
        return Day6.FishTracker(data).simulate(80)

    @staticmethod
    def two(data: list[int]) -> int:
        return Day6.FishTracker(data).simulate(256)

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
        
from typing import DefaultDict
from .abstract_day import AbstractDay
from ..util.file_util import FileUtil

class Day6(AbstractDay):
    @staticmethod
    def one() -> int:
        fishes = FileUtil.file_to_numbers(Day6.get_file_name(''))
        return Day6.FishTracker(fishes).simulate(80)

    @staticmethod
    def two() -> int:
        fishes = FileUtil.file_to_numbers(Day6.get_file_name(''))
        return Day6.FishTracker(fishes).simulate(256)

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
        
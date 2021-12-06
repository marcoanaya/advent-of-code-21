from .abstract_day import AbstractDay
from ..util.file_util import FileUtil

class Day1(AbstractDay):
    @staticmethod
    def input() -> list[int]:
        return FileUtil.file_to_list(Day1.get_file_name(), f=int)

    @staticmethod
    def one() -> int:
        measurements = Day1.input()
        return sum(
            int(measurements[i] - measurements[i-1] > 0)
            for i in range(1, len(measurements))
        )

    @staticmethod
    def two() -> int:
        measurements = Day1.input()
        count = 0
        for i in range(1, len(measurements) - 2):
            first = sum(measurements[i-1:i+2])
            second = sum(measurements[i:i+3])
            if second > first:
                count +=1
        return count

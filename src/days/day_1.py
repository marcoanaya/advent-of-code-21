from .abstract_day import AbstractDay
from ..util.file_util import FileUtil

class Day1(AbstractDay):
    @staticmethod
    def one() -> int:
        measurements = list(map(int, FileUtil.file_to_list(Day1.get_file_name())))
        return sum(
            int(measurements[i] - measurements[i-1] > 0)
            for i in range(1, len(measurements))
        )

    @staticmethod
    def two() -> int:
        measurements = list(map(int, FileUtil.file_to_list(Day1.get_file_name())))
        count = 0
        for i in range(1, len(measurements) - 2):
            first = sum(measurements[i-1:i+2])
            second = sum(measurements[i:i+3])
            if second > first:
                count +=1
        return count

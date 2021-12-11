from .abstract_day import AbstractDay
from ..util.file_util import FileUtil

class Day1(AbstractDay):
    @classmethod
    def input(cls, file_name: str) -> list[int]:
        return FileUtil.file_to_list(file_name, f=int)

    @classmethod
    def one(cls, data: list[int]) -> int:
        return sum(
            int(data[i] - data[i-1] > 0)
            for i in range(1, len(data))
        )

    @classmethod
    def two(cls, data: list[int]) -> int:
        count = 0
        for i in range(1, len(data) - 2):
            first = sum(data[i-1:i+2])
            second = sum(data[i:i+3])
            if second > first:
                count +=1
        return count

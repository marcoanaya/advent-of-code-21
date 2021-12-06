from .abstract_day import AbstractDay
from ..util.file_util import FileUtil

class Day7(AbstractDay):
    @staticmethod
    def input() -> list[str]:
        return FileUtil.file_to_list(Day7.get_file_name())

    @staticmethod
    def one() -> int:
        pass

    @staticmethod
    def two() -> int:
        pass

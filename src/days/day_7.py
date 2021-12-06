from typing import Any
from .abstract_day import AbstractDay
from ..util.file_util import FileUtil

class Day7(AbstractDay):
    @staticmethod
    def input(file_name: str) -> Any:
        return FileUtil.file_to_list(file_name)

    @staticmethod
    def one(data: Any) -> int:
        pass

    @staticmethod
    def two(data: Any) -> int:
        pass

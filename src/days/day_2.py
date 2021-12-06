from abc import ABC, abstractmethod
from .abstract_day import AbstractDay
from ..util.file_util import FileUtil


class Day2(AbstractDay):
    @staticmethod
    def input(file_name: str) -> list[str]:
        return FileUtil.file_to_list(file_name)

    @staticmethod
    def one(data: list[str]) -> int:
        return Day2.SimpleNavigator().navigate(data)

    @staticmethod
    def two(data: list[str]) -> int:
        return Day2.AdvanceNavigator().navigate(data)

    class AbstractNavigator(ABC):
        def __init__(self) -> None:
            self.horiz: int = 0
            self.depth: int = 0
        @abstractmethod
        def down(self, x: int) -> None:
            pass
        @abstractmethod
        def up(self, x: int) -> None:
            pass
        @abstractmethod
        def forward(self, x: int) -> None:
            pass
        def navigate(self, course: list[str]) -> int:
            for command in course:
                direction, x = command.split()
                getattr(self, direction)(int(x))
            return self.horiz * self.depth

    class SimpleNavigator(AbstractNavigator):
        def down(self, x: int) -> None:
            self.depth += x
        def up(self, x: int) -> None:
            self.depth -= x
        def forward(self, x: int) -> None:
            self.horiz += x

    class AdvanceNavigator(AbstractNavigator):
        def __init__(self) -> None:
            super().__init__()
            self.aim: int = 0
        def down(self, x: int) -> None:
            self.aim += x
        def up(self, x: int) -> None:
            self.aim -= x
        def forward(self, x: int) -> None:
            self.horiz += x
            self.depth += self.aim * x

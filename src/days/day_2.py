from abc import ABC, abstractmethod
from .abstract_day import AbstractDay
from ..util.file_util import FileUtil


class Day2(AbstractDay):
    @staticmethod
    def one() -> int:
        course = FileUtil.file_to_list(Day2.get_file_name())
        return Day2.NavigatorOne().navigate(course)

    @staticmethod
    def two() -> int:
        course = FileUtil.file_to_list(Day2.get_file_name())
        return Day2.NavigatorTwo().navigate(course)

    class AbstractNavigator(ABC):
        horiz: int = 0
        depth: int = 0
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

    class NavigatorOne(AbstractNavigator):
        def down(self, x: int) -> None:
            self.depth += x
        def up(self, x: int) -> None:
            self.depth -= x
        def forward(self, x: int) -> None:
            self.horiz += x

    class NavigatorTwo(AbstractNavigator):
        aim: int = 0
        def down(self, x: int) -> None:
            self.aim += x
        def up(self, x: int) -> None:
            self.aim -= x
        def forward(self, x: int) -> None:
            self.horiz += x
            self.depth += self.aim * x

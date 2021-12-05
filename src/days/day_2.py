from dataclasses import dataclass
from .abstract_day import AbstractDay
from ..util.file_util import FileUtil

@dataclass
class PositionOne:
    horiz: int = 0
    depth: int = 0
    def down(self, x: int) -> None:
        self.depth += x
    def up(self, x: int) -> None:
        self.depth -= x
    def forward(self, x: int) -> None:
        self.horiz += x

@dataclass
class PositionTwo:
    horiz: int = 0
    depth: int = 0
    aim: int = 0
    def down(self, x: int) -> None:
        self.aim += x
    def up(self, x: int) -> None:
        self.aim -= x
    def forward(self, x: int) -> None:
        self.horiz += x
        self.depth += self.aim * x

class Day2(AbstractDay):
    @staticmethod
    def one() -> int:
        course = FileUtil.file_to_list(Day2.get_file_name())
        pos = PositionOne()
        for command in course:
            direction, x = command.split()
            getattr(pos, direction)(int(x))

        return pos.horiz * pos.depth

    @staticmethod
    def two() -> int:
        course: list[str] = FileUtil.file_to_list(Day2.get_file_name())
        pos = PositionTwo()
        for command in course:
            direction, x = command.split()
            getattr(pos, direction)(int(x))
        return pos.horiz * pos.depth

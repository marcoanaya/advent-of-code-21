import re
from typing import Callable, DefaultDict
from .abstract_day import AbstractDay
from ..util.file_util import FileUtil


VentLine = list[int]
sign: Callable[[int], int] = lambda x: int(x > 0) - int(x < 0)

class Day5(AbstractDay):
    @classmethod
    def input(cls, file_name: str) -> list[VentLine]:
        return FileUtil.file_to_list(
            file_name, f=lambda l: list(map(int, re.findall(r'\d+', l)))
        )

    @classmethod
    def one(cls, data: list[VentLine]) -> int:
        return cls.Diagram().populate_and_find_dangerous_areas(data, exclude_diagonal=True)

    @classmethod
    def two(cls, data: list[VentLine]) -> int:
        return cls.Diagram().populate_and_find_dangerous_areas(data)

    class Diagram:
        def __init__(self) -> None:
            self.diagram: DefaultDict[tuple[int, int], int] = DefaultDict(int)

        def populate_and_find_dangerous_areas(
            self, vent_lines: list[VentLine], exclude_diagonal: bool=False
        ) -> int:
            for x1, y1, x2, y2 in vent_lines:
                dx, dy = sign(x2-x1), sign(y2-y1)
                if exclude_diagonal and dx and dy:
                    continue
                if x1!= x2 or y1!=y2:
                    self.diagram[(x2, y2)] += 1
                while dx or dy:
                    self.diagram[(x1, y1)] += 1
                    x1 += dx
                    y1 += dy
                    dx, dy = sign(x2-x1), sign(y2-y1)
            return sum(int(val >= 2) for val in self.diagram.values())
            
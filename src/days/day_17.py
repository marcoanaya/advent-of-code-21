import re
from typing import Any, Callable
from .abstract_day import AbstractDay
from ..util.file_util import FileUtil

class Day17(AbstractDay):
    @classmethod
    def input(cls, file_name: str) -> Any:
        line = FileUtil.get_file_lines(file_name)[0]
        x1, x2, y1, y2 = list(map(int, re.findall(r'-?\d+', line)))
        return sorted([x1, x2]), sorted([y1, y2])

    @classmethod
    def one(cls, bounds: Any) -> int:
        i = 1
        f: Callable[[int], float] = lambda n: (n ** 2 + n) / 2
        while f(i) < bounds[0][0]:
            i += 1
        j = 1
        highest = 0
        while j < -min(bounds[1]):
            probe = Day17.Probe(i, j)
            while not probe.is_past_bounds(*bounds):
                probe.step()
                if probe.is_in_bounds(*bounds):
                    highest = probe.max_y
                    break
            j += 1
        return highest

    @classmethod
    def two(cls, bounds: Any) -> int:
        i = 1
        count = 0
        while i < max(bounds[0]) + 1:
            j = min(bounds[1])
            while j < -min(bounds[1]):
                probe = Day17.Probe(i, j)
                while not probe.is_past_bounds(*bounds):
                    probe.step()
                    if probe.is_in_bounds(*bounds):
                        count += 1
                        break
                j += 1
            i += 1
        return count

    class Probe:
        def __init__(self, vx: int, vy: int) -> None:
            self.x = 0
            self.y = 0
            self.vx = vx
            self.vy = vy
            self.max_y = 0

        def step(self) -> None:
            self.x += self.vx
            self.y += self.vy
            self.max_y = max(self.y, self.max_y)
            self.vx -= 1 if self.vx else 0
            self.vy -= 1

        def is_in_bounds(self, x_bounds: tuple[int, int], y_bounds: tuple[int, int]) -> bool:
            return x_bounds[0] <= self.x <= x_bounds[1] and y_bounds[0] <= self.y <= y_bounds[1]

        def is_past_bounds(self, x_bounds: tuple[int, int], y_bounds: tuple[int, int]) -> bool:
            return (x_bounds[1] < self.x and self.vx >= 0) or (y_bounds[0] > self.y and self.vy <= 0)

        def __str__(self) -> str:
            return f"Probe({self.x},{self.y}) => {self.vx}, {self.vy}"

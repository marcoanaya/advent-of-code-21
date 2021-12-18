from enum import Enum
from .abstract_day import AbstractDay
from ..util.file_util import FileUtil

Input = tuple['Day13.Paper', list[tuple['Day13.Axis', int]]]

class Day13(AbstractDay):
    @classmethod
    def input(cls, file_name: str) -> Input:
        points = []
        instructions: list[tuple['Day13.Axis', int]] = []
        for line in FileUtil.get_file_lines(file_name, delim='\n'):
            if ',' in line:
                points.append(list(map(int, line.split(','))))
            elif line:
                a, n = line[11:].split('=')
                instructions.append((Day13.Axis[a], int(n)))
        return cls.Paper(points), instructions

    @classmethod
    def one(cls, data: Input) -> int:
        paper, [(axis, n), *_] = data
        paper.fold(axis, n)
        return len(paper.points)

    @classmethod
    def two(cls, data: Input) -> int:
        paper, instructions = data
        for axis, n in instructions:
            paper.fold(axis, n)
        print(paper)
        return len(paper.points)

    class Paper:
        def __init__(self, points: list[list]) -> None:
            self.points = points

        def fold(self, axis: 'Day13.Axis', n: int) -> None:
            for i in range(len(self.points)):
                prev = self.points[i][axis.value]
                self.points[i][axis.value] = prev if prev <= n else n+n - prev
            self.points = list(map(list,set(map(tuple, self.points))))

        def __str__(self) -> str:
            max_x = max(x for x, _ in self.points)
            max_y = max(y for _, y in self.points)
            matrix = [['#' if [x, y] in self.points else '.'  for x in range(max_x+1)] for y in range(max_y+1)]
            return '\n'.join(''.join(row) for row in matrix)

    class Axis(Enum):
        x=0
        y=1
            
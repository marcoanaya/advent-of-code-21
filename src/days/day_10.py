from typing import Any
from functools import reduce
from .abstract_day import AbstractDay
from ..util.file_util import FileUtil

class Day10(AbstractDay):
    char_map = {')': '(', ']': '[', '}': '{', '>': '<'}

    @staticmethod
    def input(file_name: str) -> list[list[str]]:
        return FileUtil.file_to_list(file_name, f=list)

    @staticmethod
    def one(data: list[list[str]]) -> int:
         return Day10.helper(data)[0]

    @staticmethod
    def two(data: list[list[str]]) -> int:
        return Day10.helper(data)[1]
    
    @staticmethod
    def helper(data: list[list[str]]) -> tuple[int, int]:
        illegal_score = Day10.IllegalScore()
        autocomplete_score = Day10.AutocompleteScore()
        for line in data:
            stack = []
            for c in line:
                if c not in Day10.char_map:
                    stack.append(c)
                else:
                    if stack[-1] != Day10.char_map[c]:
                        illegal_score[c] += 1
                        break
                    else:
                        stack.pop()
            else:
                autocomplete_score.append(stack)
        return illegal_score.calculate(), autocomplete_score.calculate()

    class IllegalScore(dict):
        map = {')': 3, ']': 57, '}': 1197, '>': 25137}
        def __init__(self) -> None:
            super().__init__({k: 0 for k in self.map})

        def calculate(self) -> int:
            return sum(self[k] * m for k, m in self.map.items())

    class AutocompleteScore(list):
        map = {'(': 1, '[': 2, '{': 3, '<': 4}
        def append(self, stack: Any) -> None:
            score = reduce(lambda score, c: (score * 5) + self.map[c], stack[::-1], 0)
            super().append(score)
        def calculate(self) -> int:
            return sorted(self)[len(self)//2]

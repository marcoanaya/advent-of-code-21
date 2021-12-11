from typing import Callable, FrozenSet
from .abstract_day import AbstractDay
from ..util.file_util import FileUtil

Input = list[tuple[list[str], list[str]]]
IsDigit = Callable[[FrozenSet], bool]
IsDigitMaker = Callable[[IsDigit, IsDigit], IsDigit]

class Day8(AbstractDay):
    @staticmethod
    def input(file_name: str) -> Input:
        digits = [d.strip().split() for d in FileUtil.file_to_list(file_name, delim='\n')]
        return [(d[:10], d[11:]) for d in digits]

    @staticmethod
    def one(data: Input) -> int:
        count = 0
        for _, right in data:
            count += sum(1 for s in right if len(s) in [2,3,4,7])
        return count

    @staticmethod
    def two(data: Input) -> int:
        count = 0
        for left, right in data:
            options = sorted((frozenset(c) for c in left), key=len)
            d: list[FrozenSet] = [frozenset()] * 10
            d[1], d[7], d[4], *unknown, d[8] = options

            def find_num(l: int, cond: IsDigit) -> FrozenSet:
                return next(v for v in unknown if cond(v) and len(v) == l)

            neither: IsDigitMaker = lambda f, g: lambda v: not f(v) and not g(v)
            former: IsDigitMaker = lambda f, g: lambda v: f(v) and not g(v)
            d[9] = find_num(6, is_9 := lambda v: d[4] < v)
            d[3] = find_num(5, is_3 := lambda v: d[1] < v)
            d[5] = find_num(5, is_5 := former(lambda v: v < d[9], is_3))
            d[6] = find_num(6, is_6 := former(lambda v: d[5] < v, is_9))
            d[0] = find_num(6, neither(is_9, is_6))
            d[2] = find_num(5, neither(is_3, is_5))
            d_map = {v: i for i, v in enumerate(d)}
            count +=  int(''.join(str(d_map[frozenset(r)])   for r in right))
        return count

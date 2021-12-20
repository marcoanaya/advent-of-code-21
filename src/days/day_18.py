import math
from copy import deepcopy
from itertools import permutations
from typing import Any, Callable, Deque, Optional, Union
from .abstract_day import AbstractDay
from ..util.file_util import FileUtil

class Day18(AbstractDay):
    @classmethod
    def input(cls, file_name: str) -> Any:
        return FileUtil.file_to_list(file_name, f=lambda x: SnailNumber.from_list(eval(x)))

    @classmethod
    def one(cls, snail_numbers: list['SnailNumber']) -> int:
        first, *rest = snail_numbers
        return int(sum(rest, first))

    @classmethod
    def two(cls, snail_numbers: list['SnailNumber']) -> int:
        return max(int(a + b) for a, b in permutations(snail_numbers, 2))

class SnailNumber:
    def __init__(self, x: Union[int, list['SnailNumber']]) -> None:
        if isinstance(x, int):
            self.x = x
        else:
            self.left, self.right = x

    @staticmethod
    def from_list(x: list[list | int] | int) -> 'SnailNumber':
        return SnailNumber(x) if isinstance(x, int) else SnailNumber(list(map(SnailNumber.from_list, x)))

    def __add__(self, other: 'SnailNumber') -> 'SnailNumber':
        if hasattr(self, 'x') and hasattr(other, 'x'):
            self.x += other.x
            return self
        return Reducer.reduce(SnailNumber([self, other]))

    def __int__(self) -> int:
        if hasattr(self, 'x'):
            return self.x
        return (3 * int(self.left)) + (2 * int(self.right))

    def __str__(self) -> str:
        def f(a: 'SnailNumber', i:int=1) -> str:
            if hasattr(a, 'x'):
                return f"<{a.x}>"
            return f"{i}[{f(a.left, i+1)},{f(a.right, i+1)}]"
        return f(self)
    __repr__ = __str__

    def split(self) -> 'SnailNumber':
        left, right = math.floor(self.x / 2), math.ceil(self.x / 2)
        return SnailNumber([SnailNumber(left), SnailNumber(right)])

    def explode(self, left: Optional['SnailNumber'], right: Optional['SnailNumber']) -> 'SnailNumber':
        if left:
            left += self.left
        if right:
            right += self.right
        return SnailNumber(0)

    def is_simple_pair(self) -> bool:
        return hasattr(self, 'left') and hasattr(self.left, 'x') and hasattr(self.right, 'x')

class Reducer:
    stack = Deque[tuple[SnailNumber, str, int]]()
    left: Optional['SnailNumber'] = None
    @staticmethod
    def reduce(snum: 'SnailNumber') -> 'SnailNumber':
        snum = deepcopy(snum)
        while True:
            if not (Reducer.dfs(snum, Reducer.explode) or Reducer.dfs(snum, Reducer.split)):
                break
        return snum

    @staticmethod
    def explode(curr: 'SnailNumber', depth: int) -> Optional['SnailNumber']:
        return curr.explode(Reducer.left, Reducer.get_right()) if depth > 4 and curr.is_simple_pair() else None

    @staticmethod
    def split(curr: 'SnailNumber', _: int) -> Optional['SnailNumber']:
        return curr.split() if hasattr(curr, 'x') and int(curr) >= 10 else None

    @staticmethod
    def get_right() -> Optional['SnailNumber']:
        while Reducer.stack:
            tmp_p, tmp_d, depth = Reducer.stack.pop()
            tmp = getattr(tmp_p, tmp_d)
            if hasattr(tmp, 'x'):
                return tmp
            Reducer.stack.extend([(tmp, 'right', depth + 1), (tmp, 'left', depth + 1)])
        return None

    @staticmethod
    def dfs(snum: 'SnailNumber', f: Callable) -> bool:
        Reducer.left = None
        Reducer.stack.clear()
        Reducer.stack.extend([(snum, 'right', 2), (snum, 'left', 2)])
        while Reducer.stack:
            parent, dirr, depth = Reducer.stack.pop()
            curr: 'SnailNumber' = getattr(parent, dirr)
            if new_curr := f(curr, depth):
                setattr(parent, dirr, new_curr)
                return True
            if hasattr(curr, 'x'):
                Reducer.left = curr
            else:
                Reducer.stack.extend([(curr, 'right', depth + 1), (curr, 'left', depth + 1)])
        return False

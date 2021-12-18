import math
from typing import Any
from dataclasses import dataclass, field
from .abstract_day import AbstractDay
from ..util.file_util import FileUtil
from ..util.misc import Index


class Day16(AbstractDay):
    @classmethod
    def input(cls, file_name: str) -> str:
        b = bin(int(FileUtil.file_to_list(file_name)[0], 16))[2:]
        return b.zfill(4 * math.ceil(len(b)/4))

    @classmethod
    def one(cls, text: str) -> int:
        return cls.parse(text).version_sum()

    @classmethod
    def two(cls, text: str) -> int:
        return cls.parse(text).eval()

    @classmethod
    def parse(cls, text: str) -> 'Day16.Exp':
        def dfs(i: Index) -> 'Day16.Exp':
            v = int(text[i.get():i.inc(3)], 2)
            t = int(text[i.get():i.inc(3)], 2)
            if t == 4:
                b = ''
                while text[i.get()] != '0':
                    b += text[i.inc(1):i.inc(4)]
                b += text[i.inc(1):i.inc(4)]
                return Day16.Literal(v, t, b=int(b, 2))
            else:
                exp = Day16.Op(v, t)
                if text[i.get()] == '0':
                    end = int(text[i.inc(1):i.inc(15)], 2) + i.get()
                    while i.get() < end:
                        exp.add_child(dfs(i))
                else:
                    n = int(text[i.inc(1):i.inc(11)], 2)
                    for _ in range(n):
                        exp.add_child(dfs(i))
                return exp
        return dfs(Index())

    @dataclass
    class Exp:
        v: int
        t: int
        children: list['Day16.Exp']=field(default_factory=list)
        def version_sum(self) -> int:
            return self.v + sum(c.version_sum() for c in self.children)
        def eval(self) -> int:
            pass

    @dataclass
    class Op(Exp):
        def add_child(self, exp: 'Day16.Exp') -> None:
            self.children.append(exp)
        def eval(self) -> int:
            f: Any = [
                sum,
                math.prod,
                min,
                max,
                None,
                lambda cs: int(cs[0] > cs[1]),
                lambda cs: int(cs[0] < cs[1]),
                lambda cs: int(cs[0] == cs[1])
            ][self.t]
            return f([c.eval() for c in self.children])

    @dataclass
    class Literal(Exp):
        b: int=0
        def eval(self) -> int:
            return self.b

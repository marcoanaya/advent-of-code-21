from typing import Any, Counter
from .abstract_day import AbstractDay
from ..util.file_util import FileUtil

class Day14(AbstractDay):
    @classmethod
    def input(cls, file_name: str) -> Any:
        lines = FileUtil.get_file_lines(file_name, delim='\n')
        template = lines[0]
        insertion_rules = [c.split(' -> ') for c in lines[2:]]
        return Day14.Polymer(template, insertion_rules)

    @classmethod
    def one(cls, polymer: 'Day14.Polymer') -> int:
        polymer.step(10)
        return polymer.most_sub_least()

    @classmethod
    def two(cls, polymer: 'Day14.Polymer') -> int:
        polymer.step(40)
        return polymer.most_sub_least()

    class Polymer:
        def __init__(self, template: str, insertion_rules: list[list[str]]) -> None:
            self.insertion_rules = {k: v for k, v in insertion_rules}
            self.count = Counter(template)
            self.template: Counter[str] = Counter()
            for i in range(1, len(template)):
                self.template[template[i-1:i+1]] += 1

        def step(self, n: int) -> None:
            for _ in range(n):
                t: Counter[str] = Counter()
                for k, v in self.template.items():
                    if k in self.insertion_rules:
                        new = self.insertion_rules[k]
                        t[k[0]+new] += v
                        t[new+k[1]] += v
                        self.count[new] += v
                    else:
                        t[k] += v
                self.template = t

        def most_sub_least(self) -> int:
            (_, most), *_, (_, least) = Counter(self.count).most_common()
            return most - least

        def __str__(self) -> str:
            return str((self.template, self.insertion_rules))

from typing import Any, DefaultDict
from itertools import product
from .abstract_day import AbstractDay
from ..util.file_util import FileUtil


class Day21(AbstractDay):
    @classmethod
    def input(cls, file_name: str) -> Any:
        [*_, p1], [*_, p2] = FileUtil.file_to_list(file_name, f=list)
        return Player('0', int(p1)), Player('1', int(p2))

    @classmethod
    def one(cls, data: Any) -> int:
        p_turn, p_other = data
        die, rolls = 1, 0
        while True:
            p_turn = p_turn.move(3 + (die * 3))
            die = ((die + 2) % 100) + 1
            rolls += 3
            if p_turn.score >= 1000:
                return p_other.score * rolls
            p_turn, p_other = p_other, p_turn

    @classmethod
    def two(cls, data: Any) -> int:
        sum_dist = DefaultDict[int, int](int)
        for roll in product([1, 2, 3], repeat=3):
            sum_dist[sum(roll)] += 1

        cache: dict[tuple, tuple] = {}
        def func(p_turn: 'Player', p_other: Player) -> DefaultDict[str, int]:
            if p_other.score >= 21:
                return DefaultDict(int, {p_other.name: 1})
            key = tuple(map(Player.to_tuple, [p_turn, p_other]))
            if key in cache:
                return DefaultDict(int, cache[key])

            counts = DefaultDict[str, int](int)
            for roll, dist in sum_dist.items():
                c = func(p_other, p_turn.move(roll))
                counts['0'] += c['0'] * dist
                counts['1'] += c['1'] * dist
            cache[key] = tuple(sorted(counts.items()))
            return counts
        return max(func(*data).values())

class Player:
    def __init__(self, name: str, space: int) -> None:
        self.name = name
        self.space = space
        self.score = 0

    def move(self, spots: int) -> 'Player':
        new = Player(self.name, (((self.space + spots)-1) % 10) + 1)
        new.score = self.score + new.space
        return new

    def to_tuple(self) -> tuple[str, int, int]:
        return (self.name, self.space, self.score)

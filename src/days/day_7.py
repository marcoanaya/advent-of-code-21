from typing import Callable
from .abstract_day import AbstractDay
from ..util.file_util import FileUtil

FuelCost = Callable[[int, int], int]

class Day7(AbstractDay):
    fuel_cost_one: FuelCost = lambda x, y: abs(x - y)
    fuel_cost_two: FuelCost = lambda x, y: sum(i for i in range(1, abs(x - y) + 1))

    @classmethod
    def input(cls, file_name: str) -> list[int]:
        return FileUtil.file_to_list(file_name, f=int, delim=',')

    @classmethod
    def one(cls, crabs: list[int]) -> int:
        median = sorted(crabs)[len(crabs)//2]
        return sum(cls.fuel_cost_one(median, d) for d in crabs)

    @classmethod
    def two(cls, crabs: list[int]) -> int:
        mean = round(sum(crabs)/len(crabs))
        return sum(cls.fuel_cost_two(mean, d) for d in crabs)

    @classmethod
    def one_brute(cls, data: list[int]) -> int:
        return cls.find_fuel(data, cls.fuel_cost_one)

    @classmethod
    def two_brute(cls, data: list[int]) -> int:
        return cls.find_fuel(data, cls.fuel_cost_two)

    @classmethod
    def find_fuel(cls, data: list[int], fuel_cost: FuelCost) -> int:
        min_val = float('inf')
        for d in range(min(data), max(data) +1):
            val = sum(fuel_cost(d, dd) for dd in data)
            min_val = min(min_val, val)
        return int(min_val)

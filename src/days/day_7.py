from typing import Callable
from .abstract_day import AbstractDay
from ..util.file_util import FileUtil

FuelCost = Callable[[int, int], int]

class Day7(AbstractDay):
    fuel_cost_one: FuelCost = lambda x, y: abs(x - y)
    fuel_cost_two: FuelCost = lambda x, y: sum(i for i in range(1, abs(x - y) + 1))

    @staticmethod
    def input(file_name: str) -> list[int]:
        return FileUtil.file_to_list(file_name, f=int, delim=',')

    @staticmethod
    def one(data: list[int]) -> int:
        median = sorted(data)[len(data)//2]
        return sum(Day7.fuel_cost_one(median, d) for d in data)

    @staticmethod
    def two(data: list[int]) -> int:
        mean = round(sum(data)/len(data))
        return sum(Day7.fuel_cost_two(mean, d) for d in data)

    @staticmethod
    def one_brute(data: list[int]) -> int:
        return Day7.find_fuel(data, Day7.fuel_cost_one)

    @staticmethod
    def two_brute(data: list[int]) -> int:
        return Day7.find_fuel(data, Day7.fuel_cost_two)

    @staticmethod
    def find_fuel(data: list[int], fuel_cost: FuelCost) -> int:
        min_val = float('inf')
        for d in range(min(data), max(data) +1):
            val = sum(fuel_cost(d, dd) for dd in data)
            min_val = min(min_val, val)
        return int(min_val)

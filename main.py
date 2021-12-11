from glob import glob
import re
import sys
from copy import deepcopy
from src.util.day_util import DayUtil

days = DayUtil.get_days()

if requested := list(map(int, sys.argv[1:])):
    days = [c for c in days if c.get_number() in requested]

for Day in days:
    print(Day.__name__)
    n = Day.get_number()
    for i, file_name in enumerate(sorted((f for f in glob(f"./src/inputs/input_{n}_*.txt")), reverse=True), 1):
        data = Day.input(file_name)
        nums_in_file = list(map(int, re.findall(r'\d+', file_name)))
        expecteds = nums_in_file[1:]
        if expecteds:
            print(f"  test {i}")
            for j, (expected, sol) in enumerate(zip(expecteds, [Day.one, Day.two]), 1):
                actual = sol(deepcopy(data))
                if expected !=  actual:
                    print(f"    {n}.{j} - Expected {expected}, got {actual}.")
                    exit(0)
                print(f"    {n}.{j} - {actual}")
    data = Day.input(f"./src/inputs/input_{n}.txt")
    print("  solution")
    print(f"    {n}.1 - {Day.one(deepcopy(data))}")
    print(f"    {n}.2 - {Day.two(deepcopy(data))}")

from glob import glob
import re
import sys
from src.util.day_util import DayUtil

days = DayUtil.get_days()

if requested := list(map(int, sys.argv[1:])):
    days = [c for c in days if c.get_number() in requested]

for Day in days:
    print(Day.__name__)
    n = Day.get_number()
    for i, file_name in enumerate(sorted((f for f in glob(f"./src/inputs/input_{n}*.txt")), reverse=True), 1):
        data = Day.input(file_name)
        nums_in_file = list(map(int, re.findall(r'\d+', file_name)))
        if len(nums_in_file) > 1:
            _, expected_one, expected_two = nums_in_file
            print(f"  test {i}")
            actual_one = Day.one(data)
            if expected_one !=  actual_one:
                raise Exception(f"Expected {expected_one}, got {actual_one}.")
            print(f"    {n}.1 - {actual_one}")
            actual_two = Day.two(data)
            if expected_two !=  actual_two:
                raise Exception(f"Expected {expected_two}, got {actual_two}.")
            print(f"    {n}.2 - {actual_two}")
        else:
            print(f"  solution")
            print(f"    {n}.1 - {Day.one(data)}")
            print(f"    {n}.2 - {Day.two(data)}")

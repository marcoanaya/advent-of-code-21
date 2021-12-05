import sys
from src.util.day_util import DayUtil

day_classes = DayUtil.get_day_classes()

if requested := sys.argv[1:]:
    day_classes = [c for c in day_classes if c.get_number() in requested]

for Day in day_classes:
    print(Day.__name__)
    n = Day.get_number()
    print(f"  {n}.1 - {Day.one()}")
    print(f"  {n}.2 - {Day.two()}")

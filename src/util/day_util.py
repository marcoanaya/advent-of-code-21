import sys
import importlib
import glob
import re
from typing import Type
from src.days.abstract_day import AbstractDay
import src.days


for file in glob.glob("./src/days/day*.py"):
    match = re.search('./src/days/(.+?).py', file)
    if match:
        importlib.import_module(f"src.days.{match.group(1)}")

class DayUtil:
    @staticmethod
    def new_day(n: int) -> None:
        with open(f"./src/days/day_{n}.py", "w", encoding="utf-8") as f:
            f.write(f"""from .abstract_day import AbstractDay
from ..util.file_util import FileUtil

class Day{n}(AbstractDay):
    @staticmethod
    def input() -> list[str]:
        return FileUtil.file_to_list(Day{n}.get_file_name())

    @staticmethod
    def one() -> int:
        pass

    @staticmethod
    def two() -> int:
        pass
""")

    @staticmethod
    def get_day_classes() -> list[Type[AbstractDay]]:
        day_modules = [(name, mod) for name, mod in src.days.__dict__.items() if name.startswith('day_')]
        day_modules.sort(key=lambda x: int(x[0].strip('day_')))
        day_modules = list(map(lambda x: x[1], day_modules))
        get_cls = lambda mod: next(cls for name, cls in mod.__dict__.items() if name.startswith('Day'))
        return list(map(get_cls, day_modules))


if __name__ == '__main__':
    num: int = int(sys.argv[1])
    DayUtil.new_day(num)

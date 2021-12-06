from abc import ABC, abstractmethod
from typing import Any


class AbstractDay(ABC):
    @classmethod
    def get_number(cls) -> int:
        return int(cls.__name__.strip("Day"))

    @staticmethod
    @abstractmethod
    def input(file_name: str) -> Any:
        pass

    @staticmethod
    @abstractmethod
    def one(data: Any) -> int:
        pass

    @staticmethod
    @abstractmethod
    def two(data: Any) -> int:
        pass

from abc import ABC, abstractmethod


class AbstractDay(ABC):
    @classmethod
    def get_number(cls) -> int:
        return int(cls.__name__.strip("Day"))

    @classmethod
    def get_file_name(cls, file_suffix: str="") -> str:
        return f"./src/inputs/input_{cls.get_number()}{file_suffix}.txt"
    
    @staticmethod
    @abstractmethod
    def one() -> int:
        pass

    @staticmethod
    @abstractmethod
    def two() -> int:
        pass

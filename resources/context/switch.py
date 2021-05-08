from abc import ABC
from typing import Any


class Switch(ABC):

    @classmethod
    def case(cls, attribute: str) -> Any:
        if hasattr(cls, attribute):
            method = getattr(cls, str(attribute))
            return method()
        raise AttributeError

    @classmethod
    def available_cases(cls) -> tuple:
        cases = [func for func in dir(cls) if callable(getattr(cls, func)) and not func.startswith("__")]
        cases.remove("case")
        cases.remove("available_cases")
        return tuple(cases)

from abc import ABC
from typing import Any


class Switch(ABC):

    @classmethod
    def case(cls, attribute: str, *args, **kwargs) -> Any:
        if hasattr(cls, attribute):
            method = getattr(cls, str(attribute))
            if len(args) > 0 and len(kwargs) > 0:
                return method(args, kwargs)
            elif len(args) > 0 and len(kwargs) == 0:
                return method(args)
            elif len(args) == 0 and len(kwargs) > 0:
                return method(kwargs)
            else:
                return method()
        raise AttributeError

    @staticmethod
    def available_cases():
        available_cases = [func for func in dir(Switch) if callable(getattr(Switch, func)) and not (
                    func.startswith("__") or (func is "case" or "available_cases"))]
        return tuple(available_cases)

from resources.concrete.handler.argument_validator import SysValidator
from resources.context.handler import ArgumentHandler
from resources.other.enough import have_enough_arguments


class SysArgumentHandler(ArgumentHandler):
    def __init__(self, debug: bool = False) -> None:
        super().__init__(debug)
        self._sys_validator = SysValidator(self._debug)

    def handle_arguments(self, *args) -> None:
        if have_enough_arguments(args):
            metric_name: str = args[1]
            metric_values: tuple = args[2::]
            self._sys_validator.handle_arguments(metric_name, metric_values)
        else:
            print("Not enough arguments.")

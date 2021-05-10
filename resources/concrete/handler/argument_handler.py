import resources.concrete.status.mode as app_status
from resources.concrete.handler.argument_validator import SysArgumentValidator
from resources.context.handler import ArgumentHandler
from resources.other.enough import have_enough_arguments


class SysArgumentHandler(ArgumentHandler):
    def __init__(self, debug: bool) -> None:
        app_status.debug = debug
        self._sys_validator = SysArgumentValidator()

    def handle_arguments(self, *args) -> None:
        if have_enough_arguments(args, threshold=3):
            metric_name: str = args[1].lower()
            metric_values: tuple = args[2::]
            self._sys_validator.handle_arguments(metric_name, metric_values)
        else:
            print("\nNot enough arguments. Choose a metric and at least one score.")

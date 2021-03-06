import resources.concrete.status.mode as app_status
from resources.concrete.validator.argument_validator import SysArgumentValidator
from resources.context.handler import ArgumentHandler
from resources.other.enough import have_enough_arguments


class SysArgumentHandler(ArgumentHandler):
    def __init__(self, debug: bool) -> None:
        app_status.debug = debug
        self._sys_validator = SysArgumentValidator()

    def handle_arguments(self, *args) -> None:
        if have_enough_arguments(args, threshold=3):
            metric_name: str = args[1].lower()
            metric_value: tuple = args[2::]
            kwargs: dict = {"metric_name": metric_name, "metric_value": metric_value}
            self._sys_validator.validate_arguments(**kwargs)
        else:
            print("\nNot enough arguments. Choose a metric and at least one score.")

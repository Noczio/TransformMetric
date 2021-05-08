from resources.concrete.system.sys_validator import SysValidator
from resources.context.sys_data import SysData
from resources.other.enough import have_enough_arguments


class SysParameterValidator(SysData):

    def __init__(self, debug: bool = False) -> None:
        self._metric_validator = SysValidator(debug)

    def parameters_are_valid(self, *args) -> bool:
        if have_enough_arguments(args):
            metric_name: str = args[1]
            metric_values: tuple = args[2::]
            arguments_are_valid: bool = self._metric_validator.is_valid(metric_name, metric_values)
            return arguments_are_valid
        return False

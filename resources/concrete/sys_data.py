from resources.context.sys_data import SysData
from resources.concrete.is_data import IsDataValid, IsNumeric, IsString
from resources.concrete.funcs.range import is_in_range


class SysParameterValidator(SysData):

    def parameters_are_valid(self, *args) -> bool:
        if len(args) >= 2:
            first_value: str = args[0]
            other_value: tuple = args[1::]

            is_string: bool = IsDataValid.is_data(IsString(), first_value)
            is_valid_metric: bool = True if is_string and first_value in self.metrics else False
            parameters_are_valid: list = [is_valid_metric]

            for value in other_value:
                is_float: bool = IsDataValid.is_data(IsNumeric(), value)
                is_valid: bool = True if is_float and is_in_range(float(value)) else False
                parameters_are_valid.append(is_valid)

            return all(parameters_are_valid)
        return False

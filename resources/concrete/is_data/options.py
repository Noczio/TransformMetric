from resources.context.switch import Switch
from resources.concrete.is_data.is_string import IsString
from resources.concrete.is_data.is_numeric import IsNumeric
from resources.context.is_data import IsData


class IsDataPossibilities(Switch):

    @staticmethod
    def string() -> IsData:
        return IsString()

    @staticmethod
    def number() -> IsData:
        return IsNumeric()

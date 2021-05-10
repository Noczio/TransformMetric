from resources.concrete.is_data.options import IsDataPossibilities
from resources.context.is_data import IsData


class IsDataCreator:
    @staticmethod
    def create_data_validator(validation_case: str) -> IsData:
        validator: IsData = IsDataPossibilities.case(validation_case)
        return validator

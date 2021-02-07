from dataclasses import dataclass


@dataclass(frozen=True)
class Alcohol():
    __create_key = object()

    value: str
    create_key: object

    def __post_init__(self):
        class_name = self.__class__.__name__
        assert self.create_key == Alcohol.__create_key, (
            f"{class_name} instance must be created by " +
            f"using the '{class_name}.create' method.")

    @classmethod
    def create(cls, value: str) -> "Acohol":
        if not isinstance(value, str):
            raise ValueError("'value' must be a string value")

        value = value.strip()

        if not (1 < len(value) < 5):
            raise ValueError(
                "'Alcohol value must be a string with at least 1 and a maximum of 5 characters")

        return Alcohol(value=value, create_key=cls.__create_key)

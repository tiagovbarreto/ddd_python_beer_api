from dataclasses import dataclass


@dataclass(frozen=True)
class Name():
    __create_key = object()

    value: str
    create_key: object

    def __post_init__(self):
        class_name = self.__class__.__name__
        assert self.create_key == Name.__create_key, (
            f"{class_name} instance must be created by " +
            f"using the '{class_name}.create' method.")

    @classmethod
    def create(cls, value: str) -> "Name":
        if not isinstance(value, str):
            raise ValueError("'value' must be a string value")

        value = value.strip()

        if not (3 < len(value) <= 50):
            raise ValueError(
                "'value must be a string with at least 3 and a maximum of 50 characters")

        return Name(value=value, create_key=cls.__create_key)

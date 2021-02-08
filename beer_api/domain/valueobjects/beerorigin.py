from dataclasses import dataclass


@dataclass(frozen=True)
class BeerOrigin():
    __create_key = object()

    value: str
    create_key: object

    def __post_init__(self):
        class_name = self.__class__.__name__
        assert self.create_key == BeerOrigin.__create_key, (
            f"{class_name} instance must be created by " +
            f"using the '{class_name}.create' method.")

    @classmethod
    def create(cls, value: str) -> "BeerOrigin":
        if not isinstance(value, str):
            raise ValueError("'value' must be a string value")

        value = value.strip()

        if not (5 < len(value) <= 30):
            raise ValueError(
                "'value must be a string with at least 5 and a maximum of 30 characters")

        return BeerOrigin(value=value, create_key=cls.__create_key)

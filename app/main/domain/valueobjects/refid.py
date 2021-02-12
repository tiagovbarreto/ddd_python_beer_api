from dataclasses import dataclass
import uuid


@dataclass(frozen=True)
class RefId:
    __create_key = object()

    value: uuid.UUID
    create_key: object

    def __post_init__(self):
        class_name = self.__class__.__name__
        assert self.create_key == RefId.__create_key, (
            f"{class_name} instance must be created by "
            + f"using the '{class_name}.create' method."
        )

    @classmethod
    def create(cls, value: uuid.UUID):
        if not isinstance(value, uuid.UUID):
            raise ValueError("'value' must be a valid uuid.UUID v4 instance.")

        return RefId(value, create_key=cls.__create_key)

    @classmethod
    def create_from_uuid_str(cls, value: str):
        try:
            uuid_object = uuid.UUID(value, version=4)
            return cls.create(uuid_object)
        except Exception as ex:
            raise ValueError(ex)

    @classmethod
    def new(cls):
        return RefId(uuid.uuid4(), create_key=cls.__create_key)

    def __str__(self):
        return self.value.hex

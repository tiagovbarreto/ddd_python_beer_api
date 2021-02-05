from uuid import uuid4


def get_repr(obj):
    attributes = ("%s=%r" % (k, v) for k, v in obj.__dict__.items())
    return "<%s(%s)." % (obj.__class__.__name__, ', '.join(attributes))


class Beer:
    def __init__(self, name: str, kind: str, origin: str, alcohol: str) -> None:
        self.name = name
        self.kind = kind
        self.origin = origin
        self.alcohol = alcohol
        self.id = uuid4()
        self.shareholders = []

    def __repr__(self) -> str:
        return get_repr(self)

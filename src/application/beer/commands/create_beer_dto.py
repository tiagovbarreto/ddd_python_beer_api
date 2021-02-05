from dataclasses import dataclass


@dataclass
class CreateBeerDTO:
    name: str
    kind: str
    origin: str
    alcoholic: str

    def to(self, request):
        pass

    def teste(self, request) -> CreateBeerDTO:

from dataclasses import dataclass


@dataclass(frozen=True)
class CreateBeerDTO:
    name: str

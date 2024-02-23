from dataclasses import dataclass


@dataclass
class Score:
    home: int
    visitor: int

    def __str__(self):
        return f"{self.home} - {self.visitor}"

    @property
    def played(self) -> bool:
        return self.home is not None and self.visitor is not None

    def __eq__(self, other):
        if isinstance(other, Score):
            return self.home == other.home and self.visitor == other.visitor
        return False

    def __hash__(self):
        return hash((self.home, self.visitor))

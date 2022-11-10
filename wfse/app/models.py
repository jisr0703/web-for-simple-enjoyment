from enum import Enum


class Feeling(int, Enum):
    Happiness: int = 1
    Sadness: int = 2
    Boring: int = 3


class Reaction(int, Enum):
    Like: int = 1
    Hate: int = 2

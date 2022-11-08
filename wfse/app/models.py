from enum import Enum


class Feelings(int, Enum):
    Happiness: int = 1
    Sadness: int = 2
    Boring: int = 3


class Reactions(int, Enum):
    Like: int = 1
    Hate: int = 2

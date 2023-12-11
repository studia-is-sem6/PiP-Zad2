from typing import List, Tuple
from abc import ABC, abstractmethod
from my_decorators.repr_decorator import inject_generic_repr


@inject_generic_repr
class Entity(ABC):
    # pylint: disable=consider-using-alias
    def __init__(self, name: str, position: List[float], movement_distance: float):
        self.name: str = name
        self.position: List[float] = position
        self.movement_distance: float = movement_distance

    @abstractmethod
    def move(self) -> Tuple[float]:
        # Moves entity and returns it's new position
        # TODO: implement entity move
        pass

    def get_position(self) -> tuple[float]:
        # Returns entity position in a tuple format
        return tuple(self.position)

    def set_position(self, x: float, y: float) -> Tuple[float]:
        # Sets entity position
        self.position = [x, y]
        return tuple(self.position)

    def __str__(self):
        return f"{self.name} is at position {self.position}"

    def verbose_print(self) -> str:
        return f"{self.name} is at position {self.position} and it's movement distance is {self.movement_distance}"


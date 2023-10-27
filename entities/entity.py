from typing import List, Tuple
from abc import ABC, abstractmethod
from my_decorators.repr_decorator import inject_generic_repr


@inject_generic_repr
class Entity(ABC):

    def __init__(self, name, position, movement_distance):
        self.name: str = name
        self.position: List[float, float] = position
        self.movement_distance: float = movement_distance

    @abstractmethod
    def move(self) -> Tuple[float, float]:
        # Moves entity and returns it's new position
        # TODO: implement entity move
        pass

    def get_position(self) -> Tuple[float, float]:
        # Returns entity position in a tuple format
        # TODO: implement get_position method of entity
        pass

    def set_position(self, x: float, y: float) -> None:
        # Sets entity position
        # TODO: implement set_position method of entity
        pass

    def __str__(self):
        return f"{self.name} is at position {self.position}"

    def __repr__(self):
        return ""


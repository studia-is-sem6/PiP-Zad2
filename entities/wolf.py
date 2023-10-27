from typing import Tuple, List

from entities.entity import Entity


class Wolf(Entity):
    def __init__(self, name: str, position: List[float], movement_distance: float):
        super().__init__(name, position, movement_distance)

    def move(self) -> Tuple[float, float]:
        # TODO: implement move method for Wolf
        pass

    def attack(self) -> None:
        # TODO: implement attack method for Wolf
        pass
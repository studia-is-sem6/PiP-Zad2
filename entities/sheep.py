from typing import List, Tuple
from entities.entity import Entity


class Sheep(Entity):
    # pylint: disable=consider-using-alias
    def __init__(self, name: str, position: List[float], movement_distance: float):
        super().__init__(name, position, movement_distance)

    def move(self) -> Tuple[float, float]:
        # TODO: implement move method for Sheep
        pass


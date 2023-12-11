from typing import List, Tuple
import random
from entities.entity import Entity


class Sheep(Entity):
    # pylint: disable=consider-using-alias
    def __init__(self, name: str, position: List[float], movement_distance: float):
        super().__init__(name, position, movement_distance)

    def move(self) -> Tuple[float]:
        # TODO: implement move method for Sheep
        direction = random.choice(['north', 'south', 'east', 'west'])

        match direction:
            case 'north':
                self.position[0] += self.movement_distance
            case 'south':
                self.position[0] -= self.movement_distance
            case 'east':
                self.position[1] += self.movement_distance
            case 'west':
                self.position[1] -= self.movement_distance

        return tuple(self.position)
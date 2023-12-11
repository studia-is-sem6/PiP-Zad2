from typing import List, Tuple
import random
import entities


class Sheep(entities.Entity):
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

        self.position = [round(self.position[0], 3), round(self.position[1], 3)]
        return tuple(self.position)

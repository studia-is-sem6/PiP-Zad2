import random
from typing import List
import entities


class Herd:
    # pylint: disable=consider-using-alias
    def __init__(self, number_of_individuals: int, initial_pos_limit: float, movement_distance_of_herd: float):
        self.number_of_individuals = number_of_individuals
        self.initial_pos_limit = initial_pos_limit
        self.movement_distance_of_herd = movement_distance_of_herd
        self.herd: List[entities.Sheep] = []
        for i in range(number_of_individuals):
            self.herd.append(entities.Sheep(f"Sheep {i}",
                                            [round(random.uniform(-1*self.initial_pos_limit, self.initial_pos_limit), 3),
                                                     round(random.uniform(-1*self.initial_pos_limit, self.initial_pos_limit), 3)],
                                            self.movement_distance_of_herd))

    def __iter__(self):
        for sheep in self.herd:
            yield sheep

    def move_herd(self):
        for sheep in self.herd:
            sheep.move()

    def get_all_herd_pos(self) -> List[List[float]]:
        positions = []
        for sheep in self:
            positions.append(sheep.position)
        return positions

    def get_all_herd_pos_with_nulls(self) -> List[List[float]]:
        positions = []
        for sheep in self:
            positions.append(sheep.position)
        for _ in range(self.number_of_individuals - len(positions)):
            positions.append(None)

        return positions

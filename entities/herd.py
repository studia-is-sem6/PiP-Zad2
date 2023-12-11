import random
from typing import List
from entities import Sheep


class Herd:
    # pylint: disable=consider-using-alias
    def __init__(self, number_of_individuals: int, initial_pos_limit: float, movement_distance_of_herd: float):
        self.number_of_individuals = number_of_individuals
        self.initial_pos_limit = initial_pos_limit
        self.movement_distance_of_herd = movement_distance_of_herd
        self.herd: List[Sheep] = []
        for i in range(number_of_individuals):
            self.herd.append(Sheep(f"Sheep {i}",
                                   [round(random.uniform(-1*self.initial_pos_limit, self.initial_pos_limit), 3),
                                            round(random.uniform(-1*self.initial_pos_limit, self.initial_pos_limit), 3)],
                                   self.movement_distance_of_herd))

    def __iter__(self):
        for sheep in self.herd:
            yield sheep

    def move_herd(self):
        for sheep in self.herd:
            sheep.move()

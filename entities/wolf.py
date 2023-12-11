from typing import Tuple, List
# from entities import Entity, Sheep
import entities

# import importlib
#
# other_herd = importlib.import_module("entities", "herd")

class Wolf(entities.Entity):
    # pylint: disable=consider-using-alias
    def __init__(self, name: str, position: List[float], movement_distance: float):
        super().__init__(name, position, movement_distance)
        self.herd: entities.Herd = None
        self.target: entities.Sheep = None

    def move(self) -> Tuple[float]:
        # TODO: implement move method for Wolf
        last_dist = self.calculate_distance(self.herd.herd[0].position, self.position)
        for sheep in self.herd:
            new_dist = self.calculate_distance(sheep.position, self.position)
            print(f"Owca {sheep}, jest w odległosci {new_dist} od wilka")
            if new_dist < last_dist:
                last_dist = new_dist
                self.target = sheep

        print(f"Najbliższa owca {self.target}, w odległości {last_dist}")
        return tuple(self.position)

        # if last_dist <= self.movement_distance:


    def attack(self) -> None:
        # TODO: implement attack method for Wolf
        pass

    def calculate_distance(self, point1: List[float], point2: List[float]) -> float:
        x1, y1 = point1
        x2, y2 = point2

        return ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
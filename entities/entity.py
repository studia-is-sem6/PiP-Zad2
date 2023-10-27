from typing import List, Tuple


class Entity:

    def __init__(self, position, name, movement_distance):
        self.position: List[float, float] = position
        self.name: str = name
        self.movement_distance: float = movement_distance

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

    
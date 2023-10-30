from entities.sheep import Sheep
from entities.wolf import Wolf


def test_sheep_class():
    sheep = Sheep("Dolly", [37, -21], 0.5)

    assert sheep.name == "Dolly"
    assert sheep.get_position() == (37, -21)
    assert sheep.movement_distance == 0.5


def test_wolf_class():
    wolf = Wolf("Ben", [-12, 34], 2)

    assert wolf.name == "Ben"
    assert wolf.get_position() == (-12, 34)
    assert wolf.movement_distance == 2

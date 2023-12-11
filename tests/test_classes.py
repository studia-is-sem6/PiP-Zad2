from entities import Sheep
from entities import Wolf
from entities import Herd


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

def test_herd_class():
    herd = Herd(15, 10,0.5)

    assert herd.movement_distance_of_herd == 0.5
    assert herd.initial_pos_limit == 10
    assert herd.number_of_individuals == 15

    herd.herd.pop()

    assert len(herd.herd) == 14
    assert herd.herd[0].name == "Sheep 0"
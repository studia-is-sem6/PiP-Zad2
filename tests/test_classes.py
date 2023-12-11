from entities import Sheep
from entities import Wolf
from entities import Herd


def test_sheep_class():
    sheep = Sheep("Dolly", [37, -21], 0.5)

    assert sheep.name == "Dolly"
    assert sheep.get_position() == (37, -21)
    assert sheep.movement_distance == 0.5

    for _ in range(100):
        sheep_pos = list(sheep.position)
        new_sheep_pos = sheep.move()
        if sheep_pos[0] == new_sheep_pos[0]:
            assert abs(new_sheep_pos[1] - sheep_pos[1]) == sheep.movement_distance
        else:
            assert abs(new_sheep_pos[0] - sheep_pos[0]) == sheep.movement_distance



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
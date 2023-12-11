from entities import Herd, Wolf


class Game:

    def __init__(self, initial_herd: Herd, initial_wolf: Wolf):
        self.herd = initial_herd
        self.wolf = initial_wolf
        self.wolf.herd = self.herd

    def advance_round(self):
        self.herd.move_herd()
        self.wolf.move()


herd = Herd(15, 10, 0.5)
wolf = Wolf("Wliczur", [0, 0], 1.0)

game = Game(herd, wolf)

game.advance_round()
from entities import Herd, Wolf


class Game:

    def __init__(self, initial_herd: Herd, initial_wolf: Wolf):
        self.herd = initial_herd
        self.wolf = initial_wolf
        self.wolf.herd = self.herd

    def advance_round(self):
        self.herd.move_herd()
        self.wolf.move()

succes = []
for game_number in range(1000):

    herd = Herd(15, 10, 0.5)
    wolf = Wolf("Wliczur", [0, 0], 1.0)

    game = Game(herd, wolf)

    for round_number in range(50):
        print(f"\n\n======================\nRunda numer {round_number+1}\n======================\n")
        game.advance_round()

    print(f"\n\nWilk złapał {wolf.caught_targets} owiec")
    if wolf.caught_targets == 15:
        succes.append(game_number)

print(f"Koniec 1000 gier. Udało się w {succes} grze")
import json
import csv
from entities import Herd, Wolf


class Game:

    def __init__(self, initial_herd: Herd, initial_wolf: Wolf):
        self.herd = initial_herd
        self.wolf = initial_wolf
        self.wolf.herd = self.herd

    def advance_round(self):
        self.herd.move_herd()
        self.wolf.move()

# succes = []
# for game_number in range(1000):
#
#     herd = Herd(15, 10, 0.5)
#     wolf = Wolf("Wliczur", [0, 0], 1.0)
#
#     game = Game(herd, wolf)
#
#     for round_number in range(65):
#         print(f"\n\n======================\nRunda numer {round_number+1}\n======================\n")
#         if len(herd.herd) == 0:
#             succes.append(game_number)
#             break
#         game.advance_round()
#
#     print(f"\n\nWilk złapał {wolf.caught_targets} owiec")
#
# print(f"Koniec 1000 gier. Udało się w {len(succes)} grach. {succes}")

json_list = []
csv_list = []

herd = Herd(15, 10, 0.5)
wolf = Wolf("Wliczur", [0, 0], 1.0)
game = Game(herd, wolf)

for round_number in range(50):
    print(f"\n\n======================\nRunda numer {round_number+1}\n======================\n")
    if len(herd.herd) == 0:
        break
    # game.advance_round()
    print(f"Pozycja wilka: {wolf}")
    print(f"Liczba żywych owiec {len(herd.herd)}")
    print(f"Najbliższa owca {wolf.target}, w odległości {wolf.best_dist} - jest aktywnie goniona przez wilka")

    json_list.append({"round_no": round_number,
                      "wolf_pos": wolf.position,
                      "sheep_pos": herd.get_all_herd_pos_with_nulls()})
    csv_list.append([round_number+1, len(herd.herd)])
    game.advance_round()

with open("game.json", "w") as f:
    json.dump(json_list, f, indent=4)

with open("rounds.csv", mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(csv_list)

print(f"\n\nWilk złapał {wolf.caught_targets} owiec")


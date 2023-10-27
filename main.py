import random
import math

class Wolf:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def move_towards(self, target_x, target_y, step_size):
        # Przesuń wilka w kierunku celu
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        if distance <= step_size:
            self.x = target_x
            self.y = target_y
        else:
            scale = step_size / distance
            self.x += dx * scale
            self.y += dy * scale

class Sheep:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_randomly(self, step_size):
        # Owca porusza się losowo
        direction = random.choice(['north', 'south', 'east', 'west'])
        if direction == 'north':
            self.y += step_size
        elif direction == 'south':
            self.y -= step_size
        elif direction == 'east':
            self.x += step_size
        elif direction == 'west':
            self.x -= step_size

class Game:
    def __init__(self, num_sheep, max_rounds):
        self.max_rounds = max_rounds
        self.round = 0
        self.wolf = Wolf()
        self.sheep = [Sheep(random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(num_sheep)]

    def play_round(self):
        if self.round < self.max_rounds and len(self.sheep) > 0:
            # Porusz owce
            for sheep in self.sheep:
                sheep.move_randomly(0.5)  # Przykładowa odległość ruchu owcy

            # Znajdź najbliższą owcę i porusz wilka w jej kierunku
            closest_sheep = min(self.sheep, key=lambda s: math.sqrt((s.x - self.wolf.x)**2 + (s.y - self.wolf.y)**2))
            self.wolf.move_towards(closest_sheep.x, closest_sheep.y, 0.8)  # Przykładowa odległość ruchu wilka

            # Sprawdź, czy wilk złapał owcę
            if math.sqrt((self.wolf.x - closest_sheep.x)**2 + (self.wolf.y - closest_sheep.y)**2) <= 0.5:
                self.sheep.remove(closest_sheep)

            self.round += 1

    def run_simulation(self):
        while self.round < self.max_rounds and len(self.sheep) > 0:
            self.play_round()
        if len(self.sheep) == 0:
            print("Wilk zjadł wszystkie owce!")
        else:
            print("Osiągnięto maksymalną liczbę rund.")

# Przykład użycia:
game = Game(num_sheep=10, max_rounds=50)
game.run_simulation()
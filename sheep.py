import random


class Sheep:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_alive = True
        self.sheep_number = 0
        self.dist_to_wolf = 0.0

    def move(self, sheep_move_dist):
        direction = random.randint(0, 3)
        if direction == 0:
            self.y += sheep_move_dist
        elif direction == 1:
            self.x += sheep_move_dist
        elif direction == 2:
            self.y -= sheep_move_dist
        else:
            self.x -= sheep_move_dist

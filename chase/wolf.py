import logging
import math


class Wolf:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_or_kill(self, nearest, wolf_move_dist):
        #  if sheep is in range of attack and then kill it
        if nearest.dist_to_wolf <= wolf_move_dist:
            self.x = nearest.x
            self.y = nearest.y
            nearest.is_alive = False
            logging.info("Wolf killed sheep no: " + str(nearest.sheep_number))
        else:  # else move to nearest one
            x_an = wolf_move_dist * ((nearest.x - self.x) / nearest.dist_to_wolf)
            y_an = wolf_move_dist * ((nearest.y - self.y) / nearest.dist_to_wolf)
            self.x += x_an
            self.y += y_an
            logging.info("Wolf moved to position: " + str(self.x) + str(self.y))

    def nearest_sheep(self, sheep):  # calculate distance to nearest sheep form list
        euclidean_distance = math.sqrt(((sheep.x - self.x) ** 2) + ((sheep.y - self.y) ** 2))
        logging.debug(
            "nearest_sheep(" + sheep.__str__() + self.__str__() + ") called, returned " + str(euclidean_distance))
        return euclidean_distance

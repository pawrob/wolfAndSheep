from wolf import Wolf
from sheep import Sheep
from utilities import *
import random
import math
import logging


def simulation_process(round_no, number_of_sheep, init_pos_limit, sheep_move_dist, wolf_move_dist, directory, wait):
    logging.debug("simulation_process(", round_no, number_of_sheep, init_pos_limit, sheep_move_dist, wolf_move_dist,
                  str(directory), wait, ") called")
    wolf = Wolf(0.0, 0.0)
    sheep = arrange(number_of_sheep, init_pos_limit)
    for i in range(1, round_no + 1):
        alive_sheep = ([x for x in sheep if x.is_alive])
        if not alive_sheep:
            print("All sheep are eaten!")
            break
        for j in alive_sheep:
            # move sheep
            j.move(sheep_move_dist)
            # calculate distance to nearest sheep form wolf
            j.dist_to_wolf = nearest_sheep(j, wolf)
        nearest = min(alive_sheep, key=lambda shp: shp.dist_to_wolf)
        if nearest.dist_to_wolf <= wolf_move_dist:
            wolf.x = nearest.x
            wolf.y = nearest.y
            nearest.is_alive = False
        if nearest.dist_to_wolf > wolf_move_dist:
            x_an = wolf_move_dist * ((nearest.x - wolf.x) / nearest.dist_to_wolf)
            y_an = wolf_move_dist * ((nearest.y - wolf.y) / nearest.dist_to_wolf)
            wolf.x += x_an
            wolf.y += y_an
            logging.info("Wolf moved to position: " + str(wolf.x) + str(wolf.y))
        if nearest.is_alive:
            print("Turn:", i, "\tWolf position: %.3f %.3f" % (wolf.x, wolf.y), "\tRemaining sheep:",
                  alive_sheep.__len__())
            logging.info("Turn: " + str(i) + "\tWolf position: " + str(wolf.x) + ", " + str(wolf.y) +
                         "\tRemaining sheep: " + str(alive_sheep.__len__()))
        else:
            x = nearest.sheep_number
            print("Turn:", i, "\tWolf position: %.3f %.3f" % (wolf.x, wolf.y), "\tRemaining sheep:",
                  alive_sheep.__len__(), "\tSheep", x, "died")
            logging.info("Turn: " + str(i) + "\tWolf position: " + str(wolf.x) + ", " + str(wolf.y) +
                         "\tRemaining sheep: " + str(alive_sheep.__len__()) + "\tSheep " + str(x) + "died")
        json_export(sheep, wolf, i, directory)
        csv_export(i, alive_sheep.__len__())
        if wait:
            input("Press a key to continue...")


def arrange(number_of_sheep, init_pos_limit):
    sheep = []
    for i in range(number_of_sheep):
        sheep.append(Sheep(random.uniform(-init_pos_limit, init_pos_limit),
                           random.uniform(-init_pos_limit, init_pos_limit)))
        sheep[i].sheep_number = i + 1
    logging.debug("arrange(" + str(number_of_sheep) + str(init_pos_limit) + ") called, returned" + str(sheep))
    return sheep


def no_of_sheep_alive(sheep):
    alive_count = 0
    for x in sheep:
        if x.is_alive:
            alive_count += 1
    logging.debug("no_of_sheep_alive(" + sheep.__str__() + ") called, returned" + str(alive_count))
    return alive_count


def nearest_sheep(sheep, wolf):
    euclidean_distance = math.sqrt(((sheep.x - wolf.x) ** 2) + ((sheep.y - wolf.y) ** 2))
    logging.debug("nearest_sheep(" + sheep.__str__() + wolf.__str__() + ") called, returned" + str(euclidean_distance))
    return euclidean_distance

# def simulation_process(round_number, number_of_sheep, init_pos_limit, sheep_move_dist, wolf_move_dist):
#     wolf = Wolf(0.0, 0.0)
#     sheep = arrange(number_of_sheep, init_pos_limit)
#     for i in range(1, round_number + 1):
#         sheep_alive_round = no_of_sheep_alive(sheep)
#         if sheep_alive_round == 0:
#             print("All sheep are eaten!")
#             break
#         for j in sheep:
#             # move sheep
#             j.move(sheep_move_dist)
#             # calculate distance to nearest sheep form wolf
#             j.dist_to_wolf = nearest_sheep(j, wolf)
#         nearest = min(sheep, key=lambda shp: shp.dist_to_wolf)
#         if nearest.dist_to_wolf <= wolf_move_dist:
#             wolf.x = nearest.x
#             wolf.y = nearest.y
#             nearest.is_alive = False
#         if nearest.dist_to_wolf > wolf_move_dist:
#             x_an = wolf_move_dist * ((nearest.x - wolf.x) / nearest.dist_to_wolf)
#             y_an = wolf_move_dist * ((nearest.y - wolf.y) / nearest.dist_to_wolf)
#             wolf.x += x_an
#             wolf.y += y_an
#         if nearest.is_alive:
#             j = "none"
#         else:
#             j = nearest.sheep_number
#         print("Turn:", i, "\tWolf position: %.3f %.3f" % (wolf.x, wolf.y), "\tRemaining sheep:",
#               sheep_alive_round, "\tSheep", j, "died")
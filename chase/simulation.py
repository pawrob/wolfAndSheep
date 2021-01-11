from chase.wolf import Wolf
from chase.sheep import Sheep
from chase.utilities import *
import random
import logging


def simulation_process(round_no, number_of_sheep, init_pos_limit, sheep_move_dist, wolf_move_dist, directory,
                       wait_flag):
    logging.debug("simulation_process(", round_no, number_of_sheep, init_pos_limit, sheep_move_dist, wolf_move_dist,
                  str(directory), wait_flag, ") called")
    # wolf nad sheep init
    wolf = Wolf(0.0, 0.0)
    sheep = arrange(number_of_sheep, init_pos_limit)

    # iterate over rounds
    for i in range(1, round_no + 1):
        # fill array with only alive sheep
        alive_sheep = collect_alive_sheep(sheep)

        # check if any of sheep are alive
        if not alive_sheep:
            print("All sheep are eaten!")
            break

        for j in alive_sheep:
            # sheep moves
            j.move(sheep_move_dist)
            # calculate distance from sheep to wolf
            j.dist_to_wolf = wolf.nearest_sheep(j)

        # choose nearest sheep
        nearest_sheep = min(alive_sheep, key=lambda shp: shp.dist_to_wolf)
        # kill sheep or mow to the nearest one
        wolf.move_or_kill(nearest_sheep, wolf_move_dist)
        # check if nearest sheep is still alive
        if nearest_sheep.is_alive:
            print("Turn:", i, "\tWolf position: %.3f %.3f" % (wolf.x, wolf.y), "\tRemaining sheep:",
                  alive_sheep.__len__())
            logging.info("Turn: " + str(i) + "\tWolf position: " + str(wolf.x) + ", " + str(wolf.y) +
                         "\tRemaining sheep: " + str(alive_sheep.__len__()))
        # if not print it out
        else:
            print("Turn:", i, "\tWolf position: %.3f %.3f" % (wolf.x, wolf.y), "\tRemaining sheep:",
                  alive_sheep.__len__(), "\tSheep", nearest_sheep.sheep_number, "died")

            logging.info("Turn: " + str(i) + "\tWolf position: " + str(wolf.x) + ", " + str(wolf.y) +
                         "\tRemaining sheep: " + str(alive_sheep.__len__()) + "\tSheep " + str(
                nearest_sheep.sheep_number) + "died")

        # export to json file
        json_export(sheep, wolf, i, directory)
        # export to csv file
        csv_export(i, alive_sheep.__len__())
        # check if -w option was selected
        if wait_flag:
            input("Press a key to continue...")


def arrange(number_of_sheep, init_pos_limit):
    sheep = []
    for i in range(number_of_sheep):  # generate position for sheep
        sheep.append(Sheep(random.uniform(-init_pos_limit, init_pos_limit),
                           random.uniform(-init_pos_limit, init_pos_limit)))
        sheep[i].sheep_number = i + 1  # assign number to sheep
    logging.debug("arrange(" + str(number_of_sheep) + str(init_pos_limit) + ") called, returned " + str(sheep))
    return sheep


def collect_alive_sheep(sheep):
    alive_sheep = []
    for i in sheep:
        if i.is_alive:  # check if sheep is still alive
            alive_sheep.append(i)  # put it to the list
    logging.debug("no_of_sheep_alive(" + str(sheep.__str__()) + ") called, returned " + str(alive_sheep))
    return alive_sheep

import argparse
import os
import csv
import json
import logging
import sys
from configparser import ConfigParser



def json_export(sheep, wolf, round_no, directory):
    logging.debug("json_export(", sheep.__str__(), wolf.__str__(), round_no, str(directory), ")")
    x = {
        "round_no": round_no,
        "wolf_pos": str(wolf.x) + ", " + str(wolf.y)
    }
    pos = []
    for i in sheep:
        if i.is_alive:
            pos.append(str(i.x) + ", " + str(i.y))
        else:
            pos.append("None")
    x['sheep_pos'] = pos
    if round_no == 1:
        if directory:
            direct = os.getcwd()
            path = direct + '\\' + directory
            dir_path = os.path.dirname(path)
            if not os.path.exists(dir_path):
                print("Create")
                os.mkdir(directory)
            os.chdir(directory)
        f = open("pos.json", "w")
    else:
        f = open("pos.json", "a")
    f.write(json.dumps(x, indent=4, sort_keys=True))
    f.close()


def csv_export(round_no, sheep_number):
    logging.debug("csv_export(", round_no, sheep_number, ")")
    if round_no == 1:
        with open('alive.csv', mode='w', newline='') as csv_file:
            fieldnames = ['round_no', 'alive']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'round_no': round_no, 'alive': sheep_number})
    else:
        with open('alive.csv', mode='a', newline='') as csv_file:
            fieldnames = ['round_no', 'alive']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'round_no': round_no, 'alive': sheep_number})


def parse_config(file):
    config = ConfigParser()
    config.read(file)
    init = config.get('Terrain', 'InitPosLimit')
    sheep = config.get('Movement', 'SheepMoveDist')
    wolf = config.get('Movement', 'WolfMoveDist')
    if float(init) < 0 or float(sheep) < 0 or float(wolf) < 0:
        logging.error("Not positive number passed as argument")
        raise ValueError("Number is not positive")
    logging.debug("parse_config(", file, ") called, returned,", float(init), float(sheep), float(wolf))
    return float(init), float(sheep), float(wolf)


# check if passed value is positive
def is_positive(value):
    if int(value) <= 0:
        raise argparse.ArgumentTypeError("%s value must be greater than 0!" % int(value))
    logging.debug("is_positive(", value, ") called, returned,", int(value))
    return int(value)

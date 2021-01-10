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


# def parse_values(args):
#     if args.config_file:
#         init_pos_limit, sheep_move_dist, wolf_move_dist = parse_config(args.config_file)
#     if args.directory:
#         directory = args.directory
#     if args.help:
#         sys.exit()
#     if args.log_file:
#         if args.log_file == "DEBUG":
#             lvl = logging.DEBUG
#         elif args.log_file == "INFO":
#             lvl = logging.INFO
#         elif args.log_file == "WARNING":
#             lvl = logging.WARNING
#         elif args.log_file == "ERROR":
#             lvl = logging.ERROR
#         elif args.log_file == "CRITICAL":
#             lvl = logging.CRITICAL
#         else:
#             raise ValueError("Invalid log level!")
#         logging.basicConfig(level=lvl, filename="chase.log")
#         logging.debug("debug")
#     if args.round_no:
#         round_no = args.round_no
#     if args.number_of_sheep:
#         number_of_sheep = args.number_of_sheep
#     if args.wait:
#         wait = args.wait

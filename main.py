from numpy import long

from simulation import simulation_process
from utilities import *
import os
import random
import argparse


def main():
    round_no = 50
    number_of_sheep = 15
    init_pos_limit = 10.0
    sheep_move_dist = 0.5
    wolf_move_dist = 1.0
    directory = None
    wait = False

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', help='Set configuration file', metavar='FILE', dest='config_file',
                        action='store')
    parser.add_argument('-d', '--dir', help='Select destination for log files', metavar='DIR', dest='directory',
                        action='store')
    parser.add_argument('-h', '--help', default=argparse.SUPPRESS, directory='help',
                        help='Synopsis\n'
                             'main [ -c --config config_file ] [ -d --dir directory ] [ -h --help ] '
                             '[ -l --log log_file ] [ -r --rounds round_no ] [ -s --sheep number_of_sheep ] '
                             '[ -w --wait ]\n\n'
                             'Summary\n'
                             'The program conducts simulation of wolf and sheep.\n')
    parser.add_argument('-l', '--log', help='Create event log file with LEVEL of event', metavar='LEVEL',
                        dest='log_file', action='store')
    parser.add_argument('-r', '--rounds', help='Select number of rounds', metavar='NUM', dest='round_no',
                        type=long, choices=range(1, 9223372036854775807), action='store')
    parser.add_argument('-s', '--sheep', help='Select number of sheep', metavar='NUM', dest='number_of_sheep',
                        type=long, choices=range(1, 9223372036854775807), action='store')
    parser.add_argument('-w', '--wait', help='Set pause between rounds', action='store_true')

    args = parser.parse_args()
    # parse_values(args)
    if args.config_file:
        init_pos_limit, sheep_move_dist, wolf_move_dist = parse_config(args.config_file)
    if args.directory:
        directory = args.directory
    if args.help:
        help = args.help
    if args.log_file:
        if args.log_file == "DEBUG":
            lvl = logging.DEBUG
        elif args.log_file == "INFO":
            lvl = logging.INFO
        elif args.log_file == "WARNING":
            lvl = logging.WARNING
        elif args.log_file == "ERROR":
            lvl = logging.ERROR
        elif args.log_file == "CRITICAL":
            lvl = logging.CRITICAL
        else:
            raise ValueError("Invalid log level!")
        logging.basicConfig(level=lvl, filename="chase.log")
        logging.debug("debug")
    if args.round_no:
        round_no = args.round_no
    if args.number_of_sheep:
        number_of_sheep = args.number_of_sheep
    if args.wait:
        wait = args.wait

    simulation_process(round_no, number_of_sheep, init_pos_limit, sheep_move_dist, wolf_move_dist, directory, wait)


if __name__ == '__main__':
    main()

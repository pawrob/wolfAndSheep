# wolfAndSheep
Project for python basics, simulation of wolf and sheep
# Introduction
Program simulates bunch of sheep in natural envirement chased by wolf. Every round wolf want to kill one sheep.<br/> If there is no sheep in his range, wolf goes to the nearest sheep. Game stops if there isnt any alive sheep or all rounds are over.
## Technologies
Project is created with:
* Setuptools
* argparse
* logging
* ConfigParser
## Setup
To run this project, install it locally using pip:

```
$ cd ../wolfandsheep
$ python setup.py sdist
$ pip install dist/chase-1.0.tar.gz
```
or run it from source code via __main__.py

## Options
You can specify additional options while using script:
* -c, --config - Set configuration file with startup values for:<br/>
InitPosLimit<br/>
SheepMoveDist<br/>
WolfMoveDist<br/>
* -d, --dir - Select destination for log files
* -l, --log, Create event log file with LEVEL of event ( DEBUG, INFO, WARNING, ERROR, CRITICAL)
* -r, --rounds, Select number of rounds
* -s, --sheep, Select number of sheep
* -w, --wait, Set pause between rounds

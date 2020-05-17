#!/usr/bin/env python3
"""
   Reliability calculator for tasks.
    Copyright © 2020 Pourya Gohari
Usage:
    calculate  [options]
Options:
    --input, -i FILE              input file [default: input.txt]
    --method, -m NAME             Method of increasing reliability [default: replication]
    --faultrate, -f ALPHA         system fault rate in millisecond  [default: 0.00001]
    --sensfactor, -s D            system sensitivity factor [default: 3]
    --output, -o FILE             output file [default: output.txt]
    --version, -v                 show version and exit
    --help, -h                    show this message
"""
import numpy as np
import math
from docopt import docopt
from pathlib import Path

d = 2
f_max = 2000
f_min = 800
landa0 = 0.00001
M = 'replication'
output = 'output.txt'
input = 'input.txt'


def cal_replication(exec_time, target):
    rou = 1
    rou_min = f_min / f_max
    landa = (landa0 * (10**((d * (1 - rou)) / (1 - rou_min))))
    print(landa)
    landa = (-1) * landa
    r = math.exp(landa * exec_time)
    PoF = 1 - r
    print(r)
    replica = math.ceil(math.log((1 - target) / PoF) / math.log(PoF))
    return replica


if __name__ == "__main__":

    # arguments = docopt(__doc__, version='0.8.0')
    # print(arguments)
    # if arguments['--output']:
    #     output = arguments['--output']

    # if arguments['--input']:
    #     input = arguments['--input']

    # if arguments['--faultrate']:
    #     landa0 = float(arguments['--faultrate'])

    # if arguments['--sensfactor']:
    #     d = int(arguments['--sensfactor'])

    # if arguments['--method']:
    #     M = arguments['--method']
    # print(d)

    print(cal_replication(20, 0.999))

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
    --sensfactor, -s D            system sensitivity factor [default: 2]
    --output, -o FILE             output file [default: output.txt]
    --print, -p                   show output in screen
    --version, -v                 show version and exit
    --help, -h                    show this message
"""
from numpy import loadtxt
import math
from docopt import docopt
from pathlib import Path

d = 2
f_max = 2000
f_min = 800
f_sel = 2000
# v[] = {0.973, 1.023, 1.062, 1.115, 1.3};
v_max = 1.3
v_min = 800
v_sel = 1.3
landa0 = 0.00001
M = 'replication'
output = 'output.txt'
input = 'input.txt'


def cal_replication(exec_time, target):
    rou = 1
    rou_min = f_min / f_max
    landa = (landa0 * (10**((d * (1 - rou)) / (1 - rou_min))))
    # print(landa)
    landa = (-1) * landa
    r = math.exp(landa * exec_time)
    PoF = 1 - r
    # print(r)
    replica = math.ceil(math.log((1 - target) / PoF) / math.log(PoF))
    return replica

# TODO add NMR Reliability

# Two phase NMR


def cal_NMR(exec_time, target):
    n = 3
    while(True):
        rou_min = v_min / v_max
        rou = v_sel / v_max
        # t_i ==> Acrual Exec. Time
        t_i = exec_time * f_max / f_min
        landa = (landa0 * (10 ** ((d * (1 - rou)) / (1 - rou_min))))
        landa = (-1) * landa
        r = math.exp(landa * exec_time)
        R_1 = (r ** (math.ceil(n / 2)))
        landa = (landa0 * math.pow(10, ((d * (1 - 1)) / (1 - rou_min))))
        landa = (-1) * landa
        r = math.exp((landa * exec_time))
        R_2 = 0
        r_max = math.exp(-landa0 * exec_time)
        for k in range(1, (math.floor(n / 2)+1)):
            for j in range(1, k+1):
                R_2 += math.comb((math.ceil(n / 2)), j) * (((1 - r) ** j)) * ((r ** (math.ceil(n / 2) - j))) * math.comb(
                    math.floor(n / 2), k - j) * (((1 - r_max) ** (k - j))) * ((r_max ** (math.floor(n / 2) - (k - j))))
        #print(n, "=")
        # print(R_1+R_2)
        if (R_1+R_2) >= target:
            return n
        else:
            n += 2


if __name__ == "__main__":

    arguments = docopt(__doc__, version='0.8.0')
    if arguments['--output']:
        output = arguments['--output']

    if arguments['--input']:
        input = arguments['--input']

    if arguments['--faultrate']:
        landa0 = float(arguments['--faultrate'])

    if arguments['--sensfactor']:
        d = int(arguments['--sensfactor'])

    if arguments['--method']:
        M = arguments['--method']

    if arguments['--print']:
        p = arguments['--print']

    data = loadtxt(input, delimiter='\t', skiprows=1)  # skips header
    for x in data:
        # print(x[0])
        # print(x[1])
        if(M == 'replication'):
            print(cal_replication(x[0], x[1]))
        if(M == 'NMR'):
            print(cal_NMR(x[0], x[1]))

#!/usr/bin/env python3
"""
   Reliability calculator for tasks.
    Copyright © 2020 Pourya Gohari
Usage:
    caculate                [options]
Options:
    --input=PATH, -i PATH               PATH of input <.txt> [default: input.txt]
    --method=M, -m M                    Method of increasing reliability <replication> [default: replication]
    --faultrate=ALPHA, -f ALPHA         system fault rate in millisecond  [default: 0.00001]
    --sensfactor=D, -s D                system sensitivity factor [default: 3]
    --output=PATH, -o PATH              PATH of output <.txt> [default: out.txt]
    --version, -v                       show version and exit
    --help, -h                          show this message
"""
import numpy as np
import math
from docopt import docopt
from pathlib import Path

if __name__ == "__main__":
    arguments = docopt(__doc__, version='0.8.0')

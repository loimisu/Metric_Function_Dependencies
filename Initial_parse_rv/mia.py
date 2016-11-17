#mia    AA-1007-TPA-MIA    3:00P 12-01-11	2011-12-01  2:57P
# -*- coding: utf-8 -*-
import numpy as np
#import pandas as pd
from itertools import islice
from operator import itemgetter
from datetime import datetime


filepath="/root/Documents/6720/clean_flight/2011-12-01-data.txt"
infile = open(filepath,"r")
dataset = islice(infile, 21)

for aline in dataset:
    data = aline.split()
    if data[0] in ("mia"):
        
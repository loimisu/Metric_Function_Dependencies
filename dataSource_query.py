#orbitz
# -*- coding: utf-8 -*-
import numpy as np
#import pandas as pd
from itertools import islice
from operator import itemgetter
from datetime import datetime


filepath="/root/Documents/6720/clean_flight/2011-12-01-data.txt"
infile = open(filepath,"r")

#myset = set()
Unique_datasource = []
for aline in infile:
    data = aline.split()
    #myset.add(data[0])
    if data[0] not in Unique_datasource :
        Unique_datasource.append(data[0])
print Unique_datasource 
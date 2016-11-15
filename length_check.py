
# -*- coding: utf-8 -*-
# flightaware	AA-1518-DFW-SDF	2011-12-01 12:10PM CST	2011-12-01 12:18PM CST	 C20 	2011-12-01 02:46PM EST	2011-12-01 02:53PM EST	 A15 
# wunderground	AA-1518-DFW-SDF	2011-12-01 12:10PM CST	2011-12-01 12:18PM CST	 C20 	2011-12-01 02:46PM EST	2011-12-01 02:53PM EST	 A15

import numpy as np
import pandas as pd
from itertools import islice
from operator import itemgetter
from datetime import datetime


if __name__ == '__main__':
    filepath="/root/Documents/6720/clean_flight/2011-12-01-data.txt"
    infile = open(filepath,"r")
    #dataset = islice(infile, 21)
    
    def filter_input(data):
        return len(data.strip())
    
    #for aline in dataset:
    numlines_array = []
    for aline in infile:
        data = filter(filter_input, aline.split('\t'))
        #if data[0] in ("flightview","panynj","gofox","foxbusiness","allegiantair"):
        if data[0] in ("flightwise"):
            numlines = str(len(data))
            if numlines not in numlines_array:
                numlines_array.append(numlines)
    print numlines_array
            
                
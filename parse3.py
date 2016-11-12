# -*- coding: utf-8 -*-
# flightexplorer	UA-1005-BOS-IAH	12/1/2011 4:19PM EST			12/1/2011 7:49PM CST
import numpy as np
#import pandas as pd
from itertools import islice
from operator import itemgetter
from datetime import datetime


filepath="/root/Documents/6720/clean_flight/2011-12-01-data.txt"
infile = open(filepath,"r")
#dataset = islice(infile, 21)

#for aline in dataset:
for aline in infile:
    data = aline.split()
    if data[0] in "flightexplorer":
        dataArray = np.array(itemgetter(0,1,2,3,5,6)(data))
        in_date_start = datetime.strptime(dataArray[2],"%m/%d/%Y")
        in_date_end = datetime.strptime(dataArray[4],"%m/%d/%Y")
        out_date_start = datetime.strftime(in_date_start,"%Y%m%d")
        out_date_end = datetime.strftime(in_date_end,"%Y%m%d")  
        in_time_start = datetime.strptime(dataArray[3], "%I:%M%p")
        in_time_end = datetime.strptime(dataArray[5], "%I:%M%p")
        out_time_start = datetime.strftime(in_time_start, "%H:%M")
        out_time_end = datetime.strftime(in_time_end, "%H:%M")
        dataArray[2] = out_date_start
        dataArray[3] = out_time_start
        dataArray[4] = out_date_end
        dataArray[5] = out_time_end
        print dataArray

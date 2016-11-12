# -*- coding: utf-8 -*-
# weather AA-1007-TPA-MIA	2011-12-01 01:55 PM			2011-12-01 03:00 PM
# flightarrival	AA-1518-DFW-SDF	2011-12-01 12:10 PM			2011-12-01 03:10 PM
import numpy as np
#import pandas as pd
from itertools import islice
from operator import itemgetter
from datetime import datetime


filepath="/root/Documents/6720/clean_flight/2011-12-01-data.txt"
infile = open(filepath,"r")
dataset = islice(infile, 21)

for aline in dataset:
#for aline in infile:
    data = aline.split()
    if data[0] in ("weather"):
        datalist = data
        datalist[3:5] = [''.join(datalist[3:5])]
        datalist[5:] = [''.join(datalist[5:])]
        dataArray = np.array(datalist)
        in_date_start = datetime.strptime(dataArray[2],"%Y-%m-%d") #only date format is different from "airtravelcenter"
        in_date_end = datetime.strptime(dataArray[4],"%Y-%m-%d")   #only date format is different from "airtravelcenter"
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
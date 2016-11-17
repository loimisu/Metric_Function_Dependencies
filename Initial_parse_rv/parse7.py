# -*- coding: utf-8 -*-
# travelocity	AA-1007-TPA-MIA	Dec 01 - 1:55pm	Dec 01 - 1:57pm	F78	Dec 01 - 3:00pm	Dec 01 - 2:57pm	D5
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
    if data[0] in ("travelocity"):
        datalist = list(itemgetter(0,1,6,7,9,15,16,18)(data))
        datalist[2:4] = [''.join(datalist[2:4])]
        datalist[4:6] = [''.join(datalist[4:6])]
        dataArray = np.array(datalist)
        in_date_start = datetime.strptime(dataArray[2],"%b%d") #only date format is different from "airtravelcenter"
        in_date_end = datetime.strptime(dataArray[4],"%b%d")   #only date format is different from "airtravelcenter"
        out_date_start = datetime.strftime(in_date_start,"2011%m%d")
        out_date_end = datetime.strftime(in_date_end,"2011%m%d")  
        in_time_start = datetime.strptime(dataArray[3], "%I:%M%p")
        in_time_end = datetime.strptime(dataArray[5], "%I:%M%p")
        out_time_start = datetime.strftime(in_time_start, "%H:%M")
        out_time_end = datetime.strftime(in_time_end, "%H:%M")
        dataArray[2] = out_date_start
        dataArray[3] = out_time_start
        dataArray[4] = out_date_end
        dataArray[5] = out_time_end
        print dataArray
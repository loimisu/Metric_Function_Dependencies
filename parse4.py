# -*- coding: utf-8 -*-
# businesstravellogue	AA-1007-TPA-MIA		2011-12-01 02:07 PM	F78		2011-12-01 02:57 PM	D5
# flylouisville	AA-1007-TPA-MIA		2011-12-01 02:07 PM	F78		2011-12-01 02:57 PM	D5
# flights	AA-1007-TPA-MIA		2011-12-01 02:07 PM	F78		2011-12-01 02:57 PM	D5
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
    if data[0] in ("flights","flylouisville","businesstravellogue"):
        datalist = list(itemgetter(0,1,2,3,4,6,7,8)(data))
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
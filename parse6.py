# -*- coding: utf-8 -*-
# flightview	AA-1007-TPA-MIA		2:07 PMDec 01			2:57 PMDec 01	
# panynj	AA-1007-TPA-MIA		2:07 PMDec 01			2:57 PMDec 01	
# gofox	AA-1007-TPA-MIA		2:07 PMDec 01			2:57 PMDec 01	
# foxbusiness	AA-1007-TPA-MIA		2:07 PMDec 01			2:57 PMDec 01	
# allegiantair	AA-1007-TPA-MIA		2:07 PMDec 01			2:57 PMDec 01	
# boston	AA-1007-TPA-MIA		2:07 PMDec 01			2:49 PMDec 01	
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
    if data[0] in ("flightview","panynj","gofox","foxbusiness","allegiantair","boston"):
        datalist = list(data)
        datalist.insert(3, datalist[3][:2])
        datalist.insert(4, datalist[4][2:])
        datalist.insert(8, datalist[8][:2])
        datalist.insert(9, datalist[9][2:])
        datalist = list(itemgetter(0,1,2,3,4,6,7,8,9,11)(datalist))
        datalist[4:6] = [''.join(datalist[4:6])]
        datalist[7:] = [''.join(datalist[7:])]
        datalist[2:4] = [''.join(datalist[2:4])]
        datalist[4:6] = [''.join(datalist[4:6])]
        i = datalist
        a, b = i.index(i[2]), i.index(i[3])
        i[b], i[a] = i[a], i[b]
        i.insert(4, i.pop(5))
        dataArray = np.array(i)
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
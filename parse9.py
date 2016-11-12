# -*- coding: utf-8 -*-
# orbitz	AA-1007-TPA-MIA	1:55pDec 1	1:57pDec 1	 F78	3:00pDec 1	2:57pDec 1	 D5
# mytripandmore	AA-1007-TPA-MIA	1:55pDec 1	1:57pDec 1	 F78	3:00pDec 1	2:57pDec 1	 D5
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
    if data[0] in ("orbitz", "mytripandmore"):
        datalist = list(data)
        datalist.insert(4, datalist[4][:4])
        datalist.insert(5, datalist[5][4:5])
        datalist.insert(6, datalist[6][5:])
        datalist.insert(12, datalist[12][:4])
        datalist.insert(13, datalist[13][4:5])
        datalist.insert(14, datalist[14][5:])
        datalist = list(itemgetter(0,1,4,5,6,8,12,13,14,16)(datalist))
        for i, item in enumerate(datalist):
            if item in 'p':
                datalist[i] = 'PM'
            if item in 'a':
                datalist[i] = 'AM'
        datalist[2:4] = [''.join(datalist[2:4])]
        datalist[3:5] = [''.join(datalist[3:5])]
        datalist[4:6] = [''.join(datalist[4:6])]
        datalist[5:] = [''.join(datalist[5:])]
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
        
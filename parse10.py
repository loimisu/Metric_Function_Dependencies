# -*- coding: utf-8 -*-
# airtravelcenter	UA-779-BOS-DEN		12/1/11 2:51 PM (-05:00)			12/1/11 5:17 PM (-07:00)	
# myrateplan	UA-779-BOS-DEN		12/1/11 2:51 PM (-05:00)			12/1/11 5:17 PM (-07:00)	
# helloflight	UA-779-BOS-DEN		12/1/11 2:51 PM (-05:00)			12/1/11 5:17 PM (-07:00)	
# flytecomm	UA-779-BOS-DEN		12/1/11 2:51 PM (-05:00)			12/1/11 5:17 PM (-07:00)
# ("flytecomm"): this pattern has some unmatch date format, parsing is interuppted
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
    if data[0] in ("airtravelcenter","myrateplan", "helloflight"):
    # ("flytecomm"): this pattern has some unmatch date format, parsing is interuppted
        datalist = list(itemgetter(0,1,2,3,4,6,7,8)(data))
        datalist[3:5] = [''.join(datalist[3:5])]
        datalist[5:] = [''.join(datalist[5:])]
        dataArray = np.array(datalist)
        in_date_start = datetime.strptime(dataArray[2],"%m/%d/%y")
        in_date_end = datetime.strptime(dataArray[4],"%m/%d/%y")
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
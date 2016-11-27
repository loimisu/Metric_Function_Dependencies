# -*- coding: utf-8 -*-
import re
import numpy as np
import pandas as pd
import os

if __name__ == '__main__':
    filepath="/home/hduser/git/Metric_Function_Dependencies/clean_flight/2011-12-11-data.txt"
#     path = "/home/hduser/git/Metric_Function_Dependencies/clean_flight"
# for file in os.listdir(path):
#     if file.endswith(".txt"):
#         filepath = path + "/" +file
    infile = open(filepath,"r")
    
    def filter_input(data):
        return len(data.strip()) # removes '\n' from the beginning and end of the string
        
    numlines_array = []
    source_nm = []
    flight_nm = []
    time1 = []
    time2 = []
    time3 = []
    time4 = []


    patRemove = re.compile(r'[ -]*(Contact|Not|Delay|On Time|&nbsp|HST|AKST|PST|MST|CST|EST|Sun|Sat|Mon|Tues|Tue|Wed|Thurs|Thur|Thu|Fri).*|[ ]*\(.*\).*$|^.*(Term|B32).*$|.*[,*.].*|.*( - ).*', re.IGNORECASE)
    # remove string with ' - contact%' or 'not%' on item
    # remove string with 'delay%' or 'on time%' on item
    # remove stiing with with '&nbsp'
    # remove string with '(%%)' on item
    # remove string with '%Term%' on item and items for string start with 'Term%'
    # remove comma(,), dash with space( - ), star(*)
    # remove sting of USA Time Zone ('HST', 'AKST', 'PST', 'MST', 'CST' ,'EST')
    # remove days of week ('Sun','Sat','Mon'), no thers


    for aline in infile:
        data = filter(filter_input, aline.split('\t')) 
        # remove '\t' from the beginning and end of the string
        if len(data[0])>=3 and data[1] in ("UA-1534-RTB-IAH", "AA-2098-ORD-BOS"):
            data = map(lambda item: patRemove.sub(' ', item), data) 
            
            #datalist = filter(lambda item: len(item) > 8, data[1:])
            datalist = map(lambda item: re.findall(r'[0-9]+:[0-9]+[ ]*[APap]*[Mm]*', item), data[2:])

            datalist.insert(0,data[1])    
            
            #replace a/p to am/pm

            n = 5 - len(datalist)
            if len(datalist) <= 5:
                datalist.extend(['NaN']*n)

            flight_nm.append(datalist[0])
            time1.append(datalist[1])
            time2.append(datalist[2])
            time3.append(datalist[3])
            time4.append(datalist[4])
            # if item index not exist, then set as 'null'   
      
    data = {
        'flight_nm': flight_nm,
        'time1': time1,
        'time2': time2,
        'time3': time3,
        'time4': time4
    }
    
    df = pd.DataFrame(data)
    print df
#     df.to_csv('/home/hduser/git/Metric_Function_Dependencies/output01.csv')
# print file + " is successully exported to csv!"
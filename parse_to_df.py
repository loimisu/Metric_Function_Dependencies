# -*- coding: utf-8 -*-
import re
import numpy as np
import pandas as pd
import os

if __name__ == '__main__':
    #filepath="/home/hduser/git/Metric_Function_Dependencies/clean_flight/2011-12-01-data.txt"
    path = "/home/hduser/git/Metric_Function_Dependencies/clean_flight"
for file in os.listdir(path):
    if file.endswith(".txt"):
        filepath = path + "/" +file
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

    patRemove = re.compile(r'[ -]*(Contact|Not|Delay|On Time|&nbsp|HST|AKST|PST|MST|CST|EST).*|[ ]*\(.*\).*$|^.*Term.*$|[,]|( - )|[*]', re.IGNORECASE)
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
        #if data[0] in ("aa", "ua"):
        data = map(lambda item: patRemove.sub(' ', item), data) 
        
        datalist = filter(lambda item: len(item) > 8, data[1:])
        datalist.insert(0,data[0])    
        #datalist = map(lambda item: re.sub(r'([1-9]+[ap][a-z]*)',' ', item, re.IGNORECASE), datalist)
        #replace a/p to am/pm

        n = 6 - len(datalist)
        if len(datalist) <= 6:
            datalist.extend(['null']*n)

        source_nm.append(datalist[0])
        flight_nm.append(datalist[1])
        time1.append(datalist[2])
        time2.append(datalist[3])
        time3.append(datalist[4])
        time4.append(datalist[5])
        # if item index not exist, then set as 'null'   
      
    data = {
        'source_nm': source_nm,
        'flight_nm': flight_nm,
        'time1': time1,
        'time2': time2,
        'time3': time3,
        'time4': time4
    }
    
    df = pd.DataFrame(data)
    #print df
    df.to_csv('/home/hduser/git/Metric_Function_Dependencies/output01.csv')
    print file + " is successully exported to csv!"
    
            

            
            
                    
            

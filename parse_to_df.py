# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import re


if __name__ == '__main__':
    filepath="/root/Documents/6720/clean_flight/2011-12-01-data.txt"
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
    for aline in infile:
        data = filter(filter_input, aline.split('\t')) # remove '\t' from the beginning and end of the string
        #if data[0] in ("aa", "ua"):
        data = map(lambda item: re.sub(r'[ -]+(Contact|Not).*','', item, re.IGNORECASE), data) # remove string with ' - contact%' or 'not%' on item
        data = map(lambda item: re.sub(r' +(Delay|(On Time)).*$','', item, re.IGNORECASE), data) # remove string with '%delay%' or '%on time%' on item
        data = map(lambda item: re.sub(r' +([(].*[)]).*$','', item, re.IGNORECASE), data) # remove string with '(%%)' on item
        data = map(lambda item: re.sub(r'^(Not).*','', item, re.IGNORECASE), data) # remove items for string start with 'Not %' 
        data = map(lambda item: re.sub(r'.*(Term).*','', item, re.IGNORECASE), data) 
        # remove string with'%Term%' on item and items for string start with 'Term%'
            
        datalist = filter(lambda item: len(item) > 8, data[1:])
        datalist.insert(0,data[0])    
        datalist = map(lambda item: re.sub(r'([,]|( - )|[*])','', item), datalist)
        numlines = str(len(datalist))
    #    if numlines not in numlines_array:
    #            numlines_array.append(numlines)
    #print numlines_array        
        
        source_nm.append(datalist[0])
        flight_nm.append(datalist[1])
        time1.append(datalist[2])
        # if item index not exist, then set as 'null'   
        if len(datalist) <= 4:
            try:
                time2.append(datalist[3])
            except IndexError:
                time2 = ['null']
        elif len(datalist) <= 5:
            try: 
                time3.append(datalist[4])
            except IndexError:
                time3 = ['null']
        elif len(datalist) <= 6:
            try: 
                time4.append(datalist[5])
            except IndexError:
                time4 = ['null']
        data = {'source_nm': source_nm,
                'fligh_nm': flight_nm,
                'time1': time1,
                'time2': time2,
                'time3': time3,
                'time4': time4}
        df = pd.dataframe(data)
        print df
    
            

            
            
                    
            
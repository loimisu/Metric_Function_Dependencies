# -*- coding: utf-8 -*-
import re
import numpy as np
import pandas as pd

if __name__ == '__main__':
    filepath="/home/hduser/git/Metric_Function_Dependencies/clean_flight/2011-12-01-data.txt"
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

    patRemove = re.compile(r'[ -]*(Contact|Not|Delay|On Time|&nbsp).*|[ ]*\(.*\).*$|^.*Term.*$')

    for aline in infile:
        data = filter(filter_input, aline.split('\t')) 
        # remove '\t' from the beginning and end of the string
        #if data[0] in ("aa", "ua"):
        data = map(lambda item: patRemove.sub('', item, re.IGNORECASE), data) 
        
        datalist = filter(lambda item: len(item) > 8, data[1:])
        datalist.insert(0,data[0])  
        datalist = map(lambda item: re.sub(r'([,]|( - )|[*])','', item), datalist)

        if len(datalist) == 3 and datalist[1] in ('AA-2059-DFW-SLC', 'UA-444-SFO-BOS', 'AA-3824-DEN-LAX'):
            n = 5 - len(datalist)
            if len(datalist) <= 5:
                datalist.extend(['null']*n)
                print datalist

# -*- coding: utf-8 -*-
import re
import numpy as np
import pandas as pd
import os


def main():
    file="/home/hduser/git/Metric_Function_Dependencies/clean_flight/2011-12-11-data.txt"
    #     path = "/home/hduser/git/Metric_Function_Dependencies/clean_flight"
    # for afile in os.listdir(path):
    #     if afile.endswith(".txt"):
    #         file = path + "/" + afile
    infile = open(file,"r")

    def filter_input(data):
        return len(data.strip()) # removes '\n' from the beginning and end of the string

    patRemove = re.compile(r'\b0(?=[0-9]:)|[ -]*(Contact|Not|Delay|On Time|&nbsp|HST|AKST|PST|MST|CST|EST|Sun|Sat|Mon|Tues|Tue|Wed|Thurs|Thur|Thu|Fri).*|[ ]*\(.*\).*$|^.*(Term|B32).*$', re.IGNORECASE)
    # remove string with ' - contact%' or 'not%' on item
    # remove string with 'delay%' or 'on time%' on item
    # remove stiing with with '&nbsp'
    # remove string with '(%%)' on item
    # remove string with '%Term%' on item and items for string start with 'Term%'
    # remove comma(,), dash with space( - ), star(*)
    # remove sting of USA Time Zone ('HST', 'AKST', 'PST', 'MST', 'CST' ,'EST')
    # remove days of week ('Sun','Sat','Mon'), no thers
    dataset = []
    for aline in infile:
        data = filter(filter_input, aline.split('\t')) 
        # remove '\t' from the beginning and end of the string
        if len(data[0]) >= 3: #and data[1] in ("AA-2098-ORD-BOS"):
            data = map(lambda item: patRemove.sub(' ', item).strip(), data[1:])
            data = filter(lambda item: len(item) > 4, data)

            # conver am/pm to hh:mm(24), substring time from datetime
            # Clearing up datalist and combine data[0]
            datetime = map(lambda item: (str(int(''.join(re.findall(r'(?=[0-9]:)\w', item)))+12) + ''.join(re.findall(r':(?=[0-9])\w*[ ]*\w', item))) if 'p' in str.lower(item) else item, data[1:])
            datalist = time = map(lambda item: ''.join(re.findall(r'[0-9]*:[0-9]*', item)).strip(), datetime)            
            datalist = filter(lambda item: len(item) > 4, datalist)
            datalist.insert(0,data[0]) 

            if len(datalist) >= 3:
                n = 5 - len(datalist)
                if len(datalist) <= 5:
                    datalist.extend(['']*n)
            #print datalist

            dataset.append(datalist)
            # for item in dataset:
            #     if len(item) <=2:
            #         dataset.remove(item)
    return dataset


if __name__ == "__main__":
    dataset = main()
    print dataset

############## export datalist to dataframe ##########################
    # flight_nm = []
    # time1 = []
    # time2 = []
    # time3 = []
    # time4 = []
    # time5 = []
    # for datalist in dataset:
    #     flight_nm.append(datalist[0])
    #     time1.append(datalist[1])
    #     time2.append(datalist[2])
    #     time3.append(datalist[3])
    #     time4.append(datalist[4])
    #             # if item index not exist, then set as 'null'   
      
    # data = {
    #         'flight_nm': flight_nm,
    #         'time1': time1,
    #         'time2': time2,
    #         'time3': time3,
    #         'time4': time4
    #         }

    # df = pd.DataFrame(data)
    # df.to_csv('/home/hduser/git/Metric_Function_Dependencies/output01.csv')
    # print "successully exported to csv!"



# ############## export datalist to txt file ##########################
# output_file = '/home/hduser/git/Metric_Function_Dependencies/clean_flight/test01.txt'
# with open(output_file, 'w') as f:
#     for item in datalist:
#         f.write(item + '\n')


# -*- coding: utf-8 -*-
# flightaware	AA-1518-DFW-SDF	2011-12-01 12:10PM CST	2011-12-01 12:18PM CST	 C20 	2011-12-01 02:46PM EST	2011-12-01 02:53PM EST	 A15 
# wunderground	AA-1518-DFW-SDF	2011-12-01 12:10PM CST	2011-12-01 12:18PM CST	 C20 	2011-12-01 02:46PM EST	2011-12-01 02:53PM EST	 A15

import numpy as np
import pandas as pd
from itertools import islice
from operator import itemgetter
from datetime import datetime


if __name__ == '__main__':
    filepath="/root/Documents/6720/clean_flight/2011-12-01-data.txt"
    infile = open(filepath,"r")
    #dataset = islice(infile, 21)
    
    def filter_input(data):
        return len(data.strip())
    
    #for aline in dataset:
    items_lens = []
    for aline in infile:
        data = filter(filter_input, aline.split('\t'))
        if data[0] in ("orbitz"):
            for item in data:
                if data.index(item) >= 2:
                    item_lens = str(len(item))
                    if item_lens not in items_lens:
                        items_lens.append(item_lens)
    print items_lens
            
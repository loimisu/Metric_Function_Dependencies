from qhull_polygon_centroid import centroid_of_polygon
from qhull_polygon_points import qhull_polygon_pts, time_pts
#from mf_diff_init import mf_pair
from scipy import spatial
from itertools import groupby
import numpy as np

# input_file = '/home/hduser/git/Metric_Function_Dependencies/output01.csv'

####### convert numeric to time_str ############
def time_to_str(time_num):
  if time_num == 0:
    return ''
  else:
    hh = str(time_num/60) 
    mm = str(time_num%60) 
    return (hh+':'+mm)

mf_pair_num =  [['AA-1007-TPA-MIA', 835, 900], 
                ['AA-1007-TPA-MIA', 835, 896], 
                ['AA-2098-ORD-BOS', 920, 1110], 
                ['AA-2098-ORD-BOS', 920, 1117], 
                ['AA-2098-ORD-BOS', 938, 1117],
                ['AA-2099-ORD-BOS', 920, 1110], 
                ['AA-2099-ORD-BOS', 920, 1117], 
                ['AA-2099-ORD-BOS', 938, 1117],
                ]


# ####### import data - mf_pair_num ############
# mf_pair_num = mf_pair(input_file)
# print mf_pair_num

mf_pair_grouped = [list(v) for l,v in groupby(sorted(mf_pair_num, key=lambda x:x[0]), lambda x: x[0])]
qhull_polygon = []
time_array = []
for agroup in mf_pair_grouped:
    if len(agroup) > 2:
        ######## get the qhull polygon points and time array ###########
        qhull_polygon.append(qhull_polygon_pts(agroup))
        time_array.append(time_pts(agroup))

flight_time = []
theta = []
for a_flight in qhull_polygon:
    header = a_flight[0]
    qhull_pts = a_flight[1:]
    #print qhull_pts
    cent = list(centroid_of_polygon(qhull_pts))
    centroid = map(lambda item: round(item, 1), cent)
    # print centroid
    ######## get nearest time point of a flight ###########
    x = []
    y = []
    for apair_num in a_flight[1:]:
        x.append(apair_num[0])
        y.append(apair_num[1])
    time_array = np.column_stack((x,y))
    # print time_array
    nearest_time_pts = time_array[spatial.KDTree(time_array).query(centroid)[1]]
    distance,index = spatial.KDTree(time_array).query(centroid)
    theta.append(round(distance,1))
    ######## generate repsentive value with metric distance ###########
    nearest_time_num = nearest_time_pts.tolist()
    nearest_time = map(lambda item: time_to_str(item), nearest_time_num)
    nearest_time.insert(0, header)
    flight_time.append(nearest_time)
    flight_time_rep = zip(flight_time, theta)
print flight_time_rep


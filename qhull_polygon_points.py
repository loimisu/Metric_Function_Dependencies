from scipy.spatial import distance
from scipy.spatial import ConvexHull
import numpy as np
import matplotlib.pyplot as plt
from itertools import groupby
from shapely.geometry import Polygon
import itertools


 



def time_pts(agroup):
    #time_points_set = []
    ###### conver to matrix ############
    x = []
    y = []
    header = []
    for apair_num in agroup:
        head = apair_num[0]
        if head not in header:
            header.append(head)
        x.append(apair_num[1])
        y.append(apair_num[2])
    time_points = np.column_stack((x,y))
    points = time_points.tolist()
    points.insert(0,header[0])
    time_points_set = points
    #time_points_set.append(points)
    return time_points_set

def qhull_polygon_pts(agroup):
    ########### Qhull_Polygon Boundary Points #############
    #qhull_polygon_pts = []
    ###### conver to matrix ############
    m = []
    n = []
    header = []
    for apair_num in agroup:
        head = apair_num[0]
        if head not in header:
            header.append(head)
        m.append(float(apair_num[1])/1500)
        n.append(float(apair_num[2])/1500)
    pts = np.column_stack((m,n))
    #print pts
    ch = ConvexHull(pts)
    ###### PERFORM CONVEX HULL ######
    hull = ConvexHull(pts)
    # hull_indices = ch.vertices   # This will work in the scipy 0.13
    hull_indices = np.unique(ch.simplices.flat)
    hull_pts = pts[hull_indices, :]
    points = hull_pts.tolist()
    polygon_points = []
    for a_time_pair in points:
        points = map(lambda item: int(item*1500), a_time_pair)
        polygon_points.append(points)
    polygon_points.insert(0,header[0])
    #qhull_polygon_pts.append(polygon_points)
    qhull_polygon_pts = polygon_points
    return qhull_polygon_pts

# agroup =  [ 
#                 ['AA-2098-ORD-BOS', 920, 1110], 
#                 ['AA-2098-ORD-BOS', 920, 1117],
#                 ['AA-2098-ORD-BOS', 938, 1117],
#                 ['AA-2098-ORD-BOS', 938, 1113],
#                 ['AA-2098-ORD-BOS', 920, 1090],
#                 ['AA-2098-ORD-BOS', 938, 1111],
#                 ['AA-2098-ORD-BOS', 920, 1118],
#                 ['AA-2098-ORD-BOS', 938, 1110],
#                 ['AA-2098-ORD-BOS', 935, 1113],
#                 ['AA-2098-ORD-BOS', 927, 1112],
#                 ['AA-2098-ORD-BOS', 925, 1111],
#                 ['AA-2098-ORD-BOS', 929, 1118],
#                 ['AA-2098-ORD-BOS', 928, 1103],
#                 ['AA-2098-ORD-BOS', 933, 1190],
#                 ['AA-2098-ORD-BOS', 936, 1199],
#                 ['AA-2098-ORD-BOS', 934, 1111],
#                 ]
# print qhull_polygon_pts(agroup)


# plt.plot(pts[:, 0], pts[:, 1], 'ko', markersize=10)
# plt.fill(hull_pts[:,0], hull_pts[:,1], fill=False, edgecolor='ro')
# plt.xlim(915, 1)
# plt.ylim(0, 1)
# plt.show()
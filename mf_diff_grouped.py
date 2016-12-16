import mf_diff_init as mf
from pandas import DataFrame
import pandas as pd

def main():
    input_file = '/home/hduser/git/Metric_Function_Dependencies/output01.csv'
    fields = ['flight_nm', 'diff']
    df = pd.read_csv(input_file, usecols=fields)

    ########## Apply diff to list by the group of flight_nm ##########
    df = df.groupby('flight_nm')['diff'].apply(list)
    header = df.index.tolist()

    ########## get the most frequent diff ##########
    diff_set = df.values.tolist()
    mf_diff_set = []
    for item in diff_set:
        mf_diff = mf.mf_durations(item)
        mf_diff_set.append(mf_diff)

    ########## zip mf_diff with header ##########    
    mf_diff = zip(header,mf_diff_set)
    return mf_diff

if __name__ == "__main__":
  mf_diff = main()
  print mf_diff


# with open(input_file, "r") as file:
#     reader = csv.reader(file)
#     for idx,line in enumerate(reader):
#         if idx>0:
#            t=line[1:5]
#            print t

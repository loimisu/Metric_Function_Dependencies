import get_duration
from pandas import DataFrame
import pandas as pd

dataset_due = get_duration.main()

output_file = '/home/hduser/git/Metric_Function_Dependencies/output01.csv'
############# export datalist to dataframe ##########################
flight_nm = []
depart_ts = []
arrival_ts = []
diff = []
for datalist in dataset_due:
    flight_nm.append(datalist[0])
    depart_ts.append(datalist[1])
    arrival_ts.append(datalist[2])
    diff.append(datalist[3])
            # if item index not exist, then set as 'null'   
  
data = {
        'flight_nm': flight_nm,
        'depart_ts': depart_ts,
        'arrival_ts': arrival_ts,
        'diff': diff
        }

df = pd.DataFrame(data)
df = df[['flight_nm', 'depart_ts', 'arrival_ts','diff']]
############## sort by duration and group by flight_nm #################
grp = df.groupby('flight_nm')
grp[['diff']].transform(sum).sort('diff')
df = df.ix[grp[['diff']].transform(sum).sort('diff').index]
print df
# f = lambda x: x.sort('B', ascending=False)
# sort2 = sort1.groupby('A', sort=False).apply(f)
# print sort2
# final_sort = sort2.reset_index(0, drop=True)
# print final_sort


df.to_csv(output_file)
print "successully exported to csv!"
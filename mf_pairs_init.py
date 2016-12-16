import mf_diff_grouped
import pandas as pd


###### convert time_str to numeric ############
def time_to_num(time_str):
  if time_str == '':
    return 0
  else:
    hh, mm = map(int, time_str.split(':'))
    return (mm + 60*hh)

def mf_pair(input_file):
	# input_file = '/home/hduser/git/Metric_Function_Dependencies/output01.csv'
	fields = ['flight_nm', 'depart_ts', 'arrival_ts','diff']
	df = pd.read_csv(input_file, usecols=fields)
	dataset = map(list, df.values)

	mf_diff_set = mf_diff_grouped.main()

	mf_dataset = []
	for datalist in dataset:
		for mf_diff in mf_diff_set:
			if datalist[0] == mf_diff[0] and datalist[3] in mf_diff[1]:
				mf_dataset.append(datalist)

	mf_pair = []
	for x in mf_dataset:
		if x not in mf_pair:
			mf_pair.append(x)

	mf_pair_num = []
	for apair in mf_pair:
		zip(*mf_pair)
		header = apair[0]
		apair_num = map(lambda item: time_to_num(item), apair[1:3])
		apair_num.insert(0, header)
		mf_pair_num.append(apair_num)
	return mf_pair_num


input_file = '/home/hduser/git/Metric_Function_Dependencies/output01.csv'
print mf_pair(input_file)


# mf_dataset = []
# for datalist in dataset_due:
# 	if datalist[3] in mf_diff:
# 		mf_dataset.append(datalist)
# #print mf_dataset

# mf_pair = []
# for x in mf_dataset:
# 	if x not in mf_pair:
# 		mf_pair.append(x)
# print mf_pair

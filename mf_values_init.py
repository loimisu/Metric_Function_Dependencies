import numpy as np
import scipy as sp
import scipy.stats
from kmeansd1 import ckmeans

X = [190,175,175,175,175,175,170,170,197,197,197,190,
	 190,179,179,179,179,179,173,190,190,170,197,190,
	 172,152,190,172,152,190,197,197,190,197,197,190,
	 197,197,190,197,172,152,190]

def mf_durations(dataset):
	# confidence interval of Gaussian Distribution
	def GCI_values(dataset,confidence=0.95):
		n = len(dataset)
		m, se = np.mean(dataset), scipy.stats.sem(dataset)
		h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
		GCI_MIN = int(m-h)+1 
		GCI_MAX = int(m+h) # use integer space instead fload
		GCI_values = []
		for item in dataset:
			if item>=GCI_MIN and item<=GCI_MAX and item not in GCI_values:
			        GCI_values.append(item)
		return GCI_values

	# This function is to get the most frequent values which clustering by ckmeans
	def ckmeans_mf_values(dataset): 
		mf_values = [] #most frequent values
		dataset = map(lambda item: float(item)/100, dataset)
		clusters = ckmeans(dataset, 3)
		mf_set= max(clusters, key=len) # most frequent set
		for x in mf_set:
		    if x not in mf_values:
		        mf_values.append(x) #get the distinct values from mf_set
		mf_values = map(lambda item: int(item*100), mf_values)
		return mf_values

	return list(set(GCI_values(dataset)) | set(ckmeans_mf_values(dataset)))

print mf_durations(X)



import parse_raw_data

####### convert time_str to numeric ############
def time_to_num(time_str):
  if time_str == '':
    return 0
  else:
    hh, mm = map(int, time_str.split(':'))
    return (mm + 60*hh)

####### convert numeric to time_str ############
def time_to_str(time_num):
  if time_num == 0:
    return ''
  else:
    hh = str(time_num/60) 
    mm = str(time_num%60) 
    return (hh+':'+mm)

def main():
  ###### import dataset from parse_raw_data ########
  dataset = parse_raw_data.main()

  dataset_all = []
  dataset_new = []
  dataset1 = []
  dataset2 = []
  dataset3 = []
  dataset4 = []


  for datalist in dataset:
    zip(*datalist)
      #print datalist
    if len(datalist) >2:
      header = (datalist[0])
      ####### Shift positon if data[1] < data[2] ############
      time_num = map(lambda item: time_to_num(item), datalist[1:])
      if time_num[1] < time_num[2]: 
        time = time_num
      else: 
        time = [time_num[0],time_num[2],time_num[1],time_num[3]]
      #data = map(lambda item: time_to_str(item), time) 
      time.insert(0, header)
      data = time
      ###### Depart/Arrive time Combinations and Duration #######
      if data[4] == 0 and data[2] != 0:
        data1 = [data[i] for i in [1,3]]
        data1.insert(0, data[0])
        #data1.insert(3,abs(data1[2]-data1[1]))
        data2 = [data[i] for i in [2,3]]
        data2.insert(0, data[0])
        #data2.insert(3,abs(data2[2]-data2[1]))
        dataset1.append(data1)
        dataset2.append(data2)
      elif data[2] == 0 and data[4] == 0: 
        data1 = [data[i] for i in [1,3]]
        data1.insert(0, data[0])
        #data1.insert(3,abs(data1[2]-data1[1]))
        dataset1.append(data1)
      else:
        data1 = [data[i] for i in [1,3]]
        data1.insert(0, data[0])
        #data1.insert(3,abs(data1[2]-data1[1]))
        data2 = [data[i] for i in [2,3]]
        data2.insert(0, data[0])
        #data2.insert(3,abs(data2[2]-data2[1]))
        data3 = [data[i] for i in [1,4]]
        data3.insert(0, data[0])
        #data3.insert(3,abs(data3[2]-data3[1]))
        data4 = [data[i] for i in [2,4]]
        data4.insert(0, data[0])
        #data4.insert(3,abs(data4[2]-data4[1]))
        dataset1.append(data1)
        dataset2.append(data2)
        dataset3.append(data3)
        dataset4.append(data4)
  # print "dataset1 is %s" % dataset1
  # print "dataset2 is %s" % dataset2
  # print "dataset3 is %s" % dataset3
  # print "dataset4 is %s" % dataset4
  dataset_all = dataset1 + dataset2 + dataset3 + dataset4
  for datalist in dataset_all:
    if datalist[1] < datalist[2]: 
       dataset_item = datalist
    else: 
      dataset_item = [datalist[0],datalist[2],datalist[1]]
    dataset_item.insert(3,abs(datalist[2]-datalist[1]))
    dataset_new.append(dataset_item)

    dataset_due = []
    for datalist in dataset_new:
      datalist_new = map(lambda item: time_to_str(item) if item in datalist[1:3] else item, datalist)
      dataset_due.append(datalist_new)
      dataset_due = filter(lambda datalist: datalist[3] > 30, dataset_due)
  return dataset_due


if __name__ == "__main__":
  dataset_due = main()
  print dataset_due





####### Depart/Arrive time Combinations and Duration #############
# a = sorted([1,4,2,6])
# newlist = [(j-i) for i in a for j in a if i != j and (j-i)>0]
# print a
# print newlist


     
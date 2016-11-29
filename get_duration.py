import parse_raw_data

datalist = parse_raw_data.main()
header = datalist[0]

datalist = ['AA-2098-ORD-BOS', '15:20', '15:27', '18:30', '18:33']

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

####### Shift positon if data[1] > data[2] ############
data = map(lambda item: time_to_num(item), datalist[1:])
if data[1] > data[2]: 
  data = [data[0],data[2],data[1],data[3]]
else: 
  data = data
  data = map(lambda item: time_to_str(item), data)
  print data
  
####### Depart/Arrive time combinations #############
  for i in (2,3):
    data1 = [data[i] for i in [0,2]]
    data2 = [data[i] for i in [1,2]]
    data3 = [data[i] for i in [0,3]]
    data4 = [data[i] for i in [1,3]]
    data1.insert(2,time_to_num(data1[1])-time_to_num(data1[0]))
    print data1
    if len(data2[0])>0:
      data2.insert(2,time_to_num(data2[1])-time_to_num(data2[0]))
      print data2 
    if len(data3[1])>0:
      data3.insert(2,time_to_num(data3[1])-time_to_num(data3[0]))
      print data3
    if len(data4[1])>0:
      data4.insert(2,time_to_num(data4[1])-time_to_num(data4[0]))
      print data4




  # data.insert(0, header)
  # datalist = data
  # print datalist



  # diff1 = data[2]-data[0]
  # diff2 = data[2]-data[1]
  # diff3 = data[3]-data[0]
  # diff4 = data[3]-data[1]

  # if data[1] == 0 and data[3] == 0:
  #   diff = [diff1,
  #           0,
  #           0,
  #           0]
  # elif data[3] == 0:
  #   diff = [diff1, 
  #           diff2,
  #           0,
  #           0] 
  # else:
  #   diff = [diff1, 
  #           diff2,
  #           diff3,
  #           diff4] 
  # #print diff
  # diff.insert(0,header)
  # print diff
  
  # for item in diff[1:]:
  #   if item  in (190, 172):
  #     print item



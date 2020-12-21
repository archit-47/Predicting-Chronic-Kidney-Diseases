import csv
import matplotlib.pyplot as plt
zero=0
one=0
two=0
three=0
four=0
five=0
nzero=0
none=0
ntwo=0
nthree=0
nfour=0
nfive=0

with open('idsfinal.csv',mode='r') as csv_file:
 csv_reader=csv.DictReader(csv_file)

 mydata=[]
 xdata=[0,1,2,3,4,5]
 for row in csv_reader:
  if row["su"]=="0":
   zero=zero+1
  elif row["su"]=="1":
   one=one+1
  elif row["su"]=="2":
   two=two+1
  elif row["su"]=="3":
   three=three+1
  elif row["su"]=="4":
   four=four+1
  elif row["su"]=="5":
   five=five+1
  
mydata.append(zero)
mydata.append(one)
mydata.append(two)
mydata.append(three)
mydata.append(four)
mydata.append(five)

plt.bar(xdata, mydata, color ='maroon', width = 0.4) 
plt.xlabel("Sugar level")
plt.ylabel("No of people with chronic kidney disease")
plt.title("Sugar level distribution")
plt.show()


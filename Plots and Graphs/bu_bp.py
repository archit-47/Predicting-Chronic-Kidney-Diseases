import csv
import matplotlib.pyplot as plt


with open('idsfinal.csv',mode='r') as csv_file:
 csv_reader=csv.DictReader(csv_file)
 mydata=[]
 for row in csv_reader:
  mydata.append(float(row["bu"]))
  
plt.boxplot(mydata) 
plt.ylabel("Blood urea")
plt.title("Blood urea distribution")
plt.show()


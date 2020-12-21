import csv
import matplotlib.pyplot as plt


with open('idsfinal.csv',mode='r') as csv_file:
 csv_reader=csv.DictReader(csv_file)
 mydata=[]
 for row in csv_reader:
  mydata.append(float(row["sc"]))
  
plt.boxplot(mydata) 
plt.ylabel("serum creatinine")
plt.title("serum creatinine distribution")
plt.show()


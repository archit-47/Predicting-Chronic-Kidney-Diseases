import csv
import matplotlib.pyplot as plt

ages=[]

with open('preprocessed.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        if line[0]=="NA":
            next(csv_reader)
        else:
            ages.append(int(line[0]))

range = (0,100)
bins=10

plt.hist(ages, bins, range, color = '#3fbf4f', histtype = 'bar', edgecolor='black') 
plt.xlabel('Ages') 
plt.ylabel('No. of people') 
plt.title('Age Distribution') 

plt.show()
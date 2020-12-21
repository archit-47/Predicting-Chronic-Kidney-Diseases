import csv
import matplotlib.pyplot as plt

volume=[]

with open('preprocessed.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        if line[15]=="NA":
            next(csv_reader)
        else:
            volume.append(int(line[15]))

range = (0,60)
bins=6

plt.hist(volume, bins, range, color = 'maroon', histtype = 'bar', edgecolor='black') 
plt.xlabel('Packed Cell Volume(%)') 
plt.ylabel('No. of people') 
plt.title('Packed Cell Volume Distribution') 

plt.show()
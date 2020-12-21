import csv
import matplotlib.pyplot as plt

good=0
poor=0


with open('chronic_kidney_disease.csv',mode='r') as csv_file:
	csv_reader=csv.DictReader(csv_file)
	line_count=0
	for row in csv_reader:
		if row["appet"]=="good":
			good = good + 1
		elif row["appet"]=="poor":
			poor = poor + 1

condition=['Good appetite','Poor appetite']
values=[good,poor]
colors=['#ff9900','#ff1a1a']

plt.pie(values, labels = condition, colors=colors,startangle=90, shadow = True, radius = 1.2, autopct = '%1.1f%%') 
plt.legend() 
plt.title("Appetite",pad=23)
plt.show()



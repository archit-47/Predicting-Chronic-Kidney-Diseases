import csv
import matplotlib.pyplot as plt

yes=0
no=0


with open('chronic_kidney_disease.csv',mode='r') as csv_file:
	csv_reader=csv.DictReader(csv_file)
	line_count=0
	for row in csv_reader:
		if row["pe"]=="yes":
			yes = yes + 1
		elif row["pe"]=="no":
			no = no + 1

condition=['Pedal Edema','No Pedal Edema']
values=[yes,no]
colors=['#ff9900','#ff1a1a']

plt.pie(values, labels = condition, colors=colors,startangle=90, shadow = True, radius = 1.2, autopct = '%1.1f%%') 
plt.legend() 
plt.title("Suffering from Pedal Edema",pad=23)
plt.show()



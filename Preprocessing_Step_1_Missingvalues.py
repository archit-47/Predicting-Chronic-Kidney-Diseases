import csv

columns=['age','bp','sg','al','su','rbc','pc','pcc','ba','bgr','bu','sc','sod','pot','hemo','pcv','wbcc',
			'rbcc','htn','dm','cad','appet','pe','ane','class']

countmissing={}

for attrib in columns:
	countmissing[attrib]=0
	with open('chronic_kidney_disease_full.csv',mode='r') as csv_file:
		csv_reader=csv.DictReader(csv_file)
		for row in csv_reader:
			if row[attrib]=="?":
				countmissing[attrib]=countmissing[attrib]+1
print("Missing values are : ")
for attrib in columns:
	print(attrib+" : "+str(countmissing[attrib]/400))
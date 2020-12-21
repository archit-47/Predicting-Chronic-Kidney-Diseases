import csv

columns=['age','bp','sg','al','su','rbc','pc','pcc','ba','bgr','bu','sc','sod','pot','hemo','pcv','wbcc',
			'rbcc','htn','dm','cad','appet','pe','ane','class']

writerows=[]

with open('preprocessed.csv',mode='r') as csv_file:
	csv_reader=csv.DictReader(csv_file)
	for row in csv_reader:
		for attrib in columns:
			if row[attrib]=="normal" or row[attrib]=="present" :
				row[attrib]=1
			elif   row[attrib]=="yes" or  row[attrib]=="good" or row[attrib]=="ckd":
				row[attrib]=1
			elif (row[attrib]=="abnormal" or row[attrib]=="notpresent" ):
				row[attrib]=0
			elif row[attrib]=="no" or  row[attrib]=="poor" or row[attrib]=="notckd":
				row[attrib]=0
		writerows.append(row)

with open('labelencoded.csv',mode='w',newline='') as csv_file:
	writer=csv.DictWriter(csv_file,columns)
	writer.writeheader()
	for row in writerows:
		try:
			writer.writerow(row)
		except:
			print(row)


import csv
columns=['age','bp','sg','al','su','rbc','pc','pcc','ba','bgr','bu','sc','sod','pot',
			'hemo','pcv','wbcc','rbcc','htn','dm','cad','appet','pe','ane','class']
ckd={}
nckd={}

with open('completedata.csv',mode='r') as csv_file:
	csv_reader=csv.DictReader(csv_file)
	linecount=0
	for row in csv_reader:
		if linecount==0:
			ckd=row
		else:
			nckd=row
		linecount=linecount+1

ckd["age"]=str(round(float(ckd["age"])))
ckd["bp"]=str(round(float(ckd["bp"])))
ckd["al"]=str(round(float(ckd["al"])))
ckd["su"]=str(round(float(ckd["su"])))
ckd["bgr"]=str(round(float(ckd["bgr"])))
ckd["bu"]=str(round(float(ckd["bu"])))
ckd["pcv"]=str(round(float(ckd["pcv"])))
ckd["wbcc"]=str(round(float(ckd["wbcc"])))
ckd["sod"]=str(round(float(ckd["sod"])))

nckd["age"]=str(round(float(nckd["age"])))
nckd["bp"]=str(round(float(nckd["bp"])))
nckd["al"]=str(round(float(nckd["al"])))
nckd["su"]=str(round(float(nckd["su"])))
nckd["bgr"]=str(round(float(nckd["bgr"])))
nckd["bu"]=str(round(float(nckd["bu"])))
nckd["pcv"]=str(round(float(nckd["pcv"])))
nckd["wbcc"]=str(round(float(nckd["wbcc"])))
nckd["sod"]=str(round(float(nckd["sod"])))

print(ckd)
print(nckd)
writelist=[]

with open('chronic_kidney_disease_full.csv',mode='r') as csv_file:
	csv_reader=csv.DictReader(csv_file)
	for row in csv_reader:
		for attrib in columns:
			if (row[attrib]=="?"):
				if(row["class"]=="ckd"):
					row[attrib]=ckd[attrib]
				else:
					row[attrib]=nckd[attrib]
			else:
				continue
		writelist.append(row)

with open('preprocessed.csv',mode='w',newline='') as csv_file:
	writer=csv.DictWriter(csv_file,columns)
	writer.writeheader()
	for row in writelist:
		try:
			writer.writerow(row)
		except:
			print(row)

import csv
import math
import statistics

columns=['age','bp','sg','al','su','rbc','pc','pcc','ba','bgr','bu','sc','sod',
			'pot','hemo','pcv','wbcc','rbcc','htn','dm','cad','appet','pe','ane','class']
isnumeric=[1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0]

colmeanckd=[]
colmeannckd=[]

i=0
for attrib in columns:
	listckd=[]
	listnckd=[]
	with open('chronic_kidney_disease_full.csv',mode='r') as csv_file:
		csv_reader=csv.DictReader(csv_file)
		line_count=0
		for row in csv_reader:
			if(row[attrib]=='?'):
				continue
			elif (row["class"]=="ckd"):
				listckd.append(row[attrib])
			else:
				listnckd.append(row[attrib])
	newlistckd=[]
	newlistnckd=[]
	if(isnumeric[i]):
		for j in listckd:
			try:
				newlistckd.append(float(j))
			except:
				print(j+attrib)
		for j in listnckd:
			try:
				newlistnckd.append(float(j))
			except:
				print(j+attrib)
		if(attrib=="sg" or attrib=="al" or attrib=="su"):
			print("ckd : "+attrib+" mode is : "+str(statistics.mode(newlistckd)))
			print("notckd : "+attrib+" mode is : "+str(statistics.mode(newlistnckd))+"\n")
			colmeanckd.append(statistics.mode(newlistckd))
			colmeannckd.append(statistics.mode(newlistnckd))
		elif(attrib=="bgr" or attrib=="bu" or attrib=="sc"):
			print("ckd : "+attrib+" median is : "+str(statistics.median(newlistckd)))
			print("notckd : "+attrib+" median is : "+str(statistics.median(newlistnckd)))
			colmeanckd.append(statistics.median(newlistckd))
			colmeannckd.append(statistics.median(newlistnckd))
			stddev=newlistckd+newlistnckd
			print("Mean and Variance of "+attrib+" is : "+ str(statistics.mean(stddev))+", "+str(math.sqrt(statistics.variance(stddev)))+"\n")
		else:	
			print("ckd : "+attrib+" mean is : "+str(statistics.mean(newlistckd)))
			colmeanckd.append('%.2f'%statistics.mean(newlistckd))
			print("notckd : "+attrib+" mean is : "+str(statistics.mean(newlistnckd)))
			colmeannckd.append('%.2f'%statistics.mean(newlistnckd))
			stddev=newlistckd+newlistnckd
			print("Mean and Variance of "+attrib+" is : "+ str(statistics.mean(stddev))+", "+str(math.sqrt(statistics.variance(stddev)))+"\n")
	else:
		print("ckd : "+attrib+" mode is : "+str(statistics.mode(listckd)))
		colmeanckd.append(statistics.mode(listckd))
		print("notckd : "+attrib+" mode is : "+str(statistics.mode(listnckd))+"\n")
		colmeannckd.append(statistics.mode(listnckd))
	i=i+1

with open("completedata.csv",'w') as csv_file:
	csvwriter=csv.writer(csv_file)
	csvwriter.writerow(columns)
	csvwriter.writerow(colmeanckd)
	csvwriter.writerow(colmeannckd)
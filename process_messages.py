
'''
f=open('messages-sample.txt')
content=f.read()

messages=[]
for line in content.split("\n"):
	messages.append(line.split("\t"))


f1=open('demo-1.txt','w')
for i in range(len(messages)):
	print("===================")
	if(i>10):
		previous=""
		for m in messages[i-10:i]:
			previous=previous+":::"+str(";".join(m))
		#print(previous.split(":::")[1:])
		#previous_message=previous+":::::"
		true_message= ";".join(messages[i])
		f1.write(str(i-10)+"\t"+"dfs"+"\t"+"sdf"+"\t"+"xvvv"+"\t"+"xvvv"+"\t"+previous+"\t"+true_message+"\t"+str("N")+"\t"+str("N"	)+"\t"+str("IMIP")+"\n")

'''
import mysql.connector

mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Ishani@340",
            port = 3306,
            database='HIV_Africa')


import pandas as pd
df=pd.read_csv('demo-1.txt', delimiter='\t')

for i in range(20):
	mycursor = mydb.cursor()
	sql = "DELETE From Messages where PairId = "+str(i)
	mycursor.execute(sql)
	mydb.commit()
	mycursor.close()


for index, row in df.iterrows():
	mycursor = mydb.cursor()
	sql = "INSERT INTO Messages (PairId, S_PostId, R_PostId, S_UserId, R_UserId, S_Content, R_Content, Sentiment, annotation_status, Category) VALUES (%s, %s, %s, %s, %s, %s, %s , %s, %s, %s)"
	print(index+1, row['scontent'])
	print("---------------------------------")
	for elem in row['scontent'].split(":::"):
		print(elem)
	print("---------------------------------")
	print(row['rcontent'])
	#print(index+1,  row['s1'], row['r1'], row['s2'], row['r2'], row['scontent'], row['rcontent'], row['sentiment'],  row['annotation'], row['category'])
	val = (index+1,  row['s1'], row['r1'], row['s2'], row['r2'], row['scontent'], row['rcontent'], row['sentiment'],  row['annotation'], row['category'])
	mycursor.execute(sql, val)
	mydb.commit()
	mycursor.close()

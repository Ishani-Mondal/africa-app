from __future__ import print_function
import os
import codecs
import sys

import mysql.connector
from datetime import datetime


database_name = sys.argv[1] #"content_annotation_mh_sub_cat"


mydb = mysql.connector.connect(
	host="52.187.63.154",
	user="ashish",
	passwd="me_health@2019",
	port = 3306,
	database=database_name
)

mycursor = mydb.cursor()

# Destination Folder
curr_date = datetime.today().strftime('%d-%m')

if not os.path.exists('Dump-' + curr_date + '/' + database_name):
	os.makedirs('Dump-' + curr_date + '/' + database_name)

destpath = 'Dump-' + curr_date + '/' + database_name + '/'

print(database_name, 'Dataset Dumping Started....')

# Tables - Posts, Post_Characteristics, Support_Characteristics, Highlight, SkipReason

# Posts
mycursor.execute("Select * From Posts")
myresult = mycursor.fetchall()

posts_file = codecs.open(destpath+'Posts.txt', 'w', 'utf-8')

for elem in myresult:
	print(elem, file = posts_file) 

posts_file.close()

# Post_Characteristics
mycursor.execute("Select * From Post_Characteristics")
myresult = mycursor.fetchall()

post_characteristics_file = codecs.open(destpath+'Post_Characteristics.txt', 'w', 'utf-8')

for elem in myresult:
	print(elem, file = post_characteristics_file)

post_characteristics_file.close()

# Support_Characteristics
mycursor.execute("Select * From Support_Characteristics")
myresult = mycursor.fetchall()

support_characteristics_file = codecs.open(destpath+'Support_Characteristics.txt', 'w', 'utf-8')

for elem in myresult:
	print(elem, file = support_characteristics_file)

support_characteristics_file.close()

# Highlight
mycursor.execute("Select * From Highlight")
myresult = mycursor.fetchall()

highlight_file = codecs.open(destpath+'Highlight.txt', 'w', 'utf-8')

for elem in myresult:
	print(elem, file = highlight_file)

highlight_file.close()

# Skip Reason
mycursor.execute("Select * From SkipReason")
myresult = mycursor.fetchall()

skip_reason_file = codecs.open(destpath+'SkipReason.txt', 'w', 'utf-8')

for elem in myresult:
	print(elem, file = skip_reason_file)

skip_reason_file.close()

print(database_name, 'Dataset Dumped Successfully!')

mycursor.close()
import time
import re
import csv
import getopt
import sys
from sys import argv
import random


def upload_data(profile) :
	items = ['south indian', 'north indian', 'bridal', 'western']
	rand_item = random.choice(items)
	print rand_item
	print profile
	filename ="C:\Users\Aravind\Desktop\profiles\\" + profile + "\\" + profile +"_profile.txt"
	fd = open(filename, "a")
	fd.write("\ncategory: " +rand_item)
	fd.close


var = ""
csv_dict = dict()

#print "-------------------------------\n"

with open('C:/Users/Aravind/Desktop/profile1.csv', 'rb') as f:
     reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
     for row in reader:
         csv_dict[re.sub(r'\s',"",row[0])] = re.sub(r'\n',"",row[1])



print csv_dict
if len(sys.argv) == 3 :
	script, first, second= argv
	print "the script is " , script

	starting_number = int (float(first))
	print "the starting_number is " ,starting_number

	print type(starting_number)

	ending_number = int (float(second))
#print var1
	print "the ending_number is " ,ending_number

	ending_number += 1
	print ending_number

for x in range(starting_number,ending_number):
	y = str(x)
	#print type(y)
	#print "y is" + y
	print csv_dict[y]
	#print profile2['x']
	upload_data(csv_dict[y])
	

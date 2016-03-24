from selenium import webdriver
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import re
import csv
import getopt
import sys
from sys import argv
import os



def upload_data(profile) :

	print "profile1: " ,profile
	filename =os.path.expanduser("~/Desktop/zedlope-testing/profiles/" + profile + "/" + profile +"_profile.txt")
	image = os.path.expanduser("~/Desktop/zedlope-testing/profiles/" + profile + "/2.jpg")
	image1 = os.path.expanduser("~/Desktop/zedlope-testing/profiles/" + profile + "/1.jpg")
	image2 = os.path.expanduser("~/Desktop/zedlope-testing/profiles/" + profile + "/3.jpg")
	image3 = os.path.expanduser("~/Desktop/zedlope-testing/profiles/" + profile + "/4.jpg")
	file = open(filename , "r")
	data = file.read().rstrip("\n")
	var = re.sub(r'\n',":",data)
	print "varrrr:",var
	data1 = re.sub(r'\s',"",var)
	print "data1:",data1
	sri = data1.split(":")
	print "sri:",sri
	profile = dict()
	print "profile:",profile
	for i in range (len(sri)):
  		if i % 2 == 0:
  			profile[sri[i]] = sri[i+1]
  	print "profile:",profile
  	driver = webdriver.Firefox()
	driver.get('http://52.7.237.110/authenticate')
	driver.find_element_by_name("txt_username").send_keys("manoj")
	driver.find_element_by_name("txt_password").send_keys("manrox")
	driver.find_element_by_name("btn_login").click()
	#driver.implicitly_wait(30)

	driver.find_element_by_name("Fname").send_keys(" " , profile['firstname'])
	driver.find_element_by_name("Lname").send_keys(" " , profile['lastname'])
	driver.find_element_by_name("Mname").send_keys(" " , profile['mname'])
	driver.find_element_by_name("country").send_keys(" " , profile['country'])
	driver.find_element_by_name("state").send_keys(" " , profile['state'])
	driver.find_element_by_name("city").send_keys(" " , profile['city'])
	driver.find_element_by_name("webname").send_keys(" " , profile['website'])
	#driver.implicitly_wait(30)
	
	driver.find_element_by_link_text('Submit').send_keys("\n")
	driver.implicitly_wait(100)
	driver.find_element_by_name('userfile').send_keys(image)
	driver.implicitly_wait(100)
	
	print "IMAGE PATH: " ,image

	driver.find_element_by_link_text("professional").click()
	
	categoryvalue = profile['category']
	print categoryvalue
	if(categoryvalue == "south indian"):
		driver.find_element(By.XPATH,"//input[@name='category[]'][@value='south indian']").click;
	elif(categoryvalue == "north indian"):
		driver.find_element(By.XPATH,"//input[@name='category[]'][@value='north indian']").click;
	elif(categoryvalue == "western"):
		driver.find_element(By.XPATH,"//input[@name='category[]'][@value='western']").click();
	else:
		driver.find_element(By.XPATH,"//input[@name='category[]'][@value='bridal']").click();
		
	# driver.implicitly_wait(30)
	# driver.find_element_by_name("piercing").send_keys(" " , profile['Piercings'])
	# driver.find_element_by_name("compensation").send_keys(" " ,profile['Compensation'])
	# driver.find_element_by_name("generes").send_keys(" " ,profile['Genres'])
	# driver.find_element_by_name("about").send_keys(" " ,profile['about'])

	driver.implicitly_wait(30)
	
	driver.find_element_by_link_text("Profile").click()
	driver.find_element_by_name("gender").send_keys("" ,profile['gender'])
	driver.find_element_by_name("age").send_keys("" ,profile['Age'])
	driver.find_element_by_name("weight").send_keys("" ,profile['Weight'])
	driver.find_element_by_name("height").send_keys("", profile['Height'])
	driver.find_element_by_name("bust").send_keys("", profile['Bust'])
	driver.find_element_by_name("waist").send_keys("", profile['Waist'])
	driver.find_element_by_name("hips").send_keys("", profile['Hips'])
	driver.find_element_by_name("cup").send_keys("", profile['Cup'])
	driver.find_element_by_name("haircolour").send_keys("", profile['Haircolor'])
	driver.find_element_by_name("hairlength").send_keys("", profile['HairLength'])
	driver.find_element_by_name("eyecolour").send_keys("", profile['EyeColor'])
	driver.find_element_by_name("ethnicity").send_keys("", profile['Ethnicity'])
	driver.find_element_by_name("skincolour").send_keys("", profile['SkinColor'])
	driver.find_element_by_name("tattoo").send_keys("", profile['Tattoos'])
	driver.find_element_by_name("experience").send_keys("", profile['Experience'])
	driver.implicitly_wait(30)

	

	driver.find_element_by_link_text('Submit').send_keys("\n")
	time.sleep(5)
	driver.find_element_by_id("submit").send_keys("\n")


	driver.implicitly_wait(30)




	driver.get('http://52.7.237.110/album')

	driver.find_element_by_link_text('Add images toalbum').click()

	driver.implicitly_wait(30)

	
	driver.find_element_by_name('category').send_keys("General")
	driver.implicitly_wait(30)
	driver.find_element_by_name("profileimage[]").send_keys(image1)
	driver.implicitly_wait(30)

	driver.find_element_by_id("Uploadalbum").send_keys("\n")

	driver.implicitly_wait(30)
	driver.find_element_by_name('category').send_keys("indianwedding")
	driver.implicitly_wait(30)
	driver.find_element_by_name("profileimage[]").send_keys(image2)
	driver.implicitly_wait(30)
	driver.find_element_by_id("Uploadalbum").send_keys("\n")


	driver.implicitly_wait(30)
	driver.find_element_by_name('category').send_keys("western")
	driver.implicitly_wait(30)
	driver.find_element_by_name("profileimage[]").send_keys(image3)
	driver.implicitly_wait(30)
	driver.find_element_by_id("Uploadalbum").send_keys("\n")

	driver.close()



var = ""
csv_dict = dict()

#print "-------------------------------\n"

with open(os.path.expanduser('~/Desktop/zedlope-testing/profile1.csv'), 'rb') as f:
     reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
     for row in reader:
         csv_dict[re.sub(r'\s',"",row[0])] = re.sub(r'\n',"",row[1])



print csv_dict
#print profile2['1']
#keys = len(csv.keys())
#print keys

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

elif len(sys.argv) == 1 :


	starting_number = 1
	print "the starting_number is " ,starting_number

	ending_number = len(csv_dict.keys())

	ending_number += 1
	print ending_number
	print "the ending_number is " ,ending_number

elif len(sys.argv) == 2 :

	script, first= argv
	print "the script is " , script

	starting_number = int (float(first))
	print "the starting_number is " ,starting_number

	ending_number = len(csv_dict.keys())

	ending_number += 1
	print ending_number
	print "the ending_number is " ,ending_number



for x in range(starting_number,ending_number):
	y = str(x)
	#print type(y)
	#print "y is" + y
	print "csv_dist[y]",csv_dict[y]
	#print profile2['x']
	upload_data(csv_dict[y])
	
	# 	@retry(stop_max_attempt_number=3)
	# 	def stop_after_3_attempts():
	# 		print "Stopping after 3 attempts"
	# else:
	# 	continue
	


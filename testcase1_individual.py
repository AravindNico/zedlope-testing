# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
from selenium import webdriver
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time,re,sys,unittest
from selenium.webdriver.common.action_chains import ActionChains

FILTER_PARAM_001 = 1200;
FILTER_PARAM_002 = 42;
FILTER_PARAM_003 = 1158;
FILTER_PARAM_004 = 26;
FILTER_PARAM_005 = 614;
FILTER_PARAM_006 = 640;
FILTER_PARAM_007 = 20;
FILTER_PARAM_008 = 500;
FILTER_PARAM_009 = 520;
FILTER_PARAM_010 = 2;
FILTER_PARAM_011 = 174;
FILTER_PARAM_012 = 176;

def slider_movement(self,leftValue,rightValue):
	driver = self.driver
	sliderleft=driver.find_element_by_class_name("min-slider-handle")
	actions=ActionChains(driver)
	actions.click_and_hold(sliderleft)
	actions.move_by_offset(leftValue, 0)
	actions.release(None)
	actions.perform()
	sliderright=driver.find_element_by_class_name("max-slider-handle")
	actionsRight=ActionChains(driver)
	actionsRight.click_and_hold(sliderright)
	actionsRight.move_by_offset(rightValue, 0)
	actionsRight.release(None)
	actionsRight.perform()

def genderSelect_male(self):
	driver = self.driver
	driver.find_element_by_class_name("btn-group").click()
	driver.find_element_by_id("gender").click()
	driver.find_element_by_id("genderselect").click()
	time.sleep(5)
	driver.find_element_by_id("male").click()
	driver.find_element_by_id("search").click()

def genderSelect_female(self):
	driver = self.driver
	driver.find_element_by_class_name("btn-group").click()
	driver.find_element_by_id("gender").click()
	driver.find_element_by_id("genderselect").click()
	time.sleep(5)
	driver.find_element_by_id("female").click()
	driver.find_element_by_id("search").click()

def ageSelect(self):
	driver = self.driver
	driver.find_element_by_class_name("btn-group").click()
	driver.find_element_by_id("age1").click()

def ZLP_TM_SRD_001(self):
	driver = self.driver
	print "==================================================================="
	print "test 001 all profile count"
	print "==================================================================="
	total_profiles = driver.find_element_by_id("totalcount").get_attribute("value");
	print "total_profiles = ",total_profiles
	print "FILTER_PARAM_001 = ",FILTER_PARAM_001
	if (int(total_profiles) == FILTER_PARAM_001):
		print "test 001 all profile - success"
	else:
		print "test 001 all profile - count mismatch"

def ZLP_TM_SRD_002(self):
	driver = self.driver
	print "==================================================================="
	print "test 002 all male profile count"
	print "==================================================================="
	genderSelect_male(self)
	driver.implicitly_wait(30)
	total_male_profiles = driver.find_element_by_id("totalcount1").get_attribute("value");
	print "total_male_profiles = ",total_male_profiles
	print "FILTER_PARAM_002 = ",FILTER_PARAM_002
	if (int(total_male_profiles) == FILTER_PARAM_002):
		print "test 002 all male profile - success"
	else:
		print "test 002 all male profile - count mismatch"

def ZLP_TM_SRD_003(self):
	driver = self.driver
	print "==================================================================="
	print "test 003 all female profile count"
	print "==================================================================="
	genderSelect_female(self)
	time.sleep(5)
	driver.implicitly_wait(30)
	total_female_profiles = driver.find_element_by_id("totalcount1").get_attribute("value");
	print "total_female_profiles = ",total_female_profiles
	print "FILTER_PARAM_003 = ",FILTER_PARAM_003
	if (int(total_female_profiles) == FILTER_PARAM_003):
		print "test 003 all female profile - success"
	else:
		print "test 003 all female profile - count mismatch"

def ZLP_TM_SRD_004_1(self):
	driver = self.driver
	print "==================================================================="
	print "test 004 male age 18to24 count"
	print "==================================================================="
	genderSelect_male(self)
	self.assertTrue(self.is_element_present(By.ID, "gen"))
	ageSelect(self)
	time.sleep(2)
	slider_movement(self,0,-50)
	time.sleep(3)
	slider_value = driver.find_element_by_id("ex12c").get_attribute("value")
	print "slider_value = ",slider_value
	driver.find_element_by_id("search").click()
	self.assertTrue(self.is_element_present(By.ID, "age"))
	time.sleep(5)
	driver.implicitly_wait(30)
	total_male18to24_profiles = driver.find_element_by_id("totalcount1").get_attribute("value");
	print "total_male18to24_profiles = ",total_male18to24_profiles
	print "FILTER_PARAM_004 = ",FILTER_PARAM_004
	if (int(total_male18to24_profiles) == FILTER_PARAM_004):
		print "test 004 male18to24 success"
	else:
		print "test 004 male18to24 count mismatch"

def ZLP_TM_SRD_004_2(self):
	driver = self.driver
	print "==================================================================="
	print "test 004 male age 24to28 count"
	print "==================================================================="
	genderSelect_male(self)
	self.assertTrue(self.is_element_present(By.ID, "gen"))
	ageSelect(self)
	time.sleep(2)
	slider_movement(self,50,-20)
	time.sleep(3)
	slider_value = driver.find_element_by_id("ex12c").get_attribute("value")
	print "slider_value = ",slider_value
	driver.find_element_by_id("search").click()
	self.assertTrue(self.is_element_present(By.ID, "age"))
	driver.implicitly_wait(30)
	time.sleep(5)
	total_male24to28_profiles = driver.find_element_by_id("totalcount1").get_attribute("value");
	print "total_male24to28_profiles = ",total_male24to28_profiles
	print "FILTER_PARAM_007 = ",FILTER_PARAM_007
	if (int(total_male24to28_profiles) == FILTER_PARAM_007):
		print "test 004 male24to28 success"
	else:
		print "test 004 male24to28 count mismatch"

def ZLP_TM_SRD_004_3(self):
	driver = self.driver
	print "==================================================================="
	print "test 004 male age 28to32 count"
	print "==================================================================="
	genderSelect_male(self)
	self.assertTrue(self.is_element_present(By.ID, "gen"))
	ageSelect(self)
	time.sleep(2)
	slider_movement(self,80,20)
	time.sleep(3)
	slider_value = driver.find_element_by_id("ex12c").get_attribute("value")
	print "slider_value = ",slider_value
	driver.find_element_by_id("search").click()
	self.assertTrue(self.is_element_present(By.ID, "age"))
	driver.implicitly_wait(30)
	time.sleep(5)
	total_male28to32_profiles = driver.find_element_by_id("totalcount1").get_attribute("value");
	print "total_male28to32_profiles = ",total_male28to32_profiles
	print "FILTER_PARAM_010 = ",FILTER_PARAM_010
	if (int(total_male28to32_profiles) == FILTER_PARAM_010):
		print "test 004 male28to32 success"
	else:
		print "test 004 male28to32 count mismatch"

def ZLP_TM_SRD_005_1(self):
	driver = self.driver
	print "==================================================================="
	print "test 005 female age 18to24 count"
	print "==================================================================="
	genderSelect_female(self)
	self.assertTrue(self.is_element_present(By.ID, "gen"))
	ageSelect(self)
	slider_movement(self,0,-50);
	slider_value = driver.find_element_by_id("ex12c").get_attribute("value")
	print "slider_value = ",slider_value
	driver.find_element_by_id("search").click()
	self.assertTrue(self.is_element_present(By.ID, "age"))
	driver.implicitly_wait(30)
	time.sleep(5)
	total_female18to24_profiles = driver.find_element_by_id("totalcount1").get_attribute("value");
	print "total_female18to24_profiles = ",total_female18to24_profiles
	print "FILTER_PARAM_005 = ",FILTER_PARAM_005
	if (int(total_female18to24_profiles) == FILTER_PARAM_005):
		print "test 005 female18to24 success"
	else:
		print "test 005 female18to24 count mismatch"

def ZLP_TM_SRD_005_2(self):
	driver = self.driver
	print "==================================================================="
	print "test 005 female age 24to28 count"
	print "==================================================================="
	genderSelect_female(self)
	self.assertTrue(self.is_element_present(By.ID, "gen"))
	ageSelect(self)
	slider_movement(self,50,-20);
	slider_value = driver.find_element_by_id("ex12c").get_attribute("value")
	print "slider_value = ",slider_value
	driver.find_element_by_id("search").click()
	self.assertTrue(self.is_element_present(By.ID, "age"))
	driver.implicitly_wait(30)
	time.sleep(5)
	total_female24to28_profiles = driver.find_element_by_id("totalcount1").get_attribute("value");
	print "total_female24to28_profiles = ",total_female24to28_profiles
	print "FILTER_PARAM_008 = ",FILTER_PARAM_008
	if (int(total_female24to28_profiles) == FILTER_PARAM_008):
		print "test 005 female24to28 success"
	else:
		print "test 005 female24to28 count mismatch"

def ZLP_TM_SRD_005_3(self):
	driver = self.driver
	print "==================================================================="
	print "test 005 female age 28to32 count"
	print "==================================================================="
	genderSelect_female(self)
	self.assertTrue(self.is_element_present(By.ID, "gen"))
	ageSelect(self)
	slider_movement(self,80,20);
	slider_value = driver.find_element_by_id("ex12c").get_attribute("value")
	print "slider_value = ",slider_value
	driver.find_element_by_id("search").click()
	self.assertTrue(self.is_element_present(By.ID, "age"))
	driver.implicitly_wait(30)
	time.sleep(5)
	total_female28to32_profiles = driver.find_element_by_id("totalcount1").get_attribute("value");
	print "total_female28to32_profiles = ",total_female28to32_profiles
	print "FILTER_PARAM_011 = ",FILTER_PARAM_011
	if (int(total_female28to32_profiles) == FILTER_PARAM_011):
		print "test 005 female28to32 success"
	else:
		print "test 005 female28to32 count mismatch"

def ZLP_TM_SRD_006_1(self):
	driver = self.driver
	print "==================================================================="
	print "test 006 all age 18to24 count"
	print "==================================================================="
	ageSelect(self)
	slider_movement(self,0,-50);
	slider_value = driver.find_element_by_id("ex12c").get_attribute("value")
	print "slider_value = ",slider_value
	driver.find_element_by_id("search").click()
	self.assertTrue(self.is_element_present(By.ID, "age"))
	driver.implicitly_wait(30)
	time.sleep(5)
	total_18to24_profiles = driver.find_element_by_id("totalcount1").get_attribute("value");
	print "total_18to24_profiles = ",total_18to24_profiles
	print "FILTER_PARAM_006 = ",FILTER_PARAM_006
	if (int(total_18to24_profiles) == FILTER_PARAM_006):
		print "test 006 all 18to24 success"
	else:
		print "test 006 all 18to24 count mismatch"

def ZLP_TM_SRD_006_2(self):
	driver = self.driver
	print "==================================================================="
	print "test 006 all age 18to24 count"
	print "==================================================================="
	ageSelect(self)
	slider_movement(self,50,-20);
	slider_value = driver.find_element_by_id("ex12c").get_attribute("value")
	print "slider_value = ",slider_value
	driver.find_element_by_id("search").click()
	self.assertTrue(self.is_element_present(By.ID, "age"))
	driver.implicitly_wait(150)
	time.sleep(5)
	total_24to28_profiles = driver.find_element_by_id("totalcount1").get_attribute("value");
	print "total_24to28_profiles = ",total_24to28_profiles
	print "FILTER_PARAM_009 = ",FILTER_PARAM_009
	if (int(total_24to28_profiles) == FILTER_PARAM_009):
		print "test 006 all 24to28 success"
	else:
		print "test 006 all 24to28 count mismatch"

def ZLP_TM_SRD_006_3(self):
	driver = self.driver
	print "==================================================================="
	print "test 006 all age 18to24 count"
	print "==================================================================="
	ageSelect(self)
	slider_movement(self,80,20);
	slider_value = driver.find_element_by_id("ex12c").get_attribute("value")
	print "slider_value = ",slider_value
	driver.find_element_by_id("search").click()
	self.assertTrue(self.is_element_present(By.ID, "age"))
	driver.implicitly_wait(150)
	time.sleep(5)
	total_28to32_profiles = driver.find_element_by_id("totalcount1").get_attribute("value");
	print "total_28to32_profiles = ",total_28to32_profiles
	print "FILTER_PARAM_012 = ",FILTER_PARAM_012
	if (int(total_28to32_profiles) == FILTER_PARAM_012):
		print "test 006 all 28to32 success"
	else:
		print "test 006 all 28to32 count mismatch"

def ZLP_TM_SRD_007(self):
	driver = self.driver
	print "==================================================================="
	print "test 007 all age 31to40 count"
	print "==================================================================="
	ageSelect(self)
	slider_movement(self,0,-50);
	driver.find_element_by_id("search").click()
	self.assertTrue(self.is_element_present(By.ID, "age"))
	


class modelsearchtest(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Firefox()
		# self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.driver.get('http://52.7.237.110')
	
	def is_element_present(self,how,what):
		try:
			self.driver.find_element(by=how, value=what)
		except NoSuchElementException:
			return False
		return True
	
	def test_searchpaneldisplay(self):
		driver = self.driver
		ZLP_TM_SRD_001(self);
		driver.refresh()
		ZLP_TM_SRD_002(self);
		driver.refresh()
		ZLP_TM_SRD_003(self);
		driver.refresh()
		ZLP_TM_SRD_004_1(self);
		driver.refresh()
		ZLP_TM_SRD_004_2(self);
		driver.refresh()
		ZLP_TM_SRD_004_3(self);
		driver.refresh()
		ZLP_TM_SRD_005_1(self);
		driver.refresh()
		ZLP_TM_SRD_005_2(self);
		driver.refresh()
		ZLP_TM_SRD_005_3(self);
		driver.refresh()
		ZLP_TM_SRD_006_1(self);
		driver.refresh()
		ZLP_TM_SRD_006_2(self);
		driver.refresh()
		ZLP_TM_SRD_006_3(self);
		driver.refresh()
		ZLP_TM_SRD_007(self);
		driver.refresh();

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()
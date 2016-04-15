from selenium import webdriver
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time,re,sys,unittest
from sys import argv
from selenium.webdriver.common.action_chains import ActionChains

def genderSelect_male(self):
	driver = self.driver
	driver.find_element_by_class_name("btn-group").click()
	driver.find_element_by_id("gender").click()
	driver.find_element_by_id("genderselect").click()
	time.sleep(5)
	driver.find_element_by_id("male").click()
	time.sleep(5)
	driver.find_element_by_id("search").click()

def genderSelect_female(self):
	driver = self.driver
	driver.find_element_by_class_name("btn-group").click()
	driver.find_element_by_id("gender").click()
	driver.find_element_by_id("genderselect").click()
	time.sleep(5)
	driver.find_element_by_id("female").click()
	time.sleep(5)
	driver.find_element_by_id("search").click()

def ageSelect(self):
	driver = self.driver
	driver.find_element_by_class_name("btn-group").click()
	driver.find_element_by_id("age1").click()
	time.sleep(5)

def slider_movement(self,leftValue,rightValue):
	driver = self.driver
	sliderleft=driver.find_element_by_class_name("min-slider-handle")
	actions=ActionChains(driver)
	actions.click_and_hold(sliderleft)
	actions.move_by_offset(leftValue, 0)
	actions.release(None)
	actions.perform()
	time.sleep(5)
	sliderright=driver.find_element_by_class_name("max-slider-handle")
	actionsRight=ActionChains(driver)
	actionsRight.click_and_hold(sliderright)
	actionsRight.move_by_offset(rightValue, 0)
	actionsRight.release(None)
	actionsRight.perform()

def ZLP_TM_SPD_001(self):
	driver = self.driver
	print "==================================================================="
	print "test 001 - Zedlope page loading test"
	print "==================================================================="
	slider_value = driver.find_element_by_id("ex12c").get_attribute("value")
	print "slider_value = ",slider_value
	print "test001 passed"
	driver.refresh()

def ZLP_TM_SPD_002(self):
	driver = self.driver
	print "==================================================================="
	print "test 002 - Search button test"
	print "==================================================================="
	driver.find_element_by_id("search").click()
	self.assertTrue(self.is_element_present(By.ID, "age"))
	print "test002 passed"
	driver.refresh()

def ZLP_TM_SPD_003(self):
	driver = self.driver
	print "==================================================================="
	print "test 003 - male/female gender select test"
	print "==================================================================="
	genderSelect_female(self)
	self.assertTrue(self.is_element_present(By.ID, "gen"))
	time.sleep(5)
	genderSelect_male(self)
	self.assertTrue(self.is_element_present(By.ID, "gen"))
	print "test003 passed"
	driver.refresh()

def ZLP_TM_SPD_004(self):
	driver = self.driver
	print "==================================================================="
	print "test 004 - Age select test"
	print "==================================================================="
	ageSelect(self)
	slider_movement(self,50,35);
	driver.find_element_by_id("search").click()
	self.assertTrue(self.is_element_present(By.ID, "age"))
	time.sleep(5)
	slider_movement(self,-30,100);
	driver.find_element_by_id("search").click()
	self.assertTrue(self.is_element_present(By.ID, "age"))
	print "test004 passed"
	driver.refresh()

def ZLP_TM_SPD_005(self):
	driver = self.driver
	print "==================================================================="
	print "test 005 - Gender male selection with age test"
	print "==================================================================="
	ageSelect(self)
	slider_movement(self,50,35);
	driver.find_element_by_id("search").click()
	self.assertTrue(self.is_element_present(By.ID, "age"))
	time.sleep(5)
	genderSelect_male(self)
	self.assertTrue(self.is_element_present(By.ID, "gen"))
	time.sleep(5)
	print "test005 passed"

def ZLP_TM_SPD_006(self):
	driver = self.driver
	print "==================================================================="
	print "test 006 - Gender female selection with age test"
	print "==================================================================="
	ageSelect(self)
	slider_movement(self,50,35);
	driver.find_element_by_id("search").click()
	self.assertTrue(self.is_element_present(By.ID, "age"))
	time.sleep(5)
	genderSelect_female(self)
	self.assertTrue(self.is_element_present(By.ID, "gen"))
	time.sleep(5)
	print "test006 passed"
	driver.refresh()

def ZLP_TM_SPD_007(self):
	print "==================================================================="
	print "test 007 - Search subpanel display element clearing test"
	print "==================================================================="
	print "============================================================================="
	print "Prerequisite function - ZLP_TM_SPD_005"
	print "============================================================================="
	ZLP_TM_SPD_005(self);
	driver = self.driver
	driver.find_element_by_id("age").click()
	time.sleep(5)
	driver.find_element_by_id("gen").click()
	time.sleep(5)
	print "test007 passed"

def ZLP_TM_SPD_008(self):
	print "============================================================================="
	print "test 008 - Gender male selection with Search subpanel display element test"
	print "============================================================================="
	print "============================================================================="
	print "Prerequisite function - ZLP_TM_SPD_007"
	print "============================================================================="
	ZLP_TM_SPD_007(self);
	driver = self.driver
	genderSelect_male(self)
	self.assertTrue(self.is_element_present(By.ID, "gen"))
	time.sleep(5)
	print "test008 passed"
	driver.refresh()

def ZLP_TM_SPD_009(self):
	print "============================================================================="
	print "test 009 - Age selection with Search subpanel display element test"
	print "============================================================================="
	print "============================================================================="
	print "Prerequisite function - ZLP_TM_SPD_007"
	print "============================================================================="
	ZLP_TM_SPD_007(self);
	driver = self.driver
	ageSelect(self)
	slider_movement(self,50,35);
	driver.find_element_by_id("search").click()
	self.assertTrue(self.is_element_present(By.ID, "age"))
	time.sleep(5)
	print "test009 passed"
	driver.refresh()

class modelsearchtest(unittest.TestCase):
	def setUp(self):
		# self.driver = webdriver.Firefox()
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.driver.get('http://52.7.237.110')

	def is_element_present(self,how,what):
		try:
			self.driver.find_element(by=how, value=what)
			# print "success"
		except NoSuchElementException:
			# print "failure"
			return False
		return True
	
	def test_searchpaneldisplay(self):
		driver = self.driver
		ZLP_TM_SPD_002(self);
		ZLP_TM_SPD_003(self);
		ZLP_TM_SPD_004(self);
		ZLP_TM_SPD_005(self);
		ZLP_TM_SPD_006(self);
		ZLP_TM_SPD_007(self);
		ZLP_TM_SPD_008(self);
		ZLP_TM_SPD_009(self);

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()
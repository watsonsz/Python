from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
import time
s=Service('C:/Users/Xxmoz/Documents/git-hub Repos/Python/geckodriver.exe')
driver = webdriver.Firefox(service=s)

#open Webpage

driver.get('https://cbrtraffic.com/Devboats/Logs.aspx')

time.sleep(2)

#Login Variables
username = "mrthomas"
pw = "CBR8200"

#Login
username_input = driver.find_element(By.XPATH, '//*[@id="MainContent_idLogin_UserName"]')
username_input.send_keys(username)

pw_input = driver.find_element(By.XPATH, '//*[@id="MainContent_idLogin_Password"]')
pw_input.send_keys(pw)

time.sleep(1)

login = driver.find_element(By.XPATH,'//*[@id="MainContent_idLogin_Button1"]')
login.click()

#General Variables
name = "Mr Thomas"

#Inputs
refresh = driver.find_element(By.XPATH, '//*[@id="A2"]')
refresh.click()

customer = driver.find_element(By.XPATH, '//*[@id="MainContent_DDLCustomer"]')
customer_object = Select(customer)
customer_object.select_by_visible_text('GREAT LAKES')

crewinfo = driver.find_element(By.XPATH, '//*[@id="MainContent_btnGetCrew"]')
crewinfo.click()

time.sleep(6)

ticket = driver.find_element(By.XPATH, '//*[@id="MainContent_txtWO"]')
ticket.send_keys('46855')

activity = driver.find_element(By.XPATH, '//*[@id="MainContent_DDLActivity"]')
activity_object = Select(activity)
activity_object.select_by_visible_text('STBY')

time.sleep(2)

liteboat = driver.find_element(By.XPATH, '//*[@id="MainContent_chkLite"]')
liteboat.click()

time.sleep(2)

time_check = driver.find_element(By.XPATH, '//*[@id="MainContent_txtTime"]')
time_check.send_keys('0001')

location = driver.find_element(By.XPATH, '//*[@id="MainContent_DDLDock"]')
location_object = Select(location)
location_object.select_by_visible_text('CORPUS CHRISTI, TX')

time.sleep(5)

waterway = driver.find_element(By.XPATH, '//*[@id="MainContent_DDLWaterway"]')
waterway_object = Select(waterway)
waterway_object.select_by_visible_text('CORPUS CHRISTI SHIP CHANNEL')

location_info_keep = driver.find_element(By.XPATH, '//*[@id="MainContent_chkKeepLocation"]')
location_info_keep.click()

comment_section = driver.find_element(By.XPATH, '//*[@id="MainContent_txtComments"]')
comment_section.send_keys('stby Dredge Carolina')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time
from JsaVariables import *
s=Service('D:\git-hub Repos\Python\geckodriver.exe')
driver = webdriver.Firefox(service=s)

#open Webpage

driver.get('https://alternasec.formstack.com/forms/central_boat_rentals_job_environmental_safety_analysis')

time.sleep(2)

#General Information variables

VesselEmail = "missedmay@centralboat.com"
JobSite = "Miss Edmay"
JobActivity = "Making Up to Barge"
Pagevar = "1"
ofvar = "1"

#General Information Fill
email = driver.find_element(By.XPATH,'//*[@id="field114239152"]')
email.send_keys(VesselEmail)

ship = driver.find_element(By.XPATH, '//*[@id="field114239182"]')
ship.send_keys(JobSite)

job = driver.find_element(By.XPATH, '//*[@id="field114239184"]')
job.send_keys(JobActivity)

page = driver.find_element(By.XPATH, '//*[@id="field114239185"]')
page.send_keys(Pagevar)

ofBox = driver.find_element(By.XPATH, '//*[@id="field114239190"]')
ofBox.send_keys(ofvar)

#Basic Steps boxes

Bs1 = driver.find_element(By.XPATH,'//*[@id="field114239204"]' )
Bs1.send_keys("Pull up to Barge")

Bs2 = driver.find_element(By.XPATH,'//*[@id="field114239231"]' )
Bs2.send_keys("Attach Cables to Barge")

Bs3 = driver.find_element(By.XPATH,'//*[@id="field114239229"]' )
Bs3.send_keys("Tighten Winches")

#Bs4 = driver.find_element(By.XPATH,'//*[@id="field114239226"]' )
#Bs4.send_keys("Test")

#Bs5 = driver.find_element(By.XPATH,'//*[@id="field114239223"]' )
#Bs5.send_keys("Test")

#Bs6 = driver.find_element(By.XPATH,'//*[@id="field114239220"]' )
#Bs6.send_keys("Test")


#Potential Hazards Boxes

Ph1 = driver.find_element(By.XPATH,'//*[@id="field114239234"]' )
Ph1.send_keys(bump, stop, slip)

Ph2 = driver.find_element(By.XPATH,'//*[@id="field114239232"]' )
Ph2.send_keys(slip, pinch, back)

Ph3 = driver.find_element(By.XPATH,'//*[@id="field114239230"]' )
Ph3.send_keys(pinch, back)

#Ph4 = driver.find_element(By.XPATH,'//*[@id="field114239227"]' )
#Ph4.send_keys("Test")

#Ph5 = driver.find_element(By.XPATH, '//*[@id="field114239224"]' )
#Ph5.send_keys("Test")

#Ph6 = driver.find_element(By.XPATH, '//*[@id="field114239221"]')
#Ph6.send_keys("Test")

#Mitigation Boxes

Mb1 = driver.find_element(By.XPATH, '//*[@id="field114239235"]')
Mb1.send_keys (watch, ppe, situ)

Mb2 = driver.find_element(By.XPATH, '//*[@id="field114239233"]')
Mb2.send_keys (situ, form, ppe)

Mb3 = driver.find_element(By.XPATH, '//*[@id="field114239228"]')
Mb3.send_keys (proc, form, ppe)

#Mb4 = driver.find_element(By.XPATH, '//*[@id="field114239225"]')
#Mb4.send_keys ("Test")

#Mb5 = driver.find_element(By.XPATH, '//*[@id="field114239222"]')
#Mb5.send_keys ("Test")

#Mb6 = driver.find_element(By.XPATH, '//*[@id="field114239219"]')
#Mb6.send_keys ("Test")

#PPE Buttons::::Delete the '#' to click the button


#Hardhat = driver.find_element(By.XPATH,'//*[@id="field114239292_1"]')
#Hardhat.click()

#SafetyShoes = driver.find_element(By.XPATH,'')
#SafetyShoes.click()

#SafetyGlasses = driver.find_element(By.XPATH,'')
#SafetyGlasses.click()

#LifeVest = driver.find_element(By.XPATH,'')
#LifeVest.click

#Gloves = driver.find_element(By.XPATH,'')
#Gloves.click()

#Goggles = driver.find_element(By.XPATH,'')
#Goggles.click()

#FaceSheild = driver.find_element(By.XPATH,'')
#FaceSheild.click()

#HearingProt = driver.find_element(By.XPATH,'')
#HearingProt.click()

#Respirator = driver.find_element(By.XPATH,'')
#Respirator.click()

#FallProt = driver.find_element(By.XPATH,'')
#FallProt.click()




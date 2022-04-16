from JsaVariables import *

#open Webpage

driver.get('https://alternasec.formstack.com/forms/central_boat_rentals_job_environmental_safety_analysis')

time.sleep(2)

#General Information variables
JobActivity = "Making Up to Barge"
Pagevar = "1"
ofvar = "1"
tday = datetime.now()

#names
reviewed = driver.find_element(By.XPATH, '//*[@id="field114239191"]')
reviewed.send_keys(deckhands)

supervisor = driver.find_element(By.XPATH, '//*[@id="field114239192"]')
supervisor.send_keys(captain)

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

#date fill
monthbox = driver.find_element(By.XPATH, '//*[@id="field114239183M"]')
monthbox_object = Select(monthbox)
monthbox_object.select_by_visible_text(tday.strftime('%b'))

daybox =driver.find_element(By.XPATH, '//*[@id="field114239183D"]')
daybox_object=Select(daybox)
daybox_object.select_by_visible_text(tday.strftime('%d'))

yearbox = driver.find_element(By.XPATH, '//*[@id="field114239183Y"]')
yearbox_object = Select(yearbox)
yearbox_object.select_by_visible_text(tday.strftime('%Y'))
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

#Safety Equipment
hardhat = driver.find_element(By.XPATH, '//*[@id="field114239292_1"]')
driver.execute_script("arguments[0].click();", hardhat)

safetyshoes = driver.find_element(By.XPATH, '//*[@id="field114239292_2"]')
driver.execute_script("arguments[0].click();", safetyshoes)

SafetyGlasses = driver.find_element(By.XPATH, '//*[@id="field114239292_3"]')
driver.execute_script("arguments[0].click();", SafetyGlasses)

Gloves = driver.find_element(By.XPATH, '//*[@id="field114239292_9"]')
driver.execute_script("arguments[0].click();", Gloves)

# FallProtection = driver.find_element(By.XPATH, '//*[@id="field114239292_10"]')
# driver.execute_script("arguments[0].click();", FallProtection)

# Goggles = driver.find_element(By.XPATH, '//*[@id="field114239292_4"]')
# driver.execute_script("arguments[0].click();", Goggles)

# FaceShield = driver.find_element(By.XPATH, '//*[@id="field114239292_5"]')
# driver.execute_script("arguments[0].click();", FaceShield)

# HearingProtection = driver.find_element(By.XPATH, '//*[@id="field114239292_6"]')
# driver.execute_script("arguments[0].click();", HearingProtection)

# Respirator = driver.find_element(By.XPATH, '//*[@id="field114239292_"7]')
# driver.execute_script("arguments[0].click();", Respirator)

ProtectiveGarment = driver.find_element(By.XPATH, '//*[@id="field114239292_8"]')
driver.execute_script("arguments[0].click();", ProtectiveGarment)

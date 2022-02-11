from DrillVariables import *
#---------------------open Webpage

driver.get('https://alternasec.formstack.com/forms/emergency_drill_and_training_reporting_form')

time.sleep(2)

#------------------HAL YOU HAVE TO CHANGE THE XXXXXX TO THE TYPE OF DRILL
scene= "Security Drill"

#---------------------General Information Fill(DO NOT TOUCH)
email = driver.find_element(By.XPATH,'//*[@id="field106104796"]')
email.send_keys(VesselEmail)

ship = driver.find_element(By.XPATH, '//*[@id="field105490179"]')
ship_object = Select(ship)
ship_object.select_by_visible_text(Vessel)

drill = driver.find_element(By.XPATH, '//*[@id="field105490825"]')
drill.send_keys(scene)

#date fill
monthbox = driver.find_element(By.XPATH, '//*[@id="field105490189M"]')
monthbox_object = Select(monthbox)
monthbox_object.select_by_visible_text(tday.strftime('%b'))

daybox =driver.find_element(By.XPATH, '//*[@id="field105490189D"]')
daybox_object=Select(daybox)
daybox_object.select_by_visible_text(tday.strftime('%d'))

yearbox = driver.find_element(By.XPATH, '//*[@id="field105490189Y"]')
yearbox_object = Select(yearbox)
yearbox_object.select_by_visible_text(tday.strftime('%Y'))
#---------------------drill type::::Uncomment Drill needed

#fire = driver.find_element(By.XPATH, '//*[@id="field105490198_1"]')
#fire.click()

security = driver.find_element(By.XPATH, '//*[@id="field105490198_2"]')
security.click()

# manoverboard = driver.find_element(By.XPATH, '//*[@id="field105490198_3"]')
# manoverboard.click()

# collision = driver.find_element(By.XPATH, '//*[@id="field105490198_4"]')
# collision.click()

# spill = driver.find_element(By.XPATH, '//*[@id="field105490198_5"]')
# spill.click()

# abandon = driver.find_element(By.XPATH, '//*[@id="field105490198_6"]')
# abandon.click()

# medicalem = driver.find_element(By.XPATH, '//*[@id="field105490198_7"]')
# medicalem.click()

# grounding = driver.find_element(By.XPATH, '//*[@id="field105490198_8"]')
# grounding.click()

# other = driver.find_element(By.XPATH, '//*[@id="field105490198_9"]')
# other.click()


#---------------------Equipment Used:::Uncomment Equipment used

#General = driver.find_element(By.XPATH, '//*[@id="field105490216_1"]')
#General.click()

# extinguisher = driver.find_element(By.XPATH, '//*[@id="field105490216_2"]')
# extinguisher.click()

# firehose = driver.find_element(By.XPATH, '//*[@id="field105490216_3"]')
# firehose.click()

# skiff = driver.find_element(By.XPATH, '//*[@id="field105490216_4"]')
# skiff.click()

# bouys = driver.find_element(By.XPATH, '//*[@id="field105490216_5"]')
# bouys.click()

# spillkit = driver.find_element(By.XPATH, '//*[@id="field105490216_6"]')
# spillkit.click()

# other_equip = driver.find_element(By.XPATH, '//*[@id="field105490216_7"]')
# other_equip.click()


#---------------------Drill Actions

DrillComments = driver.find_element(By.XPATH, '//*[@id="field105491260"]')
DrillComments.send_keys('Security Drill, changing from Marsec 1 to Marsec 2. All Radios Operational. Make 15 minute security checks around the vessel. Suspend all loading on or off  of cargo on the boat. Untie Vessel and move away from the dock.')

#Names Fill
boss = driver.find_element(By.XPATH, '//*[@id="field105491294"]')
boss.send_keys(Captain)

Relief = driver.find_element(By.XPATH, '//*[@id="field105500134"]')
Relief.send_keys(Mate)

Deckhand1 = driver.find_element(By.XPATH, '//*[@id="field105500131"]')
Deckhand1.send_keys(Deck1)

Deckhand2 = driver.find_element(By.XPATH, '//*[@id="field105500081"]')
Deckhand2.send_keys(Deck2)
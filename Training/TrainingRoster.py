from TrainingVariables import *
#---------------------open Webpage

driver.get('https://alternasec.formstack.com/forms/cbr_weekly_safety_training_roster')

time.sleep(2)


#date fill
monthbox = driver.find_element(By.XPATH, '//*[@id="field105492510M"]')
monthbox_object = Select(monthbox)
monthbox_object.select_by_visible_text(tday.strftime('%b'))

daybox =driver.find_element(By.XPATH, '//*[@id="field105492510D"]')
daybox_object=Select(daybox)
daybox_object.select_by_visible_text(tday.strftime('%d'))

yearbox = driver.find_element(By.XPATH, '//*[@id="field105492510Y"]')
yearbox_object = Select(yearbox)
yearbox_object.select_by_visible_text(tday.strftime('%Y'))



#---------------------General Information Fill(DO NOT TOUCH)
email = driver.find_element(By.XPATH,'//*[@id="field106104960"]')
email.send_keys(VesselEmail)

ship = driver.find_element(By.XPATH, '//*[@id="field105492511"]')
ship_object = Select(ship)
ship_object.select_by_visible_text(Vessel)


#Names Fill
boss = driver.find_element(By.XPATH, '//*[@id="field105492531"]')
boss.send_keys(Captain)

Relief = driver.find_element(By.XPATH, '//*[@id="field105492542"]')
Relief.send_keys(Mate)

Deckhand1 = driver.find_element(By.XPATH, '//*[@id="field106420912"]')
Deckhand1.send_keys(Deck1)

Deckhand2 = driver.find_element(By.XPATH, '//*[@id="field105492714"]')
Deckhand2.send_keys(Deck2)

Deckhand3 = driver.find_element(By.XPATH, '//*[@id="field105492709"]')
Deckhand3.send_keys(Deck3)


signature = driver.find_element(By.XPATH, '//*[@id="field105492871"]')
signature.send_keys(Captain)
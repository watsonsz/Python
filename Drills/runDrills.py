from DrillVariables import *

#---------------------open Webpage

driver.get('https://alternasec.formstack.com/forms/emergency_drill_and_training_reporting_form')

time.sleep(6)

#---------------------General Information Fill(DO NOT TOUCH)
email = driver.find_element(By.XPATH,'//*[@id="field106104796"]')
email.send_keys(VesselEmail)

ship = driver.find_element(By.XPATH, '//*[@id="field105490179"]')
ship_object = Select(ship)
ship_object.select_by_visible_text(Vessel)

from drillFunctions import *

trainingTopic = findScene()


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




#Names Fill
boss = driver.find_element(By.XPATH, '//*[@id="field105491294"]')
boss.send_keys(Captain)

Relief = driver.find_element(By.XPATH, '//*[@id="field105500134"]')
Relief.send_keys(Mate)

Deckhand1 = driver.find_element(By.XPATH, '//*[@id="field105500131"]')
Deckhand1.send_keys(Deck1)

Deckhand2 = driver.find_element(By.XPATH, '//*[@id="field105500081"]')
Deckhand2.send_keys(Deck2)

Deckhand3 = driver.find_element(By.XPATH, '//*[@id="field105500077"]')
Deckhand3.send_keys(Deck3)

def runTraining(trainingTopic):
    training = driver.find_element(By.XPATH,'//*[@id="field105490833"]')
    training.send_keys(trainingTopic)

    if(trainingTopic != "Training Completed for this month"):
        
        driver.execute_script("window.open('https://alternasec.formstack.com/forms/cbr_weekly_safety_training_roster')")
        driver.switch_to.window(driver.window_handles[-1])
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

        trainingRosterTopic = driver.find_element(By.XPATH,'//*[@id="field105492508"]')
        trainingRosterTopic.send_keys(trainingTopic)

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

        
runTraining(trainingTopic)
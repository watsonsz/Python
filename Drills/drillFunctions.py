from DrillVariables import*
tday = datetime.now()

drill = driver.find_element(By.XPATH, '//*[@id="field105490825"]')
def findScene():
    if(tday.strftime('%B') == "January"):
        if(tday.strftime('%d') < '03'):
            fireEngineRoom()
            return 'Slips, Trips, and Falls'
        elif (tday.strftime('%d') < '10'):
            manOverboard()
            return 'Personal Protective Equipment'
        elif (tday.strftime('%d') < '17'):
            collision()
            return 'Rigging'
        else:
            grounding()
            return "Training Completed for this month"
    if(tday.strftime('%B') == "February"):
        if(tday.strftime('%d') < '06'):
            spill()
            return "Hazard Communication/GHS/HM 126F"
        elif(tday.strftime('%d') < '14'):
            security()
            return "Hazwoper Awareness Level"
        elif(tday.strftime('%d') < '21'):
            abandonShip()
            return "Training Completed for this month"
        else:
            fireOnBarge()
            return "2-4"
    if(tday.strftime('%B') == "March"):
        if(tday.strftime('%d') < '07'):
            manOverboard()
            return "Back Safety/Lifting Techniques"
        elif(tday.strftime('%d') < '14'):
            collision()
            return "Fall Protection/Ladder Policy"
        elif(tday.strftime('%d') < '21'):
            grounding()
            return "Training Completed for this month"
        elif(tday.strftime('%d') < '28'):
            fireEngineRoom()
            return "Training Completed for this month"
        else:
            spill()
            return "Training Completed for this month"
    if(tday.strftime('%B') == "April"):
        
        if(tday.strftime('%d') < '11'):
            security()
            return "Fire Prevention"
        elif(tday.strftime('%d') < '18'):
            lossOfSteering()
            return "Hot Work"
        elif(tday.strftime('%d') < '25'):
            fireEngineRoom
            return "Vessel Navigating/Reporting Unsafe Conditions"
        else:
            manOverboard()
            return "Training Completed for this month"
    if(tday.strftime('%B') == "May"):
       
        if(tday.strftime('%d') < '09'):
            collision()
            return "Heat Stress"
        elif(tday.strftime('%d') < '16'):
            grounding()
            return "H2S(Hydrogen Sulfide)"
        elif(tday.strftime('%d') < '23'):
            fireOnBarge()
            return "Drug and Alcohol Awareness"
        else:
            spill()
            return "Training Completed for this month"
    if(tday.strftime('%B') == "June"):
        
        if(tday.strftime('%d') < '06'):
            security()
            return "First Aid/CPR "
        elif(tday.strftime('%d') < '13'):
            abandonShip()
            return "Access to Medical Records"
        elif(tday.strftime('%d') < '20'):
            fireEngineRoom
            return "BloodBorne Pathogens"
        elif(tday.strftime('%d') < '27'):
            manOverboard()
            return "Training Completed for this month"
        else:
            collision()
            return "Training Completed for this month"
    if(tday.strftime('%B') == "July"):
        i = '7'
        if(tday.strftime('%d') < '11'):
            grounding()
            return "Machine Guarding"
        elif(tday.strftime('%d') < '18'):
            fireOnBarge
            return "Confine Space Awareness"
        elif(tday.strftime('%d') < '25'):
            spill()
            return "Training Completed for this month"
        else:
            security()
            return "Training Completed for this month"
    if(tday.strftime('%B') == "August"):
        i = '8'
        if(tday.strftime('%d') < '08'):
            abandonShip()
            return "Hearing Protection"
        elif(tday.strftime('%d') < '15'):
            fireEngineRoom()
            return "Defensive Driving"
        elif(tday.strftime('%d') < '22'):
            manOverboard()
            return "Training Completed for this month"
        elif(tday.strftime('%d') < '28'):
            collision()
            return "Training Completed for this month"
        else:
            grounding()
            return "SDS (Storage/Safe Use)"
    if(tday.strftime('%B') == "September"):
        if(tday.strftime('%d') < 4):
            grounding()
            return "SDS (Storage/Safe Use)"
        elif (tday.strftime('%d') < 12):
            fireOnBarge()
            return "Pollution Prevention/Small Spills"
        elif (tday.strftime('%d') < 19):
            spill()
            return "Training Completed for this month"
        elif (tday.strftime('%d') < 26):
            security()
            return "Training Completed for this month"
        else:
            abandonShip()
            return "Training Completed for this month"

    if(tday.strftime('%B') == "October"):
        if(tday.strftime('%d') < 10):
            fireEngineRoom()
            return "Lockout/Tag Out"
        elif (tday.strftime('%d') < 17):
            manOverboard()
            return "Electrical Safety"
        elif (tday.strftime('%d') < 24):
            collision()
            return "Training Completed for this month"
        elif (tday.strftime('%d') < 31):
            grounding()
            return "Training Completed for this month"
        else:
            fireOnBarge
            return "Respiratory Awareness"

    if(tday.strftime('%B') == "November"):
        if(tday.strftime('%d') < 7):
            fireOnBarge()
            return "Respiratory Awareness"
        elif (tday.strftime('%d') < 14):
            spill()
            return "Benzene Awareness"
        elif (tday.strftime('%d') < 21):
            security()
            return "Training Completed for this month"
        elif (tday.strftime('%d') < 28):
            abandonShip()
            return "Training Completed for this month"
        else:
            fireEngineRoom()
            return "Violence in the Workplace"

    if(tday.strftime('%B') == "December"):
        if(tday.strftime('%d') < 5):
            fireEngineRoom()
            return "Violence in the Workplace"
        elif (tday.strftime('%d') < 12):
            manOverboard()
            return "Hand Protection"
        elif (tday.strftime('%d') < 19):
            lossOfSteering()
            return "Training Completed for this month"
        elif (tday.strftime('%d') < 26):
            grounding()
            return "Training Completed for this month"
        else:
            fireOnBarge
            return "Slips, Trips, Falls"

def manOverboard():
    scene= "Man Overboard"
    drill.send_keys(scene)
    manoverboard = driver.find_element(By.XPATH, '//*[@id="field105490198_3"]')
    manoverboard.click()
    #---------------------Equipment Used:::Uncomment Equipment used

    General = driver.find_element(By.XPATH, '//*[@id="field105490216_1"]')
    General.click()

    bouys = driver.find_element(By.XPATH, '//*[@id="field105490216_5"]')
    bouys.click()

    #---------------------Drill Actions

    DrillComments = driver.find_element(By.XPATH, '//*[@id="field105491260"]')
    DrillComments.send_keys('Announce "Man Overboard, Man Overboard, Man Overboard Starboard Side". Take engines out of gear. Use rudder to swing boat or barge out of the way. Keep Man in sight. Sound 3 short blasts on horn. Sound General Alarm. Assign someone to keep an eye on him. If victim is concious, throw lifering or any available flotation device. If Victim cannot be reached with lifering, use alternate method or other boat. If light boat, pick them up on down-current side')

def collision():
    scene= "Collision/Allision"
    drill.send_keys(scene)
    #---------------------drill type::::Uncomment Drill needed

    collision = driver.find_element(By.XPATH, '//*[@id="field105490198_4"]')
    collision.click()

    #---------------------Equipment Used:::Uncomment Equipment used

    General = driver.find_element(By.XPATH, '//*[@id="field105490216_1"]')
    General.click()


    #---------------------Drill Actions

    DrillComments = driver.find_element(By.XPATH, '//*[@id="field105491260"]')
    DrillComments.send_keys("Sound 5 short blasts on horn. Sound General ALarm. Crew muster to wheel house with life jackets donned and handheld radios. Notify Traffic if blocking. Attend to any injured crew. Assess any damages to boat/dock/barge. Obtain info from other boat/dock. Notify USCG. Take photos of all damages. Captain notify campany QI prior to acting as company representative. Fill out incident report. If any injuries occur refer to SOP 5101")

def security():
    scene= "Security Drill"
    drill.send_keys("A security drill is done in the blue folder, NOT this interface.")

def fireEngineRoom():
    scene= "Fire in Engine Room"
    drill.send_keys(scene)
    #---------------------drill type::::Uncomment Drill needed

    fire = driver.find_element(By.XPATH, '//*[@id="field105490198_1"]')
    fire.click()

    #---------------------Equipment Used:::Uncomment Equipment used

    General = driver.find_element(By.XPATH, '//*[@id="field105490216_1"]')
    General.click()

    extinguisher = driver.find_element(By.XPATH, '//*[@id="field105490216_2"]')
    extinguisher.click()

    firehose = driver.find_element(By.XPATH, '//*[@id="field105490216_3"]')
    firehose.click()

    #---------------------Drill Actions

    DrillComments = driver.find_element(By.XPATH, '//*[@id="field105491260"]')
    DrillComments.send_keys('Sound General Alarm, call out "fire, fire, FIre In Engine room." Crew mustered to wheelhouse with lifejackets donned and handheld radios. Closed blower and stack vents. Pulled fuel shut off valve. Closed Engine room door. Charged firehoses and brought b-5 extinguisher to engine room door. Fire contained. Discussed drill with crew')

def abandonShip():
    scene= "Abandon Ship"
    drill.send_keys(scene)
    abandon = driver.find_element(By.XPATH, '//*[@id="field105490198_6"]')
    abandon.click()


    #---------------------Equipment Used:::Uncomment Equipment used

    General = driver.find_element(By.XPATH, '//*[@id="field105490216_1"]')
    General.click()

    other_equip = driver.find_element(By.XPATH, '//*[@id="field105490216_7"]')
    other_equip.click()


    #---------------------Drill Actions

    DrillComments = driver.find_element(By.XPATH, '//*[@id="field105491260"]')
    DrillComments.send_keys('Sounded General Alarm. Crew Mustered to wheelhouse with Life vest donned. Took head count then head outside to the second deck to grab EPIRB and discussed proper life raft launching procedure')

def grounding():
    scene = "Grounding"
    drill.send_keys(scene)

    grounding = driver.find_element(By.XPATH, '//*[@id="field105490198_8"]')
    grounding.click()

    #---------------------Equipment Used:::Uncomment Equipment used

    General = driver.find_element(By.XPATH, '//*[@id="field105490216_1"]')
    General.click()

    DrillComments = driver.find_element(By.XPATH, '//*[@id="field105491260"]')
    DrillComments.send_keys('Sound General ALarm. Crew muster to wheel house with life jackets donned and handheld radios. Notify Traffic if blocking. Attend to any injured crew. Assess any damages to boat. Notify USCG. Take photos of all damages. Captain notify campany QI prior to acting as company representative. Fill out incident report. If any injuries occur refer to SOP 5101')

def spill():
    scene= "Spill(Fuel Hose Leaking)"
    drill.send_keys(scene)

    spill = driver.find_element(By.XPATH, '//*[@id="field105490198_5"]')
    spill.click()

    spillkit = driver.find_element(By.XPATH, '//*[@id="field105490216_6"]')
    spillkit.click()

    DrillComments = driver.find_element(By.XPATH, '//*[@id="field105491260"]')
    DrillComments.send_keys('Fuel Hose busted while transferring fuel. Shut off fuel pump on deck. Secure all valves and informed Captain on Watch and person recieving fuel. Use emergency spill kit/oil boom to contain flow')

def fireOnBarge():
    scene= "Fire on Barge"
    drill.send_keys(scene)
    
    fire = driver.find_element(By.XPATH, '//*[@id="field105490198_1"]')
    fire.click()

    General = driver.find_element(By.XPATH, '//*[@id="field105490216_1"]')
    General.click()

    extinguisher = driver.find_element(By.XPATH, '//*[@id="field105490216_2"]')
    extinguisher.click()

    firehose = driver.find_element(By.XPATH, '//*[@id="field105490216_3"]')
    firehose.click()

    DrillComments = driver.find_element(By.XPATH, '//*[@id="field105491260"]')
    DrillComments.send_keys('Sound General Alarm, call out "fire, fire, FIre on barge." Notify crew on barge, crew charged firehoses and simulated fighting fire. Discussed drill with crew')

def lossOfSteering():
    scene= "xxxxxxxxxxxx"
    drill.send_keys(scene)

    other = driver.find_element(By.XPATH, '//*[@id="field105490198_9"]')
    other.click()

    #need to fill out other

    General = driver.find_element(By.XPATH, '//*[@id="field105490216_1"]')
    General.click()

    DrillComments = driver.find_element(By.XPATH, '//*[@id="field105491260"]')
    DrillComments.send_keys('Need to fill out lossOfSeteering')
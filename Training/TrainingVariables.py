#Imports and Drivers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
import time
from datetime import datetime
s=Service('C:/Users/Xxmoz/OneDrive/Documents/git-hub-repos/Python/geckodriver.exe')
driver = webdriver.Firefox(service=s)

Captain = 'Bryan Veregrin'
Mate = 'Bryce Jones'
Deck1 = 'Steven Watson'
Deck2 = 'Blaine Gavin'
Deck3 = 'Josiah Freerick'

#Vessel Info
VesselEmail = 'MissElizabeth@centralboat.com'
#Vessel = 'MR THOMAS'
Vessel = 'MISS ELIZABETH'
#time get
tday = datetime.now()
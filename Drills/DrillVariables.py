#Imports and Drivers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
from datetime import datetime
import time
s=Service('C:/Users/Xxmoz/OneDrive/Documents/git-hub-repos/Python/geckodriver.exe')
driver = webdriver.Firefox(service=s)

Captain = 'Bryan Veregrin'
Mate = 'Tim '
Deck1 = 'Steven Watson'
Deck2 = 'Josiah Feerick'
Deck3 = 'Carlos Garcia'

#Vessel Info
VesselEmail = 'MissElizabeth@centralboat.com'
#Vessel = 'MR THOMAS'
Vessel = 'MISS ELIZABETH'


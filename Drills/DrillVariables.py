#Imports and Drivers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
import time
from datetime import datetime
s=Service('C:/Users/Xxmoz/Documents/git-hub Repos/Python/geckodriver.exe')
driver = webdriver.Firefox(service=s)

Captain = 'Jason Mayon'
Mate = 'John Fruge'
Deck1 = 'Steven Watson'
Deck2 = 'Hal Edwards'

#Vessel Info
VesselEmail = 'missedmay@centralboat.com'
#Vessel = 'MR THOMAS'
Vessel = 'MISS EDMAY'
#time get
tday = datetime.now()


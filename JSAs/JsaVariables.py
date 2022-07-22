#Imports and Drivers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
import time
from datetime import datetime
s=Service('C:/Users/Xxmoz/OneDrive/Documents/git-hub-repos/Python/geckodriver.exe')
driver = webdriver.Firefox(service=s)

#names
deckhand1 = "Steven Watson"
deckhand2 = "Blaine Gavin"
deckhand3 = "Josiah Freerick"

#FIXME:::::
deckhands = deckhand1 + ", " + deckhand2+", "+deckhand3
captain = "Bryan Veregrin" 

#vessel information
VesselEmail= "misselizabeth@centralboat.com"
JobSite = "Miss Elizabeth"

#steps variable:::::::::
gather = "Gather Equipment and Tools"
stow = "Stow Equipment and Tools"

#Hazard Variables
slip = "Slips, Trips, and Falls, "
pinch = "Pinch Points, "
back = "Back Strain, "
bump = "Sudden Bumps, "
stop = "Sudden Stops, "
burst = "Hose/Line Busting, "
damage = "Bodily Injury/Equipment Damage, "
burn = "Burns, Slips, Spills, "
unheard = "Miscommunication, "
eye = "Eye/Hand Injury, "
coll = "Collisions"
shock = "Electrical Shock, "

#Mitigation Variables
situ = "Situational-Awareness "
ppe = "wear proper PPE, "
form = "Proper Form, "
proc = "Follow Proper Procedures, "
watch = "Watch for Bump, "
safe = "Stay in Safe Area, "
cap = "Wait for Captain Instruction, "
inspect = "Inspect Equipment Before AND After use, "
oil = "Oil Pads, "
lockout = "Follow Proper Lockout Procedures, "
comm = "Clear Communication, Ensure All Parties Understand, "
msds = "Properly Review MSDS before use, "
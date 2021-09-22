"""
Webscraping module for finding flight data with specific parameters for # of connecting flights, stop locations, and airlines

This module uses selenium to open Google flights for the flights in that time period to gather data and printing 
and storing the relevant information for each flight. Time delays were used in order to avoid google's anti-bot
detection.

Author: Logan Kraver
Date: 6/10/2020
"""

from selenium import webdriver
import time
import pandas as pd


#initializing chrome driver and website
driver = webdriver.Chrome(r'C:\Users\logan\Documents\chromedriver.exe')
driver.maximize_window()
driver.get("https://www.google.com/flights?hl=en#flt=LAX.JFK.2020-06-19;c:USD;e:1;ca:-DCA,-TPA,-PDX,-FLL,-BOS,-MSP,-SJC,-SMF,-TUS;a:AA,DL,UA,WN,AS;sd:1;t:f;tt:o")


#clicking to expand flight menu to show all flights
allflightbutton = driver.find_element_by_class_name("gws-flights-results__dominated-toggle")
allflightbutton.click()
time.sleep(.5)

#clicking the expand button for more flight information for each flight
expandableButton = driver.find_elements_by_class_name("gws-flights-results__expand")
for button1 in expandableButton:
    time.sleep(2)
    button1.click()
    
    
#retrieving departure, arrival, and aircraft type for all flights
time.sleep(1)
InitialLocation = driver.find_elements_by_class_name("gws-flights-results__leg-departure")
ArrivalLocation = driver.find_elements_by_class_name("gws-flights-results__leg-arrival")
planeType = driver.find_elements_by_class_name("gws-flights-results__aircraft-type")


#writing flight data into text file
length = len(InitialLocation)
x = 0

f = open('FlightData.txt', 'r')
f.write("")
f.close()

while x < length:
    f = open('FlightData.txt', 'a')
    f.write(InitialLocation[x].text)
    f.write("\n")
    f.write(ArrivalLocation[x].text)
    f.write("\n")
    f.write(planeType[x].text)
    x = x + 1
    f.write("\n")
    f.write("\n")
    f.close


#closing chrome driver
time.sleep(5)
driver.close()

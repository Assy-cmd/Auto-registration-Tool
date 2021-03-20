# Test script to try different driver obfuscation tactics


import time 
import os
import getpass
from datetime import datetime
import win32com.client as win32

import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

from random import seed
from random import gauss

currUser = str(getpass.getuser())
currUserRoot = 'C:/Users/' + currUser + '/Desktop/scraper/Auto-registration-Tool'
ChromeDriverPath = currUserRoot + '/chromedriver87.exe'
PATH = 'C:/Program Files (x86)/Python37-32/chromedriver.exe'
URL = "https://warrior.uwaterloo.ca/Program/GetProgramDetails?courseId=cc2a16d7-f148-461e-831d-7d4659726dd1&semesterId=b0d461c3-71ea-458e-b150-134678037221"

seed(1)

def randTime():
    randVarTime = -1
    while randVarTime < 1:
        randVarTime = gauss(3,1)
        return randVarTime
    return randVarTime

#chrome_options = Options()
chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation','enable-logging'])
#chrome_options.add_experimental_option("excludeSwitches", ['enable-loggins'])

try:
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
except Exception as e:
    print(e)

try:
    chrome_options.add_argument("--user-data-dir=chrome-data")
    driver1 = webdriver.Chrome(ChromeDriverPath, options=chrome_options, desired_capabilities=chrome_options.to_capabilities())
    chrome_options.add_argument("user-data-dir=selenium")
except Exception as e:
    print(e)

time.sleep(randTime())

driver1.maximize_window()

time.sleep(randTime())

driver1.get(URL)


#git test
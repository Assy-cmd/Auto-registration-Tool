from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime
from dateutil.relativedelta import relativedelta
from selenium.webdriver.chrome.options import Options

import time 
import os
import getpass
from datetime import datetime
import logging
from cryptography.fernet import Fernet

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

currUser = str(getpass.getuser())

logging.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)s:\t%(message)s', level=logging.DEBUG, datefmt="%Y-%m-%d %H:%M:%S", filename='C:/Users/Nick/Desktop/gymBookerLog.log')

delay = 5

def todayDate(days_plus):
    now = datetime.datetime.now()
    days_ahead = (datetime.datetime.now() + relativedelta(days=days_plus)).strftime('%m-%d-%Y').replace("-", "/")
    #print (days_ahead)
    return(days_ahead)

def credentials():
    username = ''
    plain_text_encryptedpassword = ''

    # https://www.mssqltips.com/sqlservertip/5173/encrypting-passwords-for-use-with-python-and-sql-server/
    
    with open('C:/Users/Nick/Desktop/username.txt', 'r') as doc:
        for line in doc:
            username = line
    
    with open ('C:/Users/Nick/Desktop/learnKey.bin', 'rb') as doc2:
        for line in doc2:
            key = line
    
    cipher_suite = Fernet(key)

    with open('C:/Users/Nick/Desktop/learnPSWRD_bytes.bin', 'rb') as file_object:
        for line in file_object:
            encryptedpwd = line

    uncipher_text = (cipher_suite.decrypt(encryptedpwd))
    plain_text_encryptedpassword = bytes(uncipher_text).decode("utf-8") #convert to string

    return plain_text_encryptedpassword, username

def login():
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.LINK_TEXT, "Log In")))
        login = driver.find_element_by_link_text("Log In").click()
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="divLoginOptions"]/div[2]/div[2]/div/button')))
        watiam = driver.find_element_by_xpath('//*[@id="divLoginOptions"]/div[2]/div[2]/div/button').click()
        pswrd, username = credentials()
        userName = driver.find_element_by_id("userNameInput")
        userName.send_keys(username)
        userName.send_keys(Keys.RETURN)
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "passwordInput")))
        password = driver.find_element_by_id("passwordInput")
        password.send_keys(pswrd)
        password.send_keys(Keys.RETURN)
    except Exception as e:
        print(e)
        logging.debug(e)
        logging.debug("error in login")

def wait_until():
    if datetime.now().strftime('%H.%f')[:2] == '15':
        end_datetime = datetime.now().replace(hour=18,minute=0,second=0,microsecond=100)
    else:
        end_datetime = datetime.now().replace(hour=21,minute=0, second=0, microsecond=110)
    while True:
        diff = (end_datetime - datetime.now()).total_seconds()
        if diff < 0: return       # In case end_datetime was in past to begin withtime
        time.sleep(diff/2)
        if diff <= 0.1: return

def selectProgram():
    driver.refresh()
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//button[@class = 'btn btn-primary']")))
    bar = driver.find_elements_by_xpath("//button[@class = 'btn btn-primary']")
    bar = bar[len(bar)-3]
    bar.click()

def accept():
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'btnAccept')))
        accept = driver.find_element_by_id("btnAccept").click()
    except Exception as e:
        logging.debug(e)
        logging.info("failed to click accept button")        

def noAddCart():
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'rbtnNo')))
    noButton = driver.find_elements_by_id("rbtnNo")
    for i in range(9):
        noButton[i].click()
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[2]/form[2]/div[12]/button[2]')))
    addCart = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/form[2]/div[12]/button[2]").click()

def lastStep():
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'checkoutButton')))
    checkout = driver.find_element_by_id("checkoutButton").click()
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[5]/div/div[2]/button[2]')))
    finish = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[5]/div/div[2]/button[2]').click()

PATH = "C:/Users/Nick/Desktop/ChromeDrivers/chromedriver88.exe"

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation','enable-logging'])

try:
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
except Exception as e:
    print(e)

try:
    chrome_options.add_argument("--user-data-dir=chrome-data")
    driver = webdriver.Chrome(PATH, options=chrome_options, desired_capabilities=chrome_options.to_capabilities())
    chrome_options.add_argument("user-data-dir=selenium")
except Exception as e:
    print(e)

driver.get("https://warrior.uwaterloo.ca/Program/GetProgramDetails?courseId=cc2a16d7-f148-461e-831d-7d4659726dd1&semesterId=26de9ca7-b227-429c-b21f-633b4cb4c462")

login()

wait_until()
selectProgram()
accept()
noAddCart()
lastStep()
driver.quit()

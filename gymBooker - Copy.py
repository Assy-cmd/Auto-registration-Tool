from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime
from dateutil.relativedelta import relativedelta

from selenium.webdriver.chrome.options import Options


def todayDate(days_plus):
    now = datetime.datetime.now()
    days_ahead = (datetime.datetime.now() + relativedelta(days=days_plus)).strftime('%m-%d-%Y').replace("-", "/")
    #print (days_ahead)
    return(days_ahead)


def addevent(start, subject):

    oOutlook = win32com.client.Dispatch("Outlook.Application")
    appointment = oOutlook.CreateItem(1) # 1=outlook appointment item
    appointment.Start = start
    appointment.Subject = subject
    appointment.Duration = 45
    appointment.Location = 'CIF GYM'
    appointment.ReminderSet = True
    appointment.ReminderMinutesBeforeStart = 1
    appointment.Save()
    return


def login():
    login = driver.find_element_by_link_text("Log In").click()
    time.sleep(1)

    watiam = driver.find_element_by_xpath('//*[@id="divLoginOptions"]/div[2]/div[2]/div/button').click()

    userName = driver.find_element_by_id("userNameInput")
    userName.send_keys("USERNAME")
    userName.send_keys(Keys.RETURN)
    password = driver.find_element_by_id("passwordInput")
    password.send_keys("PASSWORD")
    password.send_keys(Keys.RETURN)
    time.sleep(1)


def selectProgram():
    #programs = driver.find_elements_by_class_name("program-schedule-card-header")
    #for date in range(50):
    bar = driver.find_elements_by_xpath("//button[@class = 'btn btn-primary pull-left']")
    #bar = date.find_elements_by_class_name("btn btn-primary pull-left")
        
    #kingClass = bar.get_attribute("class")
    time.sleep(1)
    bar[len(bar) - 1].click()
    time.sleep(1)


def accept():
    accept = driver.find_element_by_id("btnAccept").click()
    time.sleep(1)


def noAddCart():
    noButton = driver.find_elements_by_id("rbtnNo")

    for i in range(8):
        noButton[i].click()

    addCart = driver.find_element_by_xpath("//*[@id='mainContent']/div[2]/form[2]/div[2]/button[2]").click()
    time.sleep(1)


def lastStep():
    checkout = driver.find_element_by_id("checkoutButton").click()
    time.sleep(1)
    finish = driver.find_element_by_xpath('//*[@id="CheckoutModal"]/div/div[3]/button[2]').click()


PATH = 'C:/Program Files (x86)/Python37-32/chromedriver.exe'
chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works
driver = webdriver.Chrome(PATH, options=chrome_options)

#options = webdriver.ChromeOptions();
#options.add_argument('headless');
#options.add_argument('window-size=1200x600');
#driver = webdriver.Chrome(PATH)


driver.get("https://warrior.uwaterloo.ca/Program/GetProgramDetails?courseId=cc2a16d7-f148-461e-831d-7d4659726dd1&semesterId=b0d461c3-71ea-458e-b150-134678037221")

login()
todayDate(5)
selectProgram()
accept()
noAddCart()
lastStep()
driver.quit()
addevent(todayDate(5) + " 19:00" , "Gym booking for " + todayDate(5))

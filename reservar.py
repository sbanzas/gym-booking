import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time
import telebot as bot

USER = "rubenfb14@gmail.com"
PASS = "***REMOVED***"

CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
LOCAL_CHROMEDRIVER_PATH = './chromedriver'

chrome_bin = os.environ.get('GOOGLE_CHROME_BIN', "chromedriver")
options = webdriver.ChromeOptions()
options.binary_location = chrome_bin
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument('headless')
options.add_argument('window-size=1200x600')
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)

driver.get("https://crosshero.com/athletes/sign_in")
driver.current_url
user = driver.find_element_by_id("athlete_email") 
user.send_keys(USER)
pasw = driver.find_element_by_id("athlete_password")
pasw.send_keys(PASS)
driver.find_element_by_name("commit").click()
driver.get("https://crosshero.com/dashboard/classes?date=" + str(tomorrow.day) + "%2F" +  str(tomorrow.month) + "%2F" +  str(tomorrow.year) + "&program_id=599ea218204351000ec9130d")
reservation_hour = driver.find_elements_by_xpath("//*[contains(text(), '19:30')]")
reservation_hour[0].click()
try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "classes-sign-in"))
    )
except:
    print("no quedan sitios")
    
time.sleep(10) 
driver.save_screenshot('screenie.png')
bot.sendfile("./screenie.png")

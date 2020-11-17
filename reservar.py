import datetime
import os
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import telebot as bot

USER = "rubenfb14@gmail.com"
PASS = "***REMOVED***"

CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
LOCAL_CHROMEDRIVER_PATH = './chromedriver'

def configure_chromedriver():
    chrome_bin = os.environ.get('GOOGLE_CHROME_BIN', 'chromedriver')
    options = webdriver.ChromeOptions()
    #comment to use locally
    options.binary_location = chrome_bin
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    #Comment this if you want to see the browser (only locally)
    options.add_argument('headless')
    options.add_argument('window-size=1200x600')
    #Use LOCAL_CHROMEDRIVER_PATH here if you execute it locally
    return webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)
	
def nav_to_booking_page(driver):
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    driver.get("https://crosshero.com/athletes/sign_in")
    user = driver.find_element_by_id("athlete_email")
    pasw = driver.find_element_by_id("athlete_password")
    user.send_keys(USER)
    pasw.send_keys(PASS)
    driver.find_element_by_name("commit").click()
    driver.get("https://crosshero.com/dashboard/classes?date=" + str(tomorrow.day)
        + "%2F" +  str(tomorrow.month) + "%2F"
                +  str(tomorrow.year) + "&program_id=599ea218204351000ec9130d")
    reservation_hour = driver.find_elements_by_xpath("//*[contains(text(), '19:30')]")
    reservation_hour[0].click()
 
def get_signin_button(driver):
    button = None
    try:
        button = driver.find_element_by_id("classes-sign-in")
    except NoSuchElementException:
        driver.refresh()
    return button

def main():
    driver = configure_chromedriver()
    nav_to_booking_page(driver)
    start = time.time()
    elapsed = 0
    button = None
    while (button is None and elapsed < 60):
        elapsed = int(time.time() - start)
        button = get_signin_button(driver)
        print(elapsed)

    if elapsed >= 60:
        print("non quedan sitios")
    elif button is not None:
        button.click()    
        
    time.sleep(2)
    driver.save_screenshot('screenie.png')
    bot.sendfile("./screenie.png")

if __name__ == "__main__":
    main()

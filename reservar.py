import datetime
import os
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import telebot as bot

USER = os.environ.get('USER')
PASS = os.environ.get('PASS')

CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
LOCAL_CHROMEDRIVER_PATH = './chromedriver'
IS_LOCAL = True

def configure_chromedriver():
    chrome_bin = os.environ.get('GOOGLE_CHROME_BIN', 'chromedriver')
    options = webdriver.ChromeOptions()
    if not IS_LOCAL:
        options.binary_location = chrome_bin
        options.add_argument('headless')
        executable_path = CHROMEDRIVER_PATH
    else:
        executable_path = LOCAL_CHROMEDRIVER_PATH
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument('window-size=1200x600')
    return webdriver.Chrome(executable_path=executable_path, options=options)
	
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

    if elapsed > 59:
        print("non quedan sitios")
    elif button is not None:
        button.click()    
        
    time.sleep(2)
    driver.save_screenshot('screenie.png')
    bot.sendfile("./screenie.png")

if __name__ == "__main__":
    main()

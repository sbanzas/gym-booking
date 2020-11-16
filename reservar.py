import datetime
from selenium import webdriver

USER = "rubenfb14@gmail.com"
PASS = "***REMOVED***"

GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

LOCAL_CHROMEDRIVER_PATH = './chromedriver'

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
#comment the following line to use in local env.
chrome_options.binary_location = GOOGLE_CHROME_PATH

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options) 
driver.get("https://crosshero.com/athletes/sign_in")
driver.current_url
user = driver.find_element_by_id("athlete_email") 
user.send_keys(USER)
pasw = driver.find_element_by_id("athlete_password")
pasw.send_keys(PASS)
driver.find_element_by_name("commit").click()
driver.get("https://crosshero.com/dashboard/classes?date=" + str(tomorrow.day) + "%2F" +  str(tomorrow.month) + "%2F" +  str(tomorrow.year) + "&program_id=599ea218204351000ec9130d")
driver.current_url
reservation_hour = driver.find_elements_by_xpath("//*[contains(text(), '15:00')]")
reservation_hour[0].click()
driver.find_element_by_id("classes-sign-in").click()

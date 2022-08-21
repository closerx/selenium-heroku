from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
import os,time

CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', '/usr/local/bin/chromedriver')
GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN', '/usr/bin/google-chrome')


options = Options()
options.binary_location = GOOGLE_CHROME_BIN
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.headless = True

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH , chrome_options=options)


url = 'https://jobs.sa'
driver.get(url)
time.sleep(3)
home=driver.find_elements_by_class_name("spritejobs box")
home.click()
time.sleep(2)
print(driver.page_source)

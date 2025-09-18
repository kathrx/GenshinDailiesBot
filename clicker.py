# import webbrowser

# url = "https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=e202102251931481"

# webbrowser.open(url)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome()
driver.get("https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=e202102251931481")
# button = driver.find_element_by_id('buttonID')

time.sleep(5)

span = driver.find_element(By.XPATH, "//span[contains(@class, 'guide-close')]")
span.click()

time.sleep(2)

sign_items = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'sign-item')]"))
)

sign_items[0].click()


input("Press Enter to close the browser...")  
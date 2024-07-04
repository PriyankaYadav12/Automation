import pandas as pd
from selenium import webdriver
import os
import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--allow-insecure-localhost')
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://portal.zinghr.com/2015/pages/authentication/zing.aspx?ccode=clover")
driver.maximize_window()
time.sleep(5)
file_path = 'inputfile.xlsx'
df = pd.read_excel(file_path)

def element_exists(by, value, timeout=5):
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))
        return True
    except TimeoutException:
        return False

time.sleep(5)
textbox1 = driver.find_element(By.ID, 'txtEmpCode')  
textbox1.clear()  # Clear any existing text
textbox1.send_keys("CI11961")  

textbox2 = driver.find_element(By.ID, 'txtPassword')  
textbox2.clear()  # Clear any existing text
textbox2.send_keys("Priyanka@123")  
time.sleep(1)
submit_button = driver.find_element(By.ID, 'btnLogin')  
submit_button.click()    
time.sleep(10) 

#CLICK ON cALc[@id="scrollable-auto-tabpanel-0"]/div/div/div/div[1]/div[2]/div/div/div/div[3]/div/div


if element_exists(By.XPATH, '//*[@id="scrollable-auto-tabpanel-0"]/div/div/div/div[1]/div[2]/div/div/div/div[2]/button/span/a'):
    calc_element = driver.find_element(By.XPATH, '//*[@id="scrollable-auto-tabpanel-0"]/div/div/div/div[1]/div[2]/div/div/div/div[2]/button/span/a')
    calc_element.click()
    print('found')

else:
    calc_element = driver.find_element(By.XPATH, '//*[@id="scrollable-auto-tabpanel-0"]/div/div/div/div[1]/div[2]/div/div/div/div[2]/button/span/a')
    calc_element.click()
    print('Not found')    
time.sleep(10)

#select current date and click on it
# date_picker = driver.find_element(By.ID, 'attentance-marker')  # Replace with the actual ID or selector
# date_picker.click()

file_path = 'inputfile.xlsx'
df = pd.read_excel(file_path)

current_date = datetime.now().strftime("%Y-%m-%d")

date_element = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[3]/div/div/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/button')  # Adjust the selector as needed
date_element.click()
time.sleep(1)  

proceed_button = driver.find_element(By.ID, 'MuiButton-label')  # Replace with the actual ID or selector
proceed_button.click()
time.sleep(2) 

driver.quit()

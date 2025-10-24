import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL="https://www.saucedemo.com/"
USERNAME= "standard_user"
PASSWORD= "secret_sauce"

def get_driver ():
    driver= webdriver.Chrome(
        service= Service(ChromeDriverManager().install())
        )
    time.sleep(5)
    return driver

def login_saucedemo(driver):
    driver.get(URL)
    
    driver.find_element(By.NAME,"user-name").send_keys(USERNAME)
    driver.find_element(By.NAME,"password").send_keys(PASSWORD)
    driver.find_element(By.ID,"login-button").click()
    
    time.sleep(5)
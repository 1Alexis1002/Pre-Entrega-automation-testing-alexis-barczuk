import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils.helpers import login_saucedemo,get_driver
from selenium.webdriver.common.by import By

@pytest.fixture

def driver():
    driver = get_driver()
    yield driver
    driver.quit()
def test_login(driver):
    
    login_saucedemo(driver)
    assert "/inventory.html" in driver.current_url
    titulo = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
    assert titulo== "Products"
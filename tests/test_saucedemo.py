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
    
def test_catalogo(driver):
    login_saucedemo(driver)
    
    products= driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0
    
    primer_producto= products[0]
    
    titulo= primer_producto.find_element(By.CLASS_NAME, 'inventory_item_name').text
    desc= primer_producto.find_element(By.CLASS_NAME, 'inventory_item_desc').text
    precio= primer_producto.find_element(By.CLASS_NAME, 'inventory_item_price').text
    assert titulo == "Sauce Labs Backpack"
    assert desc != ""
    assert precio == "$29.99"

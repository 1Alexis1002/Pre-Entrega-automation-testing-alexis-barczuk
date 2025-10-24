from time import sleep
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
    title = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
    assert title== "Products"
    
def test_catalogo(driver):
    login_saucedemo(driver)
    
    products= driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0
    
    primer_product= products[0]
    
    title= primer_product.find_element(By.CLASS_NAME, 'inventory_item_name').text
    desc= primer_product.find_element(By.CLASS_NAME, 'inventory_item_desc').text
    precio= primer_product.find_element(By.CLASS_NAME, 'inventory_item_price').text
    assert title == "Sauce Labs Backpack"
    assert desc != ""
    assert precio == "$29.99"
    
def test_carrito (driver):
    login_saucedemo(driver)
    add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_button.click()
    sleep(1)
    
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert badge == "1"

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    cart_item = driver.find_element(By.CLASS_NAME, "cart_item")
    nombre = cart_item.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = cart_item.find_element(By.CLASS_NAME, "inventory_item_price").text
    assert nombre == "Sauce Labs Backpack"
    assert precio == "$29.99"
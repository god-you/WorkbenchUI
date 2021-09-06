from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import win32api

"""选择显性等待定位方式"""
def explicit_wait(driver, times, method, value):
    if method == 'id':
        method = By.ID
    elif method == 'name':
        method = By.NAME
    elif method == 'xpath':
        method = By.XPATH
    elif method == 'css':
        method = By.CSS_SELECTOR
    else:
        print("Please select one of id, name, xpath, css for positioning.")
    fele = WebDriverWait(driver, times).until(EC.visibility_of_element_located((method, value)))
    return fele

"""选择浏览器驱动"""
def drivers(browser):
    if browser == 'Firefox':
        driver = webdriver.Firefox()
        return driver
    elif browser == 'Chrome':
        driver = webdriver.Chrome()
        return driver
    elif browser == 'IE':
        driver = webdriver.Ie()
        return driver
    else:
        print("Please choose one of Firefox, Chrome, IE three browsers to use.")

def drop_down_menu():
    win32api.keybd_event(40, 0, 0, 0)
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import win32api
import time

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

# 本地目录存在路径
def path():
    local_path = "C:\\Users\\ASUS\\Desktop\\rongda_digital\\workbench"
    return local_path

def export_path():
    file_path = "C:\\Users\\ASUS\\Downloads\\"
    return file_path

def time_limit():
    time1 = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))

    if int(time1[-2:-1:]) == 3 or int(time1[-2:-1:]) == 4 or int(time1[-2:-1:]) == 5:
        time2 = int(time1)
        time3 = time2 + 70
    else:
        time2 = int(time1)
        time3 = time2 + 30
    return time3
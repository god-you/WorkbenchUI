from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from util import explicit_wait as etwait

def login_In(driver):
        driver.maximize_window()
        url = 'https://svc.roadtel.top/RDWork/login.html'
        driver.get(url)
        driver.find_element_by_xpath('//*[@id="details-button"]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="proceed-link"]').click()
        # 输入账号
        driver.find_element_by_id('employess_number').send_keys('zlx')
        # 输入密码
        driver.find_element_by_id('employess_password').send_keys('1')
        # 点击“登录”
        driver.find_element_by_id('login_btn').click()
        sleep(1)
        try:
                # 确认登录
                driver.find_element_by_id('sureid').click()
        except Exception:
                pass

        # 下拉查找对应目录
        sleep(5)
        ele1 = etwait(driver, 30, 'xpath', '//*[@id="menuul"]/li[1]/a')
        ele1.click()
        ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()

def login(driver):
        u"""无需下拉查找对应目录"""
        driver.maximize_window()
        url = 'https://svc.roadtel.top/RDWork/login.html'
        driver.get(url)
        driver.find_element_by_xpath('//*[@id="details-button"]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="proceed-link"]').click()
        # 输入账号
        driver.find_element_by_id('employess_number').send_keys('zlx')
        # 输入密码
        driver.find_element_by_id('employess_password').send_keys('1')
        # 点击“登录”
        driver.find_element_by_id('login_btn').click()
        sleep(1)
        try:
                # 确认登录
                driver.find_element_by_id('sureid').click()
        except Exception:
                pass
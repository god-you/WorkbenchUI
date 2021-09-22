# -*- coding:UTF8 -*-
import unittest
from selenium import webdriver
import time
from case.login_in import login
from common.util import explicit_wait as etwait, export_path, time_limit
from common import settings
import os
from selenium.webdriver.chrome.options import Options

options = Options()
options.debugger_address = '127.0.0.1:8001'

settings.create_dir()
pict_path = settings.pictsave_path()

class Agent_real_time_status(unittest.TestCase):
    u"""坐席实时监控"""

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        # login(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test01full_screen(self):
        u"""设置全屏"""
        # 进入客户信息目录
        # etwait(self.driver, 10, 'xpath', '//a[contains(text(),"监控管理")]').click()
        # 进入坐席实时状态菜单
        etwait(self.driver, 10, 'xpath', '//a[text()="坐席实时状态"]').click()
        # 切换iframe窗口
        frame1 = self.driver.find_element_by_css_selector('.iframeClass')
        self.driver.switch_to.frame(frame1)
        # 设置全屏
        client_width1 = self.driver.execute_script("return document.body.clientWidth")
        client_height1 = self.driver.execute_script("return document.body.clientHeight")
        etwait(self.driver, 30, 'id', 'quanpinbt').click()
        client_width2 = self.driver.execute_script("return document.body.clientWidth")
        client_height2 = self.driver.execute_script("return document.body.clientHeight")
        # 判断用例是否通过
        if client_width1 > client_width2 and client_height1 > client_height2:
            pass
        else:
            self.driver.save_screenshot(pict_path + 'agent_real-time_status_full_screen.png')
        self.assertNotEqual(client_width1, client_width2)
        self.assertNotEqual(client_height1, client_height2)

    def test02query(self):
        self.driver.find_element_by_id('company').click()
        etwait(self.driver, 30, 'xpath', '//*[@id="io01000310001"]/td[1]/input').click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/a[1]').click()
        self.driver.find_element_by_id('fenji').send_keys(89100497)
        self.driver.find_element_by_id('gonghao').send_keys(4867)
        self.driver.find_element_by_xpath('//*[@id="test"]/div[1]/div[2]/div[2]/div[1]/div/div').click()
        etwait(self.driver, 30, 'xpath', '//*[@id="test"]/div[1]/div[2]/div[2]/div[1]/div/div/dl/dd[2]').click()
        self.driver.find_element_by_id('zuowei').send_keys(89100497)
        self.driver.find_element_by_xpath('//*[@id="test"]/div[1]/div[2]/div[2]/div[4]/label').click()
        # ele1 = self.driver.

if __name__ == "__main__":
    unittest.main(verbosity=2)
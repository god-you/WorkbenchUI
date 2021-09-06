import unittest
from selenium import webdriver
from case.login_in import login_In
import time
from util import explicit_wait as etwait
import settings
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

settings.create_dir()
pict_path = settings.pictsave_path()

class Desensitization_record(unittest.TestCase):
    u"""操作记录"""

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        login_In(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test01desenrcdqur(self):
        u"""脱敏记录查询"""
        # # 进入系统管理目录
        ele2 = etwait(self.driver, 10, 'xpath', '//*[@id="menuul"]/li[26]/a')
        ele2.click()
        ActionChains(self.driver).key_down(Keys.ARROW_DOWN).perform()
        time.sleep(1)
        # 进入脱敏记录菜单
        self.driver.find_element_by_xpath('//*[@id="系统管理"]/li[11]/a').click()
        # 切换iframe窗口
        frame = self.driver.find_element_by_css_selector('.iframeClass')
        self.driver.switch_to.frame(frame)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="agent"]').send_keys('panyun')
        ele1 = self.driver.find_element_by_xpath('//*[@id="start_time"]')
        ele1.clear()
        ele1.send_keys('2021-05-01 00:00:00')
        ele2 = self.driver.find_element_by_xpath('//*[@id="end_time"]')
        ele2.clear()
        ele2.send_keys('2021-05-31 23:59:59')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/ul/li[1]/button').click()
        ele4 = self.driver.find_element_by_id('addtable')
        datanum = len(ele4.find_elements_by_tag_name('tr'))
        if datanum == 1:
            pass
        else:
            self.driver.save_screenshot(pict_path + 'desenrcdqur.png')
        self.assertEqual(datanum, 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)
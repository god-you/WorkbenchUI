import unittest
from selenium import webdriver
from case.login_in import login_In
import time
from util import explicit_wait as etwait, drop_down_menu
import settings
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import win32api

settings.create_dir()
pict_path = settings.pictsave_path()

class Forgpass(unittest.TestCase):
    u"""忘记密码"""

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        login_In(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test01query(self):
        u"""查询"""
        # 进入系统管理目录
        ele2 = etwait(self.driver, 10, 'xpath', '//*[@id="menuul"]/li[26]/a')
        ele2.click()
        drop_down_menu()
        # ActionChains(self.driver).key_down(Keys.ARROW_DOWN).perform()
        time.sleep(1)
        # 进入忘记密码菜单
        self.driver.find_element_by_xpath('//*[@id="系统管理"]/li[5]').click()
        # 切换至iframe窗口
        frame = self.driver.find_element_by_css_selector('.iframeClass')
        self.driver.switch_to.frame(frame)
        time.sleep(1)
        # 填写查询条件
        self.driver.find_element_by_xpath('//*[@id="denglunub"]').send_keys('shulihua')
        self.driver.find_element_by_xpath('//*[@id="yuangongnub"]').send_keys('舒丽华')
        ele1 = self.driver.find_element_by_xpath('//*[@id="starttime"]')
        ele1.clear()
        ele1.send_keys('2021-08-24')
        ele2 = self.driver.find_element_by_xpath('//*[@id="endtime"]')
        ele2.clear()
        ele2.send_keys('2021-08-24')
        time.sleep(1)
        # 点击‘查询’按钮
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/ul/li[1]/button').click()
        time.sleep(2)
        tbody = self.driver.find_element_by_xpath('//*[@id="addtable"]')
        datanum = len(tbody.find_elements_by_tag_name('tr'))
        count = self.driver.find_element_by_xpath('//*[@id="addtable"]/tr[1]/td[2]').text
        if datanum >= 1 and count == 'shulihua':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'forqur.png')
        self.assertNotEqual(datanum, 0)
        self.assertEqual(count, 'shulihua')

if __name__ == "__main__":
    unittest.main(verbosity=2)
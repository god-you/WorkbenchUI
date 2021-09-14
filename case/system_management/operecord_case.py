import unittest
from selenium import webdriver
from case.login_in import login_In
import time
from common.util import explicit_wait as etwait,drop_down_menu
from common import settings

settings.create_dir()
pict_path = settings.pictsave_path()

class Operecord(unittest.TestCase):
    u"""操作记录"""

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        login_In(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test01operlogqur(self):
        u"""操作日志查询"""
        # 进入系统管理目录
        ele2 = etwait(self.driver, 10, 'xpath', '//*[@id="menuul"]/li[26]/a')
        ele2.click()
        drop_down_menu()
        time.sleep(1)
        # 进入操作日志菜单
        self.driver.find_element_by_xpath('//*[@id="系统管理"]/li[10]/a').click()
        # 切换iframe窗口
        frame1 = self.driver.find_element_by_css_selector('.iframeClass')
        self.driver.switch_to.frame(frame1)
        frame2 = self.driver.find_element_by_xpath('//div[@class="newPages"]/iframe')
        self.driver.switch_to.frame(frame2)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="agent"]').send_keys('zlx')
        self.driver.find_element_by_xpath('//*[@name="employess_name"]').send_keys('周琳霞')
        self.driver.find_element_by_xpath('//*[@id="start_time"]').clear()
        self.driver.find_element_by_xpath('//*[@id="start_time"]').send_keys('2021-08-25 19:16:00')
        self.driver.find_element_by_xpath('//*[@id="end_time"]').clear()
        self.driver.find_element_by_xpath('//*[@id="end_time"]').send_keys('2021-08-25 19:16:06')
        self.driver.find_element_by_xpath('//*[@id="url"]').send_keys('getAgentPlanInfo.html')
        self.driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/ul/li[1]/button').click()
        time.sleep(30)
        ele1 = etwait(self.driver, 10, 'id', 'addtable')
        datanum = len(ele1.find_elements_by_tag_name('tr'))
        if datanum == 1:
            pass
        else:
            self.driver.save_screenshot(pict_path + 'operlogqur.png')
        self.assertEqual(datanum, 1)

    def test02onliusequr(self):
        u"""在线用户查询"""
        # 切换iframe窗口
        self.driver.switch_to.parent_frame()
        # 切换至在线用户页面
        ele1 = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/img')
        self.driver.execute_script("arguments[0].click();", ele1)
        time.sleep(2)
        # 切换至其它iframe窗口
        frame2 = self.driver.find_element_by_xpath('//div[@class="newPages"]/iframe')
        self.driver.switch_to.frame(frame2)
        # 填写查询信息
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys('周琳霞')
        self.driver.find_element_by_xpath('//*[@id="log_name"]').send_keys('zlx')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/ul/li[1]/button').click()
        time.sleep(2)
        ele2 = self.driver.find_element_by_xpath('//*[@id="addtable"]')
        datanum = len(ele2.find_elements_by_tag_name('tr'))
        if datanum >= 1:
            pass
        else:
            self.driver.save_screenshot(pict_path + 'onliusequr.png')
        self.assertNotEqual(datanum, 0)

    def test03Login_record_qur(self):
        u"""登入记录查询"""
        # 切换iframe窗口
        self.driver.switch_to.parent_frame()
        # 切换至在线用户页面
        ele1 = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[3]/img')
        self.driver.execute_script("arguments[0].click();", ele1)
        time.sleep(2)
        # 切换至其它iframe窗口
        frame2 = self.driver.find_element_by_xpath('//div[@class="newPages"]/iframe')
        self.driver.switch_to.frame(frame2)
        # 填写查询信息
        self.driver.find_element_by_xpath('//*[@id="log_name"]').send_keys('zlx')
        ele2 = self.driver.find_element_by_xpath('//*[@id="start_time"]')
        ele2.clear()
        ele2.send_keys('2021-08-24 00:00:00')
        ele3 = self.driver.find_element_by_xpath('//*[@id="end_time"]')
        ele3.clear()
        ele3.send_keys('2021-08-24 23:59:59')
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys('周琳霞')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/ul/li[1]/button').click()
        time.sleep(2)
        ele4= self.driver.find_element_by_xpath('//*[@id="addtable"]')
        datanum = len(ele4.find_elements_by_tag_name('tr'))
        if datanum == 1:
            pass
        else:
            self.driver.save_screenshot(pict_path + 'Login_record_qur.png')
        self.assertEqual(datanum, 6)

if __name__ == "__main__":
    unittest.main(verbosity=2)
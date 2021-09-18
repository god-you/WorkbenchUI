# -*- coding:UTF8 -*-
import unittest
from selenium import webdriver
import time
from case.login_in import login
from common.util import explicit_wait as etwait, export_path, time_limit
from common import settings
import os

settings.create_dir()
pict_path = settings.pictsave_path()

class My_Contact_History(unittest.TestCase):
    u"""客户管理"""

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        login(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test01query(self):
        u"""查询"""
        # 进入客户信息目录
        etwait(self.driver, 10, 'xpath', '//a[contains(text(),"客户信息")]').click()
        # 进入我的联络历史菜单
        etwait(self.driver, 10, 'xpath', '//a[text()="我的联络历史"]').click()
        # 切换iframe窗口
        frame1 = self.driver.find_element_by_css_selector('.iframeClass')
        self.driver.switch_to.frame(frame1)
        # 查询联络历史
        etwait(self.driver, 30, 'id', 'lxdh').send_keys('13266732466')
        ele1 = self.driver.find_element_by_id('date')
        ele1.clear()
        ele1.send_keys('2021-02-15')
        ele2 = self.driver.find_element_by_id('endDate')
        ele2.clear()
        ele2.send_keys('2021-03-15')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/ul/li[1]/button').click()
        # 判断用例是否通过
        etwait(self.driver, 30, 'xpath', '//*[@id="addtable"]/tr[1]/td[2]')
        ele1 = self.driver.find_element_by_id('addtable')
        datanum = ele1.find_elements_by_tag_name('tr')
        if datanum == 4:
            pass
        else:
            self.driver.save_screenshot(pict_path + 'my_contact_history_query.png')
        self.assertEqual(datanum, 4)

    def test02check(self):
        u"""查看"""
        # 查看我的联络历史详情
        self.driver.find_element_by_xpath('//*[@id="addtable"]/tr[1]/td[1]/input').click()
        self.driver.find_element_by_xpath('//*[@id="caozuo"]/button[1]').click()
        text1 = etwait(self.driver, 30, 'xpath', '//div[contains(text(),"详细信息")]').text
        time.sleep(0.5)
        self.driver.find_element_by_xpath('/html/body/div[5]/div[3]/a').click()
        if text1 == "详细信息":
            pass
        else:
            self.driver.save_screenshot(pict_path + "my_contact_history_check.png")
        self.assertEqual(text1, '详细信息')

    def test03export(self):
        u"""导出"""
        # 导出我的联络历史数据
        file_path = export_path()
        files1 = os.listdir(file_path)
        num1 = len(files1)
        self.driver.find_element_by_xpath('//*[@id="caozuo"]/button[2]').click()
        time1 = time_limit()
        time2 = time.strftime("%Y-%m-%d ", time.localtime(time.time()))
        # 判断是否导出成功
        while int(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))) <= time1:
            files2 = os.listdir(file_path)
            num2 = len(files2)
            if num2 == num1 + 1:
                for file in files2:
                    name = 'Excel_' + time2
                    if name in file and file.endswith('.xlsx'):
                        file_name = "C:\\Users\\ASUS\\Downloads\\" + file
                        result = os.path.exists(file_name)
                        if result:
                            f = open(file_name)
                            f.close()
                            os.remove(file_name)
                            break
                        self.assertEqual(result, True)
            else:
                continue

if __name__ == "__main__":
    unittest.main(verbosity=2)
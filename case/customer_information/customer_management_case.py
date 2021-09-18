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

class Customer_Management(unittest.TestCase):
    u"""客户管理"""

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        login(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test01add(self):
        u"""新增"""
        # 进入客户信息目录
        etwait(self.driver, 10, 'xpath', '//a[contains(text(),"客户信息")]').click()
        # 进入客户管理菜单
        etwait(self.driver, 10, 'xpath', '//a[text()="客户管理"]').click()
        # 切换iframe窗口
        frame1 = self.driver.find_element_by_css_selector('.iframeClass')
        self.driver.switch_to.frame(frame1)
        # 新增客户信息
        etwait(self.driver, 10, 'xpath', '//*[@id="caozuo"]/button[1]').click()
        etwait(self.driver, 10, 'xpath', '//*[@id="add_khxm"]').send_keys('白晓禿')
        self.driver.find_element_by_xpath('//*[@id="add_sjhm"]').send_keys(18682636263)
        self.driver.find_element_by_id('add_lxdh').send_keys(5632466)
        self.driver.find_element_by_xpath('//div[4]/div[3]/a[1]').click()
        # 判断用例是否通过
        text1 = etwait(self.driver, 10, 'xpath', '/html/body/div[11]/div[1]').text
        self.driver.find_element_by_xpath('//div[2]/a[contains(text(),"确定")]').click()
        if text1 == "操作成功！":
            pass
        else:
            self.driver.save_screenshot(pict_path + 'customer_management_add.png')
        self.assertEqual(text1, "操作成功！")

    def test02query(self):
        u"""查询"""
        # 重置页面
        self.driver.switch_to.default_content()
        etwait(self.driver, 10, 'xpath', '//a[text()="客户管理"]').click()
        frame1 = self.driver.find_element_by_css_selector('.iframeClass')
        self.driver.switch_to.frame(frame1)
        # 查询客户信息
        self.driver.find_element_by_id('sjhm').send_keys(18682636263)
        self.driver.find_element_by_id('lxdh').send_keys(5632466)
        self.driver.find_element_by_id('khxm').send_keys('白晓禿')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/ul/li[1]/button').click()
        # 判断用例是否通过
        etwait(self.driver, 10, 'xpath', '//*[@id="addtable"]/tr/td[2]')
        ele1 = self.driver.find_element_by_id('addtable')
        datanum = len(ele1.find_elements_by_tag_name('tr'))
        if datanum == 1:
            pass
        else:
            self.driver.save_screenshot(pict_path + 'customer_management_query.png')
        self.assertEqual(datanum, 1)

    def test03edit(self):
        u"""编辑"""
        # 修改客户信息
        self.driver.find_element_by_xpath('//*[@id="addtable"]/tr/td[1]/input').click()
        self.driver.find_element_by_xpath('//*[@id="caozuo"]/button[2]').click()
        etwait(self.driver, 10, 'id', 'edit_csrq').send_keys('1994-09-29')
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//div[5]/div[3]/a[1]').click()
        # 判断用例是否通过
        text1 = etwait(self.driver, 10, 'xpath', '/html/body/div[11]/div[1]').text
        etwait(self.driver, 10, 'xpath', '//div[2]/a[contains(text(),"确定")]').click()
        if text1 == "操作成功！":
            pass
        else:
            self.driver.save_screenshot(pict_path + 'customer_management_edit.png')
        self.assertEqual(text1, "操作成功！")

    def test04check(self):
        u"""查看详情"""
        # 查看客户信息详情
        self.driver.find_element_by_css_selector('[onclick="details(0)"]').click()
        text1 = self.driver.find_element_by_xpath('/html/body/div[6]/div[1]').text
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//a[contains(text(),"关闭")]').click()
        # 判断用例是否通过
        if text1 == "详情信息":
            pass
        else:
            self.driver.save_screenshot(pict_path + 'customer_management_edit.png')
        self.assertEqual(text1, "详情信息")

    def test05export(self):
        u"""数据导出"""
        # 导出数据
        file_path = export_path()
        files1 = os.listdir(file_path)
        num1 = len(files1)
        self.driver.find_element_by_xpath('//*[@id="caozuo"]/button[5]/span').click()
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

    def test06delete(self):
        u"""删除"""
        # 删除客户信息
        self.driver.find_element_by_xpath('//*[@id="addtable"]/tr/td[1]/input').click()
        self.driver.find_element_by_xpath('//*[@id="caozuo"]/button[3]').click()
        etwait(self.driver, 10, 'xpath', '//a[contains(text(),"确定")]').click()
        etwait(self.driver, 10, 'xpath', '//div[contains(text(),"暂无数据")]')
        ele1 = self.driver.find_element_by_id('addtable')
        datanum = len(ele1.find_elements_by_tag_name('tr'))
        if datanum == 0:
            pass
        else:
            self.driver.save_screenshot(pict_path + 'customer_management_query.png')
        self.assertEqual(datanum, 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)
# -*- coding:UTF8 -*-
import unittest
from selenium import webdriver
import time
from case.login_in import login
from common.util import explicit_wait as etwait, time_limit
from common import settings

settings.create_dir()
pict_path = settings.pictsave_path()

class Contact_Plan(unittest.TestCase):
    u"""联系计划"""

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
        # 进入联系计划菜单
        etwait(self.driver, 10, 'xpath', '//a[text()="联系计划"]').click()
        # 切换iframe窗口
        frame1 = self.driver.find_element_by_css_selector('.iframeClass')
        self.driver.switch_to.frame(frame1)
        # 新增联系计划
        etwait(self.driver, 30, 'xpath', '//*[@id="caozuo"]/button[1]').click()
        time.sleep(0.5)
        etwait(self.driver, 30, 'id', 'addcompany').click()
        etwait(self.driver, 30, 'xpath', '//*[@id="io010003"]/td[2]/span[3]').click()
        etwait(self.driver, 30, 'id', 'add_khName').send_keys('白晓禿')
        self.driver.find_element_by_id('add_title').send_keys('新增联系计划标题')
        self.driver.find_element_by_id('add_lxInfo').send_keys('18656349853')
        self.driver.find_element_by_id('add_planTime').click()
        etwait(self.driver, 30, 'xpath', '/html/body/div[14]/div[2]/div/span[3]').click()
        etwait(self.driver, 30, 'xpath', '/html/body/div[3]/div[3]/a[1]').click()
        # 判断用例是否通过
        text1 = etwait(self.driver, 30, 'xpath', '/html/body/div[13]/div[1]').text
        etwait(self.driver, 30, 'xpath', '/html/body/div[13]/div[2]/a').click()
        if text1 == "操作成功":
            pass
        else:
            self.driver.save_screenshot(pict_path + 'contact_plan_add.png')
        self.assertEqual(text1, '操作成功')

    def test02query(self):
        u"""查询"""
        # 查询联系计划
        self.driver.find_element_by_id('lxdh').send_keys(18656349853)
        self.driver.find_element_by_id('khxm').send_keys('白晓禿')
        self.driver.find_element_by_id('kfname').send_keys('潘云')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/ul/li[1]/button').click()
        # 判断用例是否通过
        time1 = time_limit()
        while int(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))) <= time1:
            ele1 = self.driver.find_element_by_id('addtable')
            datanum = len(ele1.find_elements_by_tag_name('tr'))
            if datanum == 1:
                break
            else:
                continue
        self.assertEqual(datanum, 1)

    def test03edit(self):
        u"""修改"""
        # 修改联系计划
        self.driver.find_element_by_xpath('//*[@id="addtable"]/tr/td[1]/input').click()
        self.driver.find_element_by_xpath('//*[@id="caozuo"]/button[2]').click()
        etwait(self.driver, 30, 'id', 'add_khName').send_keys('修改后')
        time.sleep(0.5)
        etwait(self.driver, 30, 'xpath', '/html/body/div[3]/div[3]/a[1]').click()
        # 判断用例是否通过
        text1 = etwait(self.driver, 30, 'xpath', '/html/body/div[13]/div[1]').text
        if text1 == "操作成功":
            pass
        else:
            self.driver.save_screenshot(pict_path + 'contact_plan_edit.png')
        self.assertEqual(text1, '操作成功')

    def test04accept(self):
        u"""受理"""
        # 受理联系计划
        self.driver.find_element_by_xpath('//*[@id="addtable"]/tr/td[13]/a[1]').click()
        etwait(self.driver, 30, 'id', 'sl_detail').send_keys('已受理')
        self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/a[1]').click()
        # 判断用例是否通过
        text1 = etwait(self.driver, 30, 'xpath', '/html/body/div[13]/div[1]').text
        if text1 == "操作成功":
            pass
        else:
            self.driver.save_screenshot(pict_path + 'contact_plan_accept.png')
        self.assertEqual(text1, '操作成功')

    def test05check(self):
        u"""查看"""
        # 查看受理详情
        self.driver.find_element_by_xpath('//*[@id="addtable"]/tr/td[13]/a[2]').click()
        # 判断用例是否通过
        text1 = etwait(self.driver, 30, 'xpath', '//div[contains(text(),"受理详情")]').text
        time.sleep(0.5)
        self.driver.find_element_by_xpath('/html/body/div[5]/span[1]/a').click()
        if text1 == "受理详情":
            pass
        else:
            self.driver.save_screenshot(pict_path + 'contact_plan_check.png')
        self.assertEqual(text1, '受理详情')

    def test06delete(self):
        u"""删除"""
        # 删除联系计划
        self.driver.find_element_by_xpath('//*[@id="addtable"]/tr/td[1]/input').click()
        self.driver.find_element_by_xpath('//*[@id="caozuo"]/button[3]').click()
        etwait(self.driver, 30, 'xpath', '/html/body/div[14]/div[2]/a[1]').click()
        # 判断用例是否通过
        time1 = time_limit()
        while int(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))) <= time1:
            ele1 = self.driver.find_element_by_id('addtable')
            datanum = len(ele1.find_elements_by_tag_name('tr'))
            if datanum == 0:
                break
            else:
                continue
        self.assertEqual(datanum, 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)
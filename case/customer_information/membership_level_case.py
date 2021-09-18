# -*- coding:UTF8 -*-
import unittest
from selenium import webdriver
import time
from case.login_in import login
from common.util import explicit_wait as etwait
from common import settings

settings.create_dir()
pict_path = settings.pictsave_path()

class Membership_Level(unittest.TestCase):
    u"""会员等级"""

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
        # 进入会员等级菜单
        etwait(self.driver, 10, 'xpath', '//a[text()="会员等级"]').click()
        # 切换iframe窗口
        frame1 = self.driver.find_element_by_css_selector('.iframeClass')
        self.driver.switch_to.frame(frame1)
        # 新增会员等级数据
        etwait(self.driver, 10, 'xpath', '//*[@id="caozuo"]/button[1]').click()
        etwait(self.driver, 10, 'id', 'add_level_number').send_keys('007')
        self.driver.find_element_by_id('add_level_name').send_keys('黑铁')
        self.driver.find_element_by_id('add_level_desc').send_keys('入门会员')
        time.sleep(0.5)
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/a[1]').click()
        # 判断用例是否通过
        text1 = etwait(self.driver, 30, 'xpath', '/html/body/div[7]/div[1]').text
        self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/a').click()
        if text1 == "操作成功！":
            pass
        else:
            self.driver.save_screenshot(pict_path + 'membership_level_add.png')
        self.assertEqual(text1, '操作成功！')

    def test02edit(self):
        u"""修改"""
        # 修改会员等级数据
        etwait(self.driver, 30, 'xpath', '//*[@id="addtable"]/tr[7]/td[1]/input').click()
        etwait(self.driver, 10, 'xpath', '//*[@id="caozuo"]/button[2]').click()
        etwait(self.driver, 30, 'id', 'edit_level_name').send_keys('编辑后')
        time.sleep(0.5)
        self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/a[1]').click()
        # 判断用例是否通过
        text1 = etwait(self.driver, 30, 'xpath', '/html/body/div[7]/div[1]').text
        self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/a').click()
        if text1 == "操作成功！":
            pass
        else:
            self.driver.save_screenshot(pict_path + 'membership_level_edit.png')
        self.assertEqual(text1, '操作成功！')

    def test03delete(self):
        u"""删除"""
        # 删除会员等级数据
        etwait(self.driver, 30, 'xpath', '//*[@id="addtable"]/tr[7]/td[1]/input').click()
        etwait(self.driver, 10, 'xpath', '//*[@id="caozuo"]/button[3]').click()
        etwait(self.driver, 30, 'xpath', '/html/body/div[7]/div[2]/a[1]').click()
        # 判断用例是否通过
        text1 = etwait(self.driver, 30, 'xpath', '/html/body/div[7]/div[1]').text
        if text1 == "删除成功！":
            pass
        else:
            self.driver.save_screenshot(pict_path + 'membership_level_delete.png')
        self.assertEqual(text1, '删除成功！')

if __name__ == "__main__":
    unittest.main(verbosity=2)
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

class Blacklistmana(unittest.TestCase):
    u"""黑名单管理"""

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        login_In(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test01add(self):
        u"""新增黑名单"""
        # 进入系统 管理目录
        ele2 = etwait(self.driver, 10, 'xpath', '//*[@id="menuul"]/li[26]/a')
        ele2.click()
        drop_down_menu()
        time.sleep(1)
        # 进入黑名单管理菜单
        self.driver.find_element_by_xpath('//*[@id="系统管理"]/li[13]/a').click()
        # 切换iframe窗口
        frame = self.driver.find_element_by_css_selector('.iframeClass')
        self.driver.switch_to.frame(frame)
        # 填写查询条件
        self.driver.find_element_by_css_selector('select#searchType').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="searchType"]/option[2]').click()
        # 点击‘查询’按钮
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/ul/li[1]/button').click()
        # 点击‘新增’按钮
        self.driver.find_element_by_id('createButton').click()
        # 选择添加类型
        self.driver.find_element_by_xpath('//a[contains(text(),"多媒体会话添加")]').click()
        # 填写新增部门信息并确认
        ele1 = etwait(self.driver, 10, 'xpath', '//*[@id="mpocompany"]')
        ele1.click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="departmentUi"]//tbody//tr[1]//span[3]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="mpopUp_qudao"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="channelContent"]/li[1]/input').click()
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="mpopUp_userId"]').send_keys("新增用户ID测试")
        self.driver.find_element_by_xpath('//a[contains(text(),"添加")]').click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        add_ele1 = etwait(self.driver, 30, 'xpath', '/html/body/div[12]/div[1]')
        add_text = add_ele1.text
        self.driver.find_element_by_xpath('/html/body/div[12]/div[2]/a').click()
        if add_text == '全部添加成功':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'blacklistadd.png')
        self.assertEqual(add_text, '全部添加成功')

    def test02query(self):
        u"""查询"""
        # 填写查询条件
        self.driver.find_element_by_css_selector('select#searchType').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="searchType"]/option[2]').click()
        # 点击‘查询’按钮
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/ul/li[1]/button').click()
        time.sleep(2)
        tbody = self.driver.find_element_by_xpath('//*[@id="addtable"]')
        datanum = len(tbody.find_elements_by_tag_name('tr'))
        text1 = self.driver.find_element_by_xpath('//*[@id="addtable"]/tr/td[3]').text
        if datanum >= 1 and text1 == '多媒体会话':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'blacklistqur.png')
        self.assertNotEqual(datanum, 0)

    def test03edit(self):
        u"""修改黑名单"""
        # 选择需修改项
        self.driver.find_element_by_xpath('//*[@id="addtable"]/tr/td[1]/input').click()
        # 点击‘修改’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[2]').click()
        time.sleep(2)
        # 修改黑名单信息并保存
        self.driver.find_element_by_xpath('//*[@id="mpopUp_userId"]').send_keys('编辑后')
        self.driver.find_element_by_xpath('//a[contains(text(),"添加")]').click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        edi_ele1 = etwait(self.driver, 30, 'xpath', '/html/body/div[12]/div[1]')
        edi_text = edi_ele1.text
        self.driver.find_element_by_xpath('/html/body/div[12]/div[2]/a').click()
        if edi_text == '更新成功':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'blacklistedit.png')
        self.assertEqual(edi_text, '更新成功')

    def test04del(self):
        u"""删除部门"""
        # 获取当前页面数据量
        ele1 = self.driver.find_element_by_css_selector('tbody#addtable')
        num1 = len(ele1.find_elements_by_tag_name('tr'))
        # 选择需删除项
        self.driver.find_element_by_xpath('//*[@id="addtable"]/tr/td[1]/input').click()
        # 点击‘删除’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[3]').click()
        time.sleep(2)
        # 确定删除
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        time.sleep(2)
        # 再次获取当前页面数据量，判断数据量是否-1，未-1则截屏保存。
        # 通过断言判断用例是否通过
        ele2 = self.driver.find_element_by_css_selector('tbody#addtable')
        num2 = len(ele2.find_elements_by_tag_name('tr'))
        if num1 - num2 == 1:
            pass
        else:
            self.driver.save_screenshot(pict_path + 'departdel.png')
        time.sleep(1)
        self.assertEqual(num1, num2 + 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)
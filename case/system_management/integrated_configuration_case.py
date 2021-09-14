# -*- coding:UTF8 -*-
import unittest
from selenium import webdriver
from case.login_in import login_In
import time
from common.util import explicit_wait as etwait, drop_down_menu
from common import settings

settings.create_dir()
pict_path = settings.pictsave_path()


class Inteconfig(unittest.TestCase):
    u"""集成配置"""

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        login_In(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test01add(self):
        u"""新增集成配置"""
        # 进入系统管理目录
        ele2 = etwait(self.driver, 10, 'xpath', '//*[@id="menuul"]/li[26]/a')
        ele2.click()
        drop_down_menu()
        # ActionChains(self.driver).key_down(Keys.ARROW_DOWN).perform()
        time.sleep(1)
        # 进入集成配置菜单
        self.driver.find_element_by_xpath('//*[@id="系统管理"]/li[15]/a').click()
        # 切换iframe窗口
        frame = self.driver.find_element_by_css_selector('.iframeClass')
        self.driver.switch_to.frame(frame)
        # 点击‘新增’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[1]').click()
        time.sleep(2)
        # 填写新增员工信息并确认
        ele1 = etwait(self.driver, 10, 'id', 'addcompany')
        ele1.click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="io010002"]/td[1]/input').click()
        self.driver.find_element_by_xpath('//a[contains(text(),"提交")]').click()
        self.driver.find_element_by_id('add_rzAddress').send_keys("新增认证地址")
        self.driver.find_element_by_id('add_name').send_keys('新增集成名称')
        self.driver.find_element_by_id('add_url').send_keys('https://www.localhome.com.cn')
        self.driver.find_element_by_id('add_sort').send_keys(827)
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        add_ele1 = etwait(self.driver, 30, 'xpath', '/html/body/div[10]/div[1]')
        add_text = add_ele1.text
        if add_text == '新增成功':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'inteconfigadd.png')
        self.assertEqual(add_text, '新增成功')

    def test02query(self):
        u"""查询"""
        # 填写查询条件
        self.driver.find_element_by_css_selector('#company').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="io010002"]/td[1]/input').click()
        self.driver.find_element_by_xpath('//*[contains(text(),"提交")]').click()
        # 点击‘查询’按钮
        self.driver.find_element_by_xpath('//button[contains(text(),"查询")]').click()
        time.sleep(2)
        tbody = self.driver.find_element_by_xpath('//*[@id="addtable"]')
        datanum = len(tbody.find_elements_by_tag_name('tr'))
        if datanum >= 1:
            pass
        else:
            self.driver.save_screenshot(pict_path + 'inteconfigqur.png')
        self.assertNotEqual(datanum, 0)

    def test03edit(self):
        u"""修改集成配置信息"""
        # 选择需修改项
        self.driver.find_element_by_xpath('//*[@id="addtable"]/tr/td[1]/input').click()
        # 点击‘修改’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[2]').click()
        time.sleep(2)
        # 修改黑名单信息并保存
        self.driver.find_element_by_id('add_rzAddress').send_keys('编辑后')
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        edi_ele1 = etwait(self.driver, 30, 'xpath', '/html/body/div[10]/div[1]')
        edi_text = edi_ele1.text
        if edi_text == '修改成功':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'inteconfigedit.png')
        self.assertEqual(edi_text, '修改成功')

    def test04del(self):
        u"""删除集成配置信息"""
        # 点击‘查询’按钮刷新数据
        self.driver.find_element_by_xpath('//button[contains(text(),"查询")]').click()
        time.sleep(2)
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
            self.driver.save_screenshot(pict_path + 'inteconfigdel.png')
        time.sleep(1)
        self.assertEqual(num1, num2 + 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)
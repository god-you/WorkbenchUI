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

class Departmana(unittest.TestCase):
    u"""部门管理"""

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        login_In(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test01add(self):
        u"""新增部门"""
        # 进入系统管理目录
        ele2 = etwait(self.driver, 10, 'xpath', '//*[@id="menuul"]/li[26]/a')
        ele2.click()
        drop_down_menu()
        # ActionChains(self.driver).key_down(Keys.ARROW_DOWN).perform()
        time.sleep(1)
        # 进入部门管理菜单
        self.driver.find_element_by_xpath('//li[2]/a[contains(text(),"部门管理")]').click()
        # 切换iframe窗口并选择上级部门
        frame = self.driver.find_element_by_css_selector('.iframeClass')
        self.driver.switch_to.frame(frame)
        self.driver.find_element_by_xpath('//*[@id="io0"]/td[1]/input').click()
        # 点击‘新增’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[1]').click()
        # 填写新增部门信息并确认
        alter_ele1 = etwait(self.driver, 30, 'id', 'org_name')
        alter_ele1.send_keys('新增测试部门')
        time.sleep(1)
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        add_ele1 = etwait(self.driver, 30, 'xpath', '/html/body/div[9]/div[1]')
        add_text = add_ele1.text
        if add_text == '添加成功！':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'depatradd.png')
        self.assertEqual(add_text, '添加成功！')

    def test02edit(self):
        u"""修改部门信息"""
        # 选择需修改项
        self.driver.find_element_by_xpath('//*[@id="io010005"]/td[1]/input').click()
        # 点击‘修改’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[2]').click()
        # 修改角色信息并保存
        self.driver.find_element_by_id('edit_orgName').send_keys('(编辑后)')
        time.sleep(2)
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        edi_ele1 = etwait(self.driver, 30, 'xpath', '/html/body/div[9]/div[1]')
        edi_text = edi_ele1.text
        if edi_text == '更新成功！':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'departedit.png')
        self.assertEqual(edi_text, '更新成功！')

    def test03del(self):
        u"""删除部门"""
        # 选择需删除项
        self.driver.find_element_by_xpath('//*[@id="io010005"]/td[1]/input').click()
        # 点击‘删除’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[3]').click()
        time.sleep(2)
        # 确定删除
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        del_ele1 = etwait(self.driver, 30, 'xpath', '//div[contains(text(),"删除成功！")]')
        del_text = del_ele1.text
        if del_text == '删除成功！':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'departdel.png')
        time.sleep(1)
        self.assertEqual(del_text, '删除成功！')

    def test04config(self):
        u"""修改部门功能配置"""
        # 选择需进行功能配置项
        self.driver.find_element_by_xpath('//*[@id="io010002"]/td[1]/input').click()
        # 点击‘功能配置’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[4]').click()
        time.sleep(2)
        # 进行配置并保存
        self.driver.find_element_by_css_selector('input#qxchooseall1').click()
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        config_ele2 = etwait(self.driver, 30, 'xpath', '/html/body/div[9]/div[1]')
        config_text = config_ele2.text
        if config_text == '修改成功！':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'departcon.png')
        time.sleep(3)
        self.assertEqual(config_text, '修改成功！')

if __name__ == "__main__":
    unittest.main(verbosity=2)
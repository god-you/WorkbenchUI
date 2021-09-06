import unittest
from selenium import webdriver
from case.login_in import login_In
import time
from util import explicit_wait as etwait, drop_down_menu
import settings
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

settings.create_dir()
pict_path = settings.pictsave_path()

class Menuconfig(unittest.TestCase):
    u"""菜单配置"""

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        login_In(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test01add(self):
        u"""新增菜单"""
        # 进入系统管理目录
        ele2 = etwait(self.driver, 10, 'xpath', '//*[@id="menuul"]/li[26]/a')
        ele2.click()
        drop_down_menu()
        time.sleep(1)
        # 进入菜单配置菜单
        self.driver.find_element_by_xpath('//*[@id="系统管理"]/li[7]/a').click()
        # 切换至iframe窗口
        frame = self.driver.find_element_by_css_selector('.iframeClass')
        self.driver.switch_to.frame(frame)
        # 点击‘新增’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[1]').click()
        time.sleep(1)
        # 填写新增菜单信息并确认
        self.driver.find_element_by_xpath('//*[@id="functionname"]').send_keys('新增测试目录')
        self.driver.find_element_by_xpath('//*[@id="xzorder"]').send_keys(10201)
        time.sleep(1)
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        try:
            add_ele1 = etwait(self.driver, 30, 'xpath', '//div[contains(text(),"添加成功")]')
            add_text = add_ele1.text
            time.sleep(3)
            self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
            if add_text == '添加成功':
                pass
            else:
                self.driver.save_screenshot(pict_path + 'menuadd.png')
        except Exception:
            self.driver.save_screenshot(pict_path + 'menuadd.png')
        self.assertEqual(add_text, '添加成功')

    def test02edit(self):
        u"""修改菜单"""
        # 翻页查看新增信息
        ActionChains(self.driver).key_down(Keys.PAGE_DOWN).perform()
        time.sleep(1)
        # 选择需修改项并返回页面顶部
        self.driver.find_element_by_xpath('//tbody[@id="addtable"]/tr[1044]/td/input').click()
        ActionChains(self.driver).key_down(Keys.PAGE_UP).perform()
        time.sleep(1)
        # 点击‘修改’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[2]').click()
        # 修改并保存
        ele1 = etwait(self.driver, 10, 'id', 'up_newfunctionname')
        ele1.send_keys('编辑后')
        time.sleep(1)
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        try:
            add_ele1 = etwait(self.driver, 30, 'xpath', '//div[contains(text(),"修改成功")]')
            add_text = add_ele1.text
            time.sleep(3)
            self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
            if add_text == '修改成功':
                pass
            else:
                self.driver.save_screenshot(pict_path + 'menuedit.png')
        except Exception:
            self.driver.save_screenshot(pict_path + 'menuedit.png')
        self.assertEqual(add_text, '修改成功')

    def test03del(self):
        u"""删除菜单"""
        # 翻页查看新增信息
        ActionChains(self.driver).key_down(Keys.PAGE_DOWN).perform()
        time.sleep(1)
        # 选择需删除项并返回页面顶部
        self.driver.find_element_by_xpath('//tbody[@id="addtable"]/tr[1044]/td/input').click()
        ActionChains(self.driver).key_down(Keys.PAGE_UP).perform()
        time.sleep(1)
        # 点击‘删除’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[3]').click()
        time.sleep(1)
        # 确定删除
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        time.sleep(0.5)
        # 判断是否删除成功，失败则截屏保存。
        # 通过断言判断用例是否通过
        try:
            add_ele1 = etwait(self.driver, 30, 'xpath', '//div[contains(text(),"删除成功")]')
            add_text = add_ele1.text
            time.sleep(3)
            self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
            if add_text == '删除成功':
                pass
            else:
                self.driver.save_screenshot(pict_path + 'menudel.png')
        except Exception:
            self.driver.save_screenshot(pict_path + 'menudel.png')
        self.assertEqual(add_text, '删除成功')

    def test04contr(self):
        u"""部门控制"""
        # 展开二级菜单并选择需设置部门
        self.driver.find_element_by_xpath('//table[@id="treeTable1"]//tr[1]//span[2]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//table[@id="treeTable1"]//tr[2]//input').click()
        # 点击‘部门控制’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[4]').click()
        # 编辑部门控制并确定
        ele1 = etwait(self.driver, 10, 'id', 'AllOrgs')
        ele1.click()
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        alter = self.driver.switch_to.alert
        alter.accept()
        # 判断是否删除成功，失败则截屏保存。
        # 通过断言判断用例是否通过
        try:
            ele1 = etwait(self.driver, 30, 'xpath', '//div[contains(text(),"操作成功")]')
            text1 = ele1.text
            time.sleep(3)
            self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
            if text1 == '操作成功':
                pass
            else:
                self.driver.save_screenshot(pict_path + 'menucon.png')
        except Exception:
            self.driver.save_screenshot(pict_path + 'menucon.png')
        self.assertEqual(text1, '操作成功')

if __name__ == "__main__":
        unittest.main(verbosity=2)
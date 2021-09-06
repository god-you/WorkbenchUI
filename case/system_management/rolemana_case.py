import unittest
from selenium import webdriver
from case.login_in import login_In
import time
from util import explicit_wait as etwait
import settings
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

settings.create_dir()
pict_path = settings.pictsave_path()

class Rolemana(unittest.TestCase):
    u"""角色管理"""

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        login_In(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test01add(self):
        u"""新增角色"""
        # 进入系统管理目录
        ele2 = etwait(self.driver, 10, 'xpath', '//*[@id="menuul"]/li[26]/a')
        ele2.click()
        ActionChains(self.driver).key_down(Keys.ARROW_DOWN).perform()
        time.sleep(1)
        # 进入角色管理菜单
        self.driver.find_element_by_xpath('//*[@id="系统管理"]/li[1]/a').click()
        # 选择上级角色
        frame1 = self.driver.find_element_by_css_selector('.iframeClass')
        self.driver.switch_to.frame(frame1)
        self.driver.find_element_by_xpath('//*[@id="ir0"]/td[1]/input').click()
        # 点击‘新增’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[1]').click()
        # 填写新增角色信息并确认
        alter_ele1 = etwait(self.driver, 30, 'id', 'role_name')
        alter_ele1.send_keys('测试组长')
        self.driver.find_element_by_id('role_money').send_keys('test01')
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        add_ele1 = etwait(self.driver, 30, 'xpath', '/html/body/div[11]/div')
        add_text = add_ele1.text
        if add_text == '添加成功！':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'roleadd.png')
        time.sleep(1)
        self.assertEqual(add_text, '添加成功！')

    def test02edit(self):
        u"""修改角色信息"""
        # 选择需修改项
        self.driver.find_element_by_xpath('//*[@id="ir010008"]/td[1]/input').click()
        # 点击‘修改’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[2]').click()
        # 修改角色信息并保存
        self.driver.find_element_by_id('up_role_name').send_keys('(编辑后)')
        self.driver.find_element_by_id('up_role_orgNum').click()
        edit_ele1 = etwait(self.driver, 30, 'xpath', '//*[@id="up_role_orgNum"]/option[3]')
        edit_ele1.click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        edi_ele1 = etwait(self.driver, 30, 'xpath', '/html/body/div[11]/div')
        edi_text = edi_ele1.text
        if edi_text == '修改成功！':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'roleedit.png')
        time.sleep(1)
        self.assertEqual(edi_text, '修改成功！')

    def test03mana(self):
        u"""权限管理配置"""
        # 选择需配置权限管理项
        self.driver.find_element_by_xpath('//*[@id="ir010008"]/td[1]/input').click()
        # 点击‘权限管理’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[4]').click()
        time.sleep(2)
        # 确认修改权限
        self.driver.find_element_by_xpath('//*[@id="chooseall1"]').click()
        mana_ele1 = etwait(self.driver, 30, 'xpath', '//a[contains(text(),"确定")]')
        time.sleep(1)
        mana_ele1.click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        mana_ele2 = etwait(self.driver, 30, 'xpath', '/html/body/div[11]/div')
        mana_text = mana_ele2.text
        if mana_text == '修改权限成功':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'rolemana.png')
        time.sleep(3)
        self.assertEqual(mana_text, '修改权限成功')

    def test04data(self):
        u"""数据权限配置"""
        # 点击‘数据权限’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[5]').click()
        # 设置数据权限
        '//*[@id="datacontrol"]/div/table/thead/tr/td[2]/div[2]/input'
        self.driver.find_element_by_xpath('//*[@id="datacontrol"]/div/table/thead/tr/td[2]/div[2]/input').click()
        self.driver.find_element_by_id('slChooseAll').click()
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        data_ele = etwait(self.driver, 30, 'xpath', '/html/body/div[11]/div')
        data_text = data_ele.text
        if data_text == '成功':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'roledata.png')
        time.sleep(1)
        self.assertEqual(data_text, '成功')

    def test05del(self):
        u"""删除角色"""
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
            self.driver.save_screenshot(pict_path + 'roledel.png')
        time.sleep(1)
        self.assertEqual(del_text, '删除成功！')

if __name__ == "__main__":
    unittest.main(verbosity=2)
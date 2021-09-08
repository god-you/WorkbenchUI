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

class Softphone(unittest.TestCase):
    u"""软电话配置"""

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        login_In(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test01softphadd(self):
        u"""软电话配置新增"""
        # # 进入系统管理目录
        ele2 = etwait(self.driver, 10, 'xpath', '//*[@id="menuul"]/li[26]/a')
        ele2.click()
        drop_down_menu()
        time.sleep(1)
        # 进入软电话配置菜单
        self.driver.find_element_by_xpath('//*[@id="系统管理"]/li[9]/a').click()
        # 切换iframe窗口
        frame1 = self.driver.find_element_by_css_selector('.iframeClass')
        self.driver.switch_to.frame(frame1)
        # 切换至软电话配置页面
        ele2 = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[3]/img')
        self.driver.execute_script("arguments[0].click();", ele2)
        # 切换至其它iframe窗口
        frame2 = self.driver.find_element_by_xpath('//div[@class="newPages"]/iframe')
        self.driver.switch_to.frame(frame2)
        # 点击新增
        ele1 = etwait(self.driver, 10, 'xpath', '//*[@id="caozuobt"]/button[1]')
        ele1.click()
        # 填写新增信息并确认
        alter_ele1 = etwait(self.driver, 30, 'xpath', '//*[@id="url"]')
        alter_ele1.send_keys('新增软电话URL测试')
        result = self.driver.find_element_by_xpath('//*[@id="is_default"]').is_selected()
        print(result)
        # 判断是否勾选为默认数据，若勾选，则去除勾选状态，否则忽略
        if result:
            self.driver.find_element_by_xpath('//*[@id="is_default"]').click()
        else:
            pass
        self.driver.find_element_by_xpath('//*[@id="addcompany"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="io0"]/td[2]/span[3]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        add_ele1 = etwait(self.driver, 30, 'xpath', '/html/body/div[9]/div[1]')
        add_text = add_ele1.text
        self.driver.find_element_by_xpath('/html/body/div[9]/div[2]/a')
        if add_text == '操作成功！':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'softphadd.png')
        self.assertEqual(add_text, '操作成功！')

    def test02softphquery(self):
        u"""软电话配置查询"""
        time.sleep(1)
        # 点击‘查询’按钮
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/ul/li[1]/button').click()
        time.sleep(2)
        tbody = self.driver.find_element_by_xpath('//*[@id="treeTable1"]/tbody')
        datanum = len(tbody.find_elements_by_tag_name('tr'))
        if datanum >= 1:
            pass
        else:
            self.driver.save_screenshot(pict_path + 'softphqur.png')
        self.assertNotEqual(datanum, 0)

    def test03softphedit(self):
        u"""修改软电话配置信息"""
        # 选择需修改项
        self.driver.find_element_by_xpath('//*[@id="treeTable1"]/tbody/tr[1]/td[1]/input').click()
        # 点击‘修改’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[2]').click()
        # 修改并保存
        ele1 = etwait(self.driver, 10, 'xpath', '//*[@id="url"]')
        ele1.send_keys('编辑后')
        time.sleep(1)
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        edi_ele1 = etwait(self.driver, 30, 'xpath', '/html/body/div[9]/div[1]')
        edi_text = edi_ele1.text
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[9]/div[2]/a').click()
        if edi_text == '操作成功！':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'softphedit.png')
        self.assertEqual(edi_text, '操作成功！')

    def test04softphdel(self):
        u"""删除软电话配置信息"""
        # 选择需修改项
        self.driver.find_element_by_xpath('//*[@id="treeTable1"]/tbody/tr[1]/td[1]/input').click()
        # 点击‘删除’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[3]').click()
        time.sleep(1)
        # 确定删除
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        time.sleep(0.5)
        # 判断是否删除成功，失败则截屏保存。
        # 通过断言判断用例是否通过
        del_ele1 = etwait(self.driver, 30, 'xpath', '/html/body/div[9]/div[1]')
        del_text = del_ele1.text
        self.driver.find_element_by_xpath('/html/body/div[9]/div[2]/a').click()
        if del_text == '删除成功！':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'softphdel.png')
        self.assertEqual(del_text, '删除成功！')

    def test05popupadd(self):
        u"""弹屏配置新增"""
        # 切换iframe窗口
        self.driver.switch_to.parent_frame()
        # 切换至弹屏配置页面
        self.driver.find_element_by_xpath('//div[@class="topTab"]//select').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="topTab"]//select/option[4]').click()
        # 切换至其它iframe窗口
        frame2 = self.driver.find_element_by_xpath('//div[@class="newPages"]/iframe')
        self.driver.switch_to.frame(frame2)
        # 点击新增
        ele1 = etwait(self.driver, 10, 'xpath', '//*[@id="caozuobt"]/button[1]')
        ele1.click()
        # 填写新增信息并确认
        alter_ele1 = etwait(self.driver, 30, 'xpath', '//*[@id="url"]')
        alter_ele1.send_keys('新增弹屏URL测试')
        self.driver.find_element_by_xpath('//*[@id="is_default"]').click()
        self.driver.find_element_by_xpath('//*[@id="addcompany"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="io0"]/td[2]/span[3]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        add_ele1 = etwait(self.driver, 30, 'xpath', '/html/body/div[8]/div[1]')
        add_text = add_ele1.text
        self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/a').click()
        if add_text == '操作成功！':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'softphadd.png')
        self.assertEqual(add_text, '操作成功！')

    def test06softphquery(self):
        u"""弹屏配置查询"""
        time.sleep(1)
        # 点击‘查询’按钮
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/ul/li[1]/button').click()
        time.sleep(2)
        tbody = self.driver.find_element_by_xpath('//*[@id="addtable"]')
        datanum = len(tbody.find_elements_by_tag_name('tr'))
        if datanum >= 1:
            pass
        else:
            self.driver.save_screenshot(pict_path + 'softphqur.png')
        self.assertNotEqual(datanum, 0)

    def test07softphedit(self):
        u"""修改弹屏配置信息"""
        # 选择需修改项
        self.driver.find_element_by_xpath('//*[@id="addtable"]/tr[1]/td[1]/input').click()
        # 点击‘修改’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[2]').click()
        # 修改并保存
        ele1 = etwait(self.driver, 10, 'xpath', '//*[@id="url"]')
        ele1.send_keys('编辑后')
        time.sleep(1)
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        edi_ele1 = etwait(self.driver, 30, 'xpath', '/html/body/div[8]/div[1]')
        edi_text = edi_ele1.text
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/a').click()
        if edi_text == '修改成功！':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'softphedit.png')
        self.assertEqual(edi_text, '修改成功！')

    def test08softphdel(self):
        u"""删除弹屏配置信息"""
        # 选择需修改项
        self.driver.find_element_by_xpath('//*[@id="addtable"]/tr[1]/td[1]/input').click()
        # 点击‘删除’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[3]').click()
        time.sleep(1)
        # 确定删除
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        time.sleep(0.5)
        # 判断是否删除成功，失败则截屏保存。
        # 通过断言判断用例是否通过
        del_ele1 = etwait(self.driver, 30, 'xpath', '/html/body/div[8]/div[1]')
        del_text = del_ele1.text
        self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/a').click()
        if del_text == '删除成功！':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'softphdel.png')
        self.assertEqual(del_text, '删除成功！')

if __name__ == "__main__":
    unittest.main(verbosity=2)
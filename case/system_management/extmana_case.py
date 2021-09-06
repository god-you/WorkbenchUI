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

class Extmana(unittest.TestCase):
    u"""分机管理"""

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        login_In(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test01add(self):
        u"""新增分机"""
        # 进入系统管理目录
        ele2 = etwait(self.driver, 10, 'xpath', '//*[@id="menuul"]/li[26]/a')
        ele2.click()
        ActionChains(self.driver).key_down(Keys.ARROW_DOWN).perform()
        time.sleep(1)
        # 进入分机管理菜单
        self.driver.find_element_by_xpath('//*[@id="系统管理"]/li[3]/a').click()
        # 切换至iframe窗口
        frame = self.driver.find_element_by_css_selector('.iframeClass')
        self.driver.switch_to.frame(frame)
        # 点击‘新增’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[1]').click()
        # 填写新增部门信息并确认
        alter_ele1 = etwait(self.driver, 30, 'id', 'add_number')
        alter_ele1.send_keys('新增分机位置编号')
        self.driver.find_element_by_id('add_IP').send_keys('新增IP编号')
        self.driver.find_element_by_id('add_phonenumber').send_keys('新增话机编号')
        self.driver.find_element_by_id('addcompany').click()
        time.sleep(2)
        add_ele2 = etwait(self.driver, 30, 'xpath', '//div[@id="departmentUi"]//span[contains(text(),"集团总部")]')
        add_ele2.click()
        add_ele3 = etwait(self.driver, 30, 'xpath', '//a[contains(text(),"确定")]')
        add_ele3.click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        add_ele1 = etwait(self.driver, 30, 'xpath', '/html/body/div[10]/div[1]')
        add_text = add_ele1.text
        self.driver.find_element_by_xpath('/html/body/div[10]/div[2]/a').click()
        if add_text == '新增成功':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'extadd.png')
        self.assertEqual(add_text, '新增成功')

    def test02query(self):
        u"""查询"""
        # 填写查询条件
        self.driver.find_element_by_id('searchIP').send_keys('新增IP编号')
        self.driver.find_element_by_xpath('//*[@id="search_number"]').send_keys('新增分机位置编号')
        self.driver.find_element_by_xpath('//*[@id="search_phonenumber"]').send_keys('新增话机编号')
        # 点击‘查询’按钮
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/ul/li[1]/button').click()
        time.sleep(2)
        tbody = self.driver.find_element_by_xpath('//*[@id="addtable"]')
        datanum = len(tbody.find_elements_by_tag_name('tr'))
        if datanum == 1:
            pass
        else:
            self.driver.save_screenshot(pict_path + 'extqur.png')
        self.assertEqual(datanum, 1)


    def test03edit(self):
        u"""修改部门信息"""
        # 选择需修改项
        self.driver.find_element_by_xpath('//*[@id="addtable"]/tr/td[1]/input').click()
        # 点击‘修改’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[2]').click()
        time.sleep(3)
        # 保存
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        edi_ele1 = etwait(self.driver, 30, 'xpath', '/html/body/div[10]/div[1]')
        edi_text = edi_ele1.text
        if edi_text == '修改成功':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'extedit.png')
        self.assertEqual(edi_text, '修改成功')

    def test04del(self):
        u"""删除分机"""
        # 选择需删除项
        self.driver.find_element_by_xpath('//*[@id="addtable"]/tr/td[1]/input').click()
        # 点击‘删除’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[3]').click()
        time.sleep(1)
        # 确定删除
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        time.sleep(3)
        # 判断是否删除成功，失败则截屏保存。
        # 通过断言判断用例是否通过
        tbody = self.driver.find_element_by_xpath('//*[@id="addtable"]')
        datanum = len(tbody.find_elements_by_tag_name('tr'))
        if datanum == 0:
            pass
        else:
            self.driver.save_screenshot(pict_path + 'extqur.png')
        self.assertEqual(datanum, 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)
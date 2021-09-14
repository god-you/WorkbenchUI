import unittest
from selenium import webdriver
import time
from case.login_in import login
from common.util import explicit_wait as etwait
from common import settings

settings.create_dir()
pict_path = settings.pictsave_path()

class AnnouncementTypeConfig(unittest.TestCase):
    u"""首页公告"""

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        login(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test01add(self):
        u"""公告类型配置"""
        # 进入首页公告目录
        self.driver.find_element_by_xpath('//*[contains(text(),"首页公告")]').click()
        # 进入公告类型配置菜单
        etwait(self.driver, 10, 'xpath', '//*[@id="首页公告"]/li[3]/a').click()
        # 切换iframe窗口
        frame1 = self.driver.find_element_by_css_selector('.iframeClass')
        self.driver.switch_to.frame(frame1)
        # 进入新增信息填写页面，填写新增信息并确认
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[1]').click()
        etwait(self.driver, 30, 'xpath', '//*[@id="addname"]').send_keys('新增公告类型测试')
        self.driver.find_element_by_xpath('//*[@id="addcompany"]').click()
        time.sleep(1)
        etwait(self.driver, 30, 'xpath', '//div[1]/div[1]/div[1]/table/tbody/tr[2]/td[2]/span[3]').click()
        etwait(self.driver, 30, 'xpath', '//a[contains(text(),"确定")]').click()
        # 通过弹窗文本判断是否新增成功
        text1 = etwait(self.driver, 30, 'xpath', '/html/body/div[9]/div[1]').text
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[9]/div[2]/a').click()
        if text1 == "新增成功":
            pass
        else:
            self.driver.save_screenshot(pict_path + 'AnnouncementTypeConfigAdd.png')
        # 断言用例是否通过
        self.assertEqual(text1, '新增成功')

    def test02query(self):
        # 选择公司部门并点击查询
        self.driver.find_element_by_xpath('//*[@id="company"]').click()
        time.sleep(1)
        etwait(self.driver, 30, 'xpath', '//*[@id="io010002"]/td[1]/input').click()
        self.driver.find_element_by_xpath('//*[contains(text(),"提交")]').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/ul/li[1]/button').click()
        # 获取首条数据适用公司信息
        text1 = self.driver.find_element_by_xpath('//*[@id="addtable"]/tr[1]/td[4]').text
        # 判断适用公司是否为“苏州分部”，如果是，则直接进行截图判断及断言。如果不是，则等待三秒后再进行截图判断及断言
        if text1 == '苏州分部':
            ele1 = self.driver.find_element_by_xpath('//*[@id="addtable"]')
            datanum = len(ele1.find_elements_by_tag_name('tr'))
            if datanum >= 1:
                pass
            else:
                self.driver.save_screenshot(pict_path + 'AnnouncementTypeConfigQuery.png')
            self.assertNotEqual(datanum, 0)
        else:
            time.sleep(3)
            ele2 = self.driver.find_element_by_xpath('//*[@id="addtable"]')
            datanum = len(ele2.find_elements_by_tag_name('tr'))
            if datanum >= 1:
                pass
            else:
                self.driver.save_screenshot(pict_path + 'AnnouncementTypeConfigQuery.png')
            self.assertNotEqual(datanum, 0)

    def test03edit(self):
        # 选择需编辑项
        self.driver.find_element_by_xpath('//*[@id="addtable"]/tr[1]/td[1]/input').click()
        # 进入修改页面，填写编辑信息并确认
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[2]').click()
        etwait(self.driver, 30, 'xpath', '//*[@id="updatename"]').send_keys('编辑后')
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        # 通过弹窗文本判断是否新增成功
        text1 = etwait(self.driver, 30, 'xpath', '/html/body/div[9]/div[1]').text
        if text1 == "修改成功":
            pass
        else:
            self.driver.save_screenshot(pict_path + 'AnnouncementTypeConfigEdit.png')
        # 断言用例是否通过
        self.assertEqual(text1, '修改成功')

    def test04delete(self):
        time.sleep(1)
        # 选择需删除项
        self.driver.find_element_by_xpath('//*[@id="addtable"]/tr[1]/td[1]/input').click()
        # 点击删除并确认
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[3]').click()
        time.sleep(1)
        etwait(self.driver, 30, 'xpath', '//a[contains(text(),"确定")]').click()
        time.sleep(1)
        # 通过弹窗文本判断是否新增成功
        text1 = etwait(self.driver, 30, 'xpath', '/html/body/div[9]/div[1]').text
        if text1 == "删除成功":
            pass
        else:
            self.driver.save_screenshot(pict_path + 'AnnouncementTypeConfigDelete.png')
        # 断言用例是否通过
        self.assertEqual(text1, '删除成功')
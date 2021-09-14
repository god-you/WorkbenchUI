import unittest
from selenium import webdriver
import time
from case.login_in import login
from common.util import explicit_wait as etwait
from common import settings

settings.create_dir()
pict_path = settings.pictsave_path()

class AnnouncementManagement(unittest.TestCase):
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
        u"""公告管理"""
        # 进入首页公告目录
        self.driver.find_element_by_xpath('//*[contains(text(),"首页公告")]').click()
        # 进入公告管理菜单
        etwait(self.driver, 10, 'xpath', '//*[@id="首页公告"]/li[4]/a').click()
        # 切换iframe窗口
        frame1 = self.driver.find_element_by_css_selector('.iframeClass')
        self.driver.switch_to.frame(frame1)
        # 进入新增公告页面
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[1]').click()
        # 切换到新增公告窗口,填写新增信息并提交
        self.driver.switch_to.frame(0)
        etwait(self.driver, 30, 'xpath', '//div[1]/div[1]/div[1]/form[1]/ul[1]/li[1]/div[1]/div[1]/input').click()
        time.sleep(1)
        etwait(self.driver, 30, 'xpath', '//*[@id="io010002"]/td[2]/span[3]').click()
        self.driver.find_element_by_xpath('//div[1]/div[1]/div[1]/form[1]/ul[1]/li[4]//input').send_keys('新增公告主题测试')
        # 切换到下一级iframe窗口并输入公告正文
        self.driver.switch_to.frame(self.driver.find_element_by_id('ueditor_0'))
        self.driver.find_element_by_css_selector('[class="view"][contenteditable="true"]').send_keys('新增公告正文测试')
        # 切换至上一级iframe窗口并点击提交
        self.driver.switch_to.parent_frame()
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/button[1]').click()
        # 通过弹窗文本判断是否新增成功
        text1 = etwait(self.driver, 30, 'xpath', '//*[@class="layui-layer-content"]').text
        if text1 == '提交成功！':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'AnnouncementManagementAdd.png')
        # 断言用例是否通过
        self.assertEqual(text1, '提交成功！')

    def test02query(self):
        # 切换至上一级iframe窗口
        self.driver.switch_to.parent_frame()
        etwait(self.driver, 30, 'xpath', '//*[@id="addtable"]/tr[1]/td[2]')
        # 填写查询条件并进行查询
        etwait(self.driver, 30, 'css', '[id="company"]').click()
        time.sleep(1)
        etwait(self.driver, 30, 'xpath', '//*[@id="io010002"]/td[1]/input').click()
        self.driver.find_element_by_xpath('//*[contains(text(),"提交")]').click()
        self.driver.find_element_by_css_selector('[id="nitname"]').send_keys('新增公告主题测试')
        self.driver.find_element_by_xpath('//*[@id="lookHide"]/div[2]/div[1]/div[2]/ul/li[1]/button').click()
        # 判断是否结束查询
        etwait(self.driver, 30, 'xpath', '//tr[1]/td[contains(text(),"新增公告主题测试")]')
        ele1 = self.driver.find_element_by_xpath('//*[@id="addtable"]')
        datanum = len(ele1.find_elements_by_tag_name('tr'))
        if datanum >= 1:
            pass
        else:
            self.driver.save_screenshot(pict_path + 'AnnouncementManagementQuery.png')
        self.assertNotEqual(datanum, 0)

    def test03edit(self):
        # 进入公告修改页面
        time.sleep(3.5)
        self.driver.find_element_by_xpath('//*[@id="addtable"]/tr[1]/td[1]/input').click()
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[2]').click()
        # 切换到修改公告窗口,修改公告信息并提交
        self.driver.switch_to.frame(0)
        self.driver.find_element_by_xpath('//div[1]/div[1]/div[1]/form[1]/ul[1]/li[4]//input').send_keys('编辑后')
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/button[1]').click()
        # 通过弹窗文本判断是否新增成功
        text1 = etwait(self.driver, 30, 'xpath', '//*[@class="layui-layer-content"]').text
        if text1 == '提交成功！':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'AnnouncementManagementEdit.png')
        # 断言用例是否通过
        self.assertEqual(text1, '提交成功！')



    def test04delete(self):
        # 切换至上一级iframe窗口
        self.driver.switch_to.parent_frame()
        # 选择需删除项，点击删除并确认
        time.sleep(5)
        etwait(self.driver, 30, 'xpath', '//*[@id="addtable"]/tr[1]/td[1]/input').click()
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[3]').click()
        etwait(self.driver, 30, 'xpath', '//a[contains(text(),"确定")]').click()
        time.sleep(0.5)
        # 通过弹窗文本判断是否新增成功
        text1 = etwait(self.driver, 30, 'xpath', '/html/body/div[6]/div[1]').text
        if text1 == '删除成功':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'AnnouncementManagementDelete.png')
        # 判断用例是否通过
        self.assertEqual(text1, '删除成功')
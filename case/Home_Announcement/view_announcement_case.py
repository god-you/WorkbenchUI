import unittest
from selenium import webdriver
from case.login_in import login
from common.util import explicit_wait as etwait
from common import settings

settings.create_dir()
pict_path = settings.pictsave_path()

class ViewAnnouncement(unittest.TestCase):
    u"""首页公告"""

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        login(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test01query(self):
        u"""查看公告"""
        # 进入首页公告目录
        self.driver.find_element_by_xpath('//*[contains(text(),"首页公告")]').click()
        # 进入查看公告菜单
        ele1 = etwait(self.driver, 10, 'xpath', '//*[@id="首页公告"]/li[1]/a')
        ele1.click()
        # 切换iframe窗口
        frame1 = self.driver.find_element_by_css_selector('.iframeClass')
        self.driver.switch_to.frame(frame1)
        # 填写查询信息并点击查询
        ele2 = etwait(self.driver, 10, 'xpath', '//*[@id="starttime"]')
        ele2.clear()
        ele2.send_keys('2021-04-21 00:00:00')
        ele3 = self.driver.find_element_by_xpath('//*[@id="endtime"]')
        ele3.clear()
        ele3.send_keys('2021-04-21 23:59:59')
        self.driver.find_element_by_xpath('//*[@id="nitname"]').send_keys('热热热22')
        self.driver.find_element_by_xpath('//button[contains(text(),"查询")]').click()
        # 获取查询后的数据并判断是否与预期结果一致，不一致则截图保存
        etwait(self.driver, 30, 'xpath', '//*[@id="addtable"]/tr/td[1]')
        tbody = self.driver.find_element_by_id('addtable')
        datanum = len(tbody.find_elements_by_tag_name('tr'))
        if datanum == 1:
            pass
        else:
            self.driver.save_screenshot(pict_path + 'viewannquery.png')
        # 查看公告详情
        self.driver.find_element_by_xpath('//*[@id="addtable"]/tr/td[11]/button').click()
        # 切换下一层iframe窗口并关闭公告查看页面
        self.driver.switch_to.frame(0)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/button').click()
        # 断言判断用例是否通过
        self.assertEqual(datanum, 1)
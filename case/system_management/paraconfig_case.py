import unittest
from selenium import webdriver
import time
from common.util import explicit_wait as etwait, drop_down_menu
from common import settings

settings.create_dir()
pict_path = settings.pictsave_path()

class Paraconfig(unittest.TestCase):
    u"""参数配置"""

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        # login_In(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test01add(self):
        u"""新增参数"""
        # 进入系统管理目录
        ele2 = etwait(self.driver, 10, 'xpath', '//*[@id="menuul"]/li[26]/a')
        ele2.click()
        drop_down_menu()
        time.sleep(1)
        # 进入参数配置菜单
        self.driver.find_element_by_xpath('//*[@id="系统管理"]/li[4]/a').click()
        # 切换至iframe窗口
        frame = self.driver.find_element_by_css_selector('.iframeClass')
        self.driver.switch_to.frame(frame)
        # 刷新数据
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/ul/li[1]/button').click()
        # 点击‘新增’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[1]').click()
        # 填写新增部门信息并确认
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="vdnaddcom"]').click()
        time.sleep(2)
        add_ele2 = etwait(self.driver, 30, 'xpath', '//div[@id="departmentUi"]//span[contains(text(),"集团总部")]')
        add_ele2.click()
        time.sleep(1)
        alter_ele1 = etwait(self.driver, 30, 'xpath', '//*[@id="vname"]')
        alter_ele1.send_keys('新增VDN名称测试')
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        add_ele1 = etwait(self.driver, 30, 'xpath', '/html/body/div[17]/div[1]')
        add_text = add_ele1.text
        self.driver.find_element_by_xpath('/html/body/div[17]/div[2]/a').click()
        if add_text == '操作成功！':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'paraadd.png')
        self.assertEqual(add_text, '操作成功！')

    def test02edit(self):
        u"""修改参数信息"""
        # 选择需修改项
        self.driver.find_element_by_xpath('//*[@id="addtable"]/tr[1]/td[1]/input').click()
        # 点击‘修改’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[2]').click()
        # 修改并保存
        ele1 = etwait(self.driver, 10, 'xpath', '//*[@id="item_name_bj"]')
        ele1.send_keys('编辑后')
        time.sleep(1)
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        edi_ele1 = etwait(self.driver, 30, 'xpath', '/html/body/div[17]/div[1]')
        edi_text = edi_ele1.text
        self.driver.find_element_by_xpath('/html/body/div[17]/div[2]/a').click()
        if edi_text == '操作成功！':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'paraedit.png')
        self.assertEqual(edi_text, '操作成功！')

    def test03del(self):
        u"""删除参数"""
        # 选择需删除项
        self.driver.find_element_by_xpath('//*[@id="addtable"]/tr[1]/td[1]/input').click()
        # 点击‘删除’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[3]').click()
        time.sleep(1)
        # 确定删除
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        time.sleep(0.5)
        # 判断是否删除成功，失败则截屏保存。
        # 通过断言判断用例是否通过
        del_ele1 = etwait(self.driver, 30, 'xpath', '/html/body/div[17]/div[1]')
        del_text = del_ele1.text
        self.driver.find_element_by_xpath('/html/body/div[17]/div[2]/a').click()
        if del_text == '删除成功！':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'pardel.png')
        self.assertEqual(del_text, '删除成功！')

    def test04query(self):
        u"""查询"""
        time.sleep(1)
        # 填写查询条件
        self.driver.find_element_by_xpath('//*[@id="s_type"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="s_type"]/option[2]').click()
        # 点击‘查询’按钮
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/ul/li[1]/button').click()
        time.sleep(2)
        tbody = self.driver.find_element_by_xpath('//*[@id="addtable"]')
        datanum = len(tbody.find_elements_by_tag_name('tr'))
        if datanum >= 1:
            pass
        else:
            self.driver.save_screenshot(pict_path + 'extqur.png')
        self.assertNotEqual(datanum, 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)
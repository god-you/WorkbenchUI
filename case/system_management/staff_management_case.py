# -*- coding:UTF8 -*-
import unittest
from selenium import webdriver
import time
from common.util import explicit_wait as etwait,drop_down_menu
from common import settings
import os
from selenium.webdriver.chrome.options import Options
options = Options()
options.debugger_address = '127.0.0.1:8000'
settings.create_dir()
pict_path = settings.pictsave_path()


class Staffmana(unittest.TestCase):
    u"""员工管理"""

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        # login_In(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test01add(self):
        u"""新增员工"""
        # 进入系统管理目录
        ele2 = etwait(self.driver, 10, 'xpath', '//*[@id="menuul"]/li[26]/a')
        ele2.click()
        drop_down_menu()
        time.sleep(1)
        # 进入员工管理菜单
        self.driver.find_element_by_xpath('//*[@id="系统管理"]/li[14]/a').click()
        # 切换iframe窗口
        frame = self.driver.find_element_by_css_selector('.iframeClass')
        self.driver.switch_to.frame(frame)
        # 点击‘新增’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[1]').click()
        # 填写新增员工信息并确认
        ele1 = etwait(self.driver, 10, 'xpath', '//*[@id="rd_name"]')
        ele1.send_keys("新增员工姓名测试")
        self.driver.find_element_by_xpath('//*[@id="rd_number"]').send_keys(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())))
        self.driver.find_element_by_xpath('//*[@id="rd_agent"]').send_keys(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())))
        self.driver.find_element_by_xpath('//*[@id="addcompany"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="io010002"]/td[2]/span[3]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="ir010001"]/td[2]/span[3]').click()
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        add_ele1 = etwait(self.driver, 30, 'xpath', '/html/body/div[19]/div[1]')
        add_text = add_ele1.text
        # self.driver.find_element_by_xpath('/html/body/div[19]/div[2]/a').click()
        if add_text == '操作成功！':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'staffmanaadd.png')
        self.assertEqual(add_text, '操作成功！')

    def test02query(self):
        u"""查询"""
        # 填写查询条件
        self.driver.find_element_by_css_selector('input#checkcompany').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="io010002"]/td[1]/input').click()
        self.driver.find_element_by_css_selector('a.layui-layer-btn0').click()
        self.driver.find_element_by_css_selector('input#checkrole').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="ir010001"]/td[2]/span[3]').click()
        self.driver.find_element_by_css_selector('input#name').send_keys('新增员工姓名测试')
        # self.driver.find_element_by_css_selector('input#employeeNumber').send_keys(202108261911)
        # self.driver.find_element_by_css_selector('input#agent').send_keys(202108261911)
        # 点击‘查询’按钮
        self.driver.find_element_by_xpath('//button[contains(text(),"查询")]').click()
        time.sleep(2)
        tbody = self.driver.find_element_by_xpath('//*[@id="addtable"]')
        datanum = len(tbody.find_elements_by_tag_name('tr'))
        text1 = self.driver.find_element_by_xpath('//*[@id="addtable"]/tr/td[3]').text
        if datanum >= 1 and text1 == '新增员工姓名测试':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'staffmanaqur.png')
        self.assertEqual(datanum, 1)

    def test03edit(self):
        u"""修改员工信息"""
        # 选择需修改项
        self.driver.find_element_by_xpath('//*[@id="addtable"]/tr/td[1]/input').click()
        # 点击‘修改’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[2]').click()
        time.sleep(2)
        # 修改黑名单信息并保存
        self.driver.find_element_by_xpath('//*[@id="up_rd_name"]').send_keys('编辑后')
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        edi_ele1 = etwait(self.driver, 30, 'xpath', '/html/body/div[19]/div[1]')
        edi_text = edi_ele1.text
        self.driver.find_element_by_xpath('/html/body/div[19]/div[2]/a').click()
        if edi_text == '修改成功！':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'staffmanaedit.png')
        self.assertEqual(edi_text, '修改成功！')

    def test04resetpass(self):
        u"""密码重置"""
        # 选择需修改项
        self.driver.find_element_by_xpath('//*[@id="addtable"]/tr/td[1]/input').click()
        # 点击‘密码重置’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[4]').click()
        # 切换alert弹窗并确认
        alert = self.driver.switch_to.alert
        alert.accept()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        edi_ele1 = etwait(self.driver, 30, 'xpath', '/html/body/div[19]/div[1]')
        edi_text = edi_ele1.text
        self.driver.find_element_by_xpath('/html/body/div[19]/div[2]/a').click()
        if edi_text == '重置密码成功！':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'staffmanaresetpass.png')
        self.assertEqual(edi_text, '重置密码成功！')

    def test05conskcf(self):
        u"""会话技能配置"""
        # 选择需修改项
        self.driver.find_element_by_xpath('//*[@id="addtable"]/tr/td[1]/input').click()
        # 点击‘会话技能配置’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[5]').click()
        time.sleep(1)
        # 选择技能组并保存
        self.driver.find_element_by_xpath('//*[@id="cSkillTable"]/tbody/tr[2]/td[1]/input').click()
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        edi_ele1 = etwait(self.driver, 30, 'xpath', '/html/body/div[19]/div[1]')
        edi_text = edi_ele1.text
        self.driver.find_element_by_xpath('/html/body/div[19]/div[2]/a').click()
        if edi_text == '操作成功':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'staffmanaedit.png')
        self.assertEqual(edi_text, '操作成功')

    def test06dataexport(self):
        u"""数据导出"""
        frame = self.driver.find_element_by_css_selector('.iframeClass')
        self.driver.switch_to.frame(frame)
        path = "C:\\Users\\ASUS\\Downloads\\"
        num1 = len(os.listdir(path))
        # 点击‘数据导出’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[6]').click()
        while True:
            num2 = len([lists for lists in os.listdir(path)])
            if num2 == num1+1:
                break
            else:
                continue
        file = path + '员工信息.xls'
        while True:
            result = os.path.exists(path + '员工信息.xls')
            if result:
                f = open(file)
                f.close()
                os.remove(file)
                break
            else:
                continue
        self.assertTrue(result)

    def test07csgconfig(self):
        u"""话务技能组配置"""
        # 点击‘会话技能配置’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[7]').click()
        time.sleep(1)
        # 选择话务技能组并保存
        self.driver.find_element_by_xpath('//*[@id="huawuSkillTable"]/tbody/tr[2]/td[1]/input').click()
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        edi_ele1 = etwait(self.driver, 30, 'xpath', '/html/body/div[19]/div[1]')
        edi_text = edi_ele1.text
        self.driver.find_element_by_xpath('/html/body/div[19]/div[2]/a').click()
        if edi_text == '配置成功':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'staffmanaedit.png')
        self.assertEqual(edi_text, '配置成功')

    def test08del(self):
        u"""删除员工"""
        # 获取当前页面数据量
        ele1 = self.driver.find_element_by_css_selector('tbody#addtable')
        num1 = len(ele1.find_elements_by_tag_name('tr'))
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
            self.driver.save_screenshot(pict_path + 'staffmanadel.png')
        time.sleep(1)
        self.assertEqual(num1, num2 + 1)

    def test09temexport(self):
        u"""模板导出"""
        # 点击‘模板导出’按钮
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[8]').click()
        file = "C:\\Users\\ASUS\\Downloads\\员工导入模板.xlsx"
        while True:
            result = os.path.exists(file)
            if result:
                f = open(file)
                f.close()
                os.remove(file)
                break
            else:
                continue
        self.assertTrue(result)

    def test10batimport(self):
        u"""批量导入"""
        ele1 = self.driver.find_element_by_xpath('//*[@id="name"]')
        ele1.clear()
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/ul/li[1]/button').click()
        self.driver.find_element_by_xpath('//*[@id="caozuobt"]/button[9]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="upfile"]').send_keys('C:\\Users\\ASUS\\Desktop\\rongda_digital\\files\\员工导入模板.xlsx')
        time.sleep(1)
        self.driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        # 获取div弹窗文本，判断是否与预期结果一致，不一致则截屏保存。
        # 通过断言判断用例是否通过
        edi_ele1 = etwait(self.driver, 30, 'xpath', '/html/body/div[19]/div[1]')
        edi_text = edi_ele1.text
        self.driver.find_element_by_xpath('/html/body/div[19]/div[2]/a').click()
        if edi_text == '导入成功':
            pass
        else:
            self.driver.save_screenshot(pict_path + 'staffmanaimpot.png')
        self.assertEqual(edi_text, '导入成功')

if __name__ == "__main__":
    unittest.main(verbosity=2)
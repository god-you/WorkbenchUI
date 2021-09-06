# -*- coding:UTF8 -*-
import HTMLTestRunner
import unittest
import time
import os

if __name__ == "__main__":
    case_dirs = os.getcwd() + "\\case"
    sys_manage = unittest.defaultTestLoader.discover(case_dirs + "\\system_management", "*_case.py", top_level_dir=os.getcwd())
    home_announ = unittest.defaultTestLoader.discover(case_dirs + "\\home_announcement", "*_case.py", top_level_dir=os.getcwd())
    file_prefix = time.strftime("%Y_%m_%d %H_%M_%S", time.localtime(time.time()))
    fp = open(os.getcwd() + "\\test_report\\" + file_prefix + "result.html", 'wb')
    sys_manage_runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'东航测试报告', description=u'系统管理测试用例执行情况', verbosity=2)
    home_announ_runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'东航测试报告', description=u'首页公告测试用例执行情况', verbosity=2)
    sys_manage_runner.run(sys_manage)
    home_announ_runner.run(home_announ)
    fp.close()
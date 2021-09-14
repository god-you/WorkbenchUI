# -*- coding:UTF8 -*-
import os
import time
from common import HTMLTestRunner,util
import unittest

path = util.path()
case_dirs = path + "\\case"
file_prefix = time.strftime("%Y_%m_%d %H_%M_%S", time.localtime(time.time()))
fp = open(path + "\\test_report\\" + file_prefix + "result.html", 'wb')

def system_management():
    sys_manage = unittest.defaultTestLoader.discover(case_dirs + "\\system_management", "*_case.py",
                                                     top_level_dir=os.getcwd())
    sys_manage_runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'工作台测试报告', description=u'系统管理测试用例执行情况',
                                                      verbosity=2)
    sys_manage_runner.run(sys_manage)
    fp.close()

def home_announcement():
    home_announ = unittest.defaultTestLoader.discover(case_dirs + "\\home_announcement", "*_case.py",
                                                      top_level_dir=os.getcwd())
    home_announ_runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'工作台测试报告', description=u'首页公告测试用例执行情况',
                                                       verbosity=2)
    home_announ_runner.run(home_announ)
    fp.close()
print(os.getcwd())
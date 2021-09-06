# -*- coding:UTF8 -*-
import HTMLTestRunner
import unittest
import time
import os

if __name__ == "__main__":
    case_dirs = os.getcwd() + "\\case\\system_management"
    discover = unittest.defaultTestLoader.discover(case_dirs, "*_case.py")
    file_prefix = time.strftime("%Y_%m_%d %H_%M_%S", time.localtime(time.time()))
    fp = open(os.getcwd() + "\\test_report\\" + file_prefix + "result.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'东航测试报告', description=u'测试用例执行情况', verbosity=2)
    runner.run(discover)
    fp.close()
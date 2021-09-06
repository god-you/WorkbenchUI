import unittest
from selenium import webdriver
from case.login_in import login_In
import time
from util import explicit_wait as etwait
from selenium.webdriver.chrome.options import Options
import settings
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

settings.create_dir()
pict_path = settings.pictsave_path()
options = Options()
options.debugger_address = '127.0.0.1:8001'

class Workpool(unittest.TestCase):
    u"""工号池"""

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        # login_In(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
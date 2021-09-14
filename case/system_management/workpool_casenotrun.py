import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from common import settings

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
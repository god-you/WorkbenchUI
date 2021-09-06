import os
import time
from selenium.webdriver.common.action_chains import ActionChains

directory_name = time.strftime("%Y_%m_%d", time.localtime(time.time()))
path = "C:\\Users\\ASUS\\Desktop\\rongda_digital\\eastern_airlines\\error_screenshot\\" + directory_name

def create_dir():
    if not os.path.exists(path):
        os.mkdir(path)

def pictsave_path():
    picture_time = time.strftime("%Y_%m_%d %H_%M_%S", time.localtime(time.time()))
    err_scr_shot = path + "\\" + picture_time
    return err_scr_shot

def click_locxy(dr, x, y, click=True):
  '''
  dr:浏览器
  x:页面x坐标
  y:页面y坐标
  left_click:True为鼠标左键点击，否则为右键点击
  '''
  if click:
    ActionChains(dr).move_by_offset(x, y).click().perform()
  else:
    ActionChains(dr).move_by_offset(x, y).context_click().perform()
  ActionChains(dr).move_by_offset(-x, -y).perform()

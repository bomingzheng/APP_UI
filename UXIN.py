import datetime
import json
import time
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import yaml
from page_locat.path_config.path_config_class import *

with open(account_range, 'r') as f:
    ps= json.load(f)

# ld = open(account_range, 'r')
# ps = yaml.load(ld, Loader=yaml.FullLoader)

caps = {"platformName": "Android",
        "platformVersion": "6.0.1",
        "deviceName": "Android Emulator",
        "appPackage": "com.uxin.usedcar",
        "appActivity": "com.uxin.mainmodule.ui.activity.main.MainActivity",
        "autoGrantPermissions": "true",
        "automationName": "uiautomator2",
        "unicodeKeyboard": True,
        "resetKeyboard": True}
        # "noReset":True

wb = webdriver.Remote("http://localhost:4723/wd/hub", caps)

# dicts = {'0': 7, '1': 8, '2': 9, '3': 10, '4': 11, '5': 12, '6': 13, '7': 14, '8': 15, '9': 16,
#          'a': 29, 'b': 30, 'c': 31, 'd': 32, 'e': 33, 'f': 34, 'g': 35, 'h': 36, 'i': 37, 'j': 38,
#          'k': 39, 'l': 40, 'm': 41, 'n': 42, 'o': 43, 'p': 44, 'q': 45, 'r': 46, 's': 47, 't': 48,
#          'u': 49, 'v': 50, 'w': 51, 'x': 52, 'y': 53, 'z': 54}


def load(wb):
    print(datetime.datetime.now())
    if len(wb.find_elements_by_id("jn")) >= 1:
        wb.find_element_by_xpath("//*[@text='安庆']").click()
        return True
    else:
        return False
try:
    WebDriverWait(wb, 20).until(load)
except:
    print("No update")
WebDriverWait(wb, 20).until(EC.visibility_of_element_located((MobileBy.XPATH, "//*[@text='安庆市大观区服务门店']")))
wb.find_element_by_xpath("//*[@text='安庆市大观区服务门店']").click()
WebDriverWait(wb, 20).until(EC.presence_of_element_located((MobileBy.XPATH, "//*[contains(@text,'安庆')]")))
print(wb.find_element_by_xpath("//*[contains(@text,'安庆')]").text)
WebDriverWait(wb, 20).until(EC.visibility_of_element_located((MobileBy.ID, "bkn")))
wb.find_element_by_id("bkn").click()
WebDriverWait(wb, 20).until(EC.visibility_of_element_located((MobileBy.ID, "a0h")))
wb.find_element_by_id("a0h").click()

WebDriverWait(wb, 20).until(EC.visibility_of_element_located((MobileBy.ID, "ae3")))
wb.find_element_by_id("ae3").click()

WebDriverWait(wb, 20).until(EC.visibility_of_element_located((MobileBy.XPATH, "//*[@text='点击登录']")))
wb.find_element_by_xpath("//*[@text='点击登录']").click()
WebDriverWait(wb, 20).until(EC.visibility_of_element_located((MobileBy.ID, "ayk")))
wb.find_element_by_id("ayk").click()
WebDriverWait(wb, 20).until(EC.visibility_of_element_located((MobileBy.ID, "aku")))
wb.find_element_by_id("aku").click()
username = '17501033396'
for i in username:
    if ps.get(i):
        wb.press_keycode(ps[i])
    else:
        wb.press_keycode(ps[i.lower()], 64, 59) # 先把i切换成小写，然后再通过shift+capslock组合键切换成大写
    time.sleep(0.05)
wb.keyevent(66)  # 按回车键
wb.find_element_by_id("akw").click()
pwd = 'bmz1989'
for j in pwd:
    if ps.get(j):
        wb.press_keycode(ps[j])
    else:
        wb.press_keycode(ps[j.lower()], 64, 59)
    time.sleep(0.05)
time.sleep(2)
wb.keyevent(66)
time.sleep(1)
wb.find_element_by_id("akt").click()

WebDriverWait(wb, 20, 0.01).until(EC.presence_of_element_located((MobileBy.XPATH, "//*[@class='android.widget.Toast']")))
print(wb.find_element_by_xpath("//*[@class='android.widget.Toast']").text)


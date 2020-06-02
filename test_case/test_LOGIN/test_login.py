import json
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from page_locat.path_config.path_config_class import *
import yaml
import pytest
from page_locat.logging_file.logging_class import MyLog
with open(account_range, 'r') as f:
    ps= json.load(f)


@pytest.mark.usefixtures("start_app")
class TestLogIn:
    def test_login(self, start_app):
        WebDriverWait(start_app, 20).until(EC.visibility_of_element_located((MobileBy.ID, "ae3")))
        start_app.find_element_by_id("ae3").click()
        WebDriverWait(start_app, 20).until(EC.visibility_of_element_located((MobileBy.XPATH, "//*[@text='点击登录']")))
        start_app.find_element_by_xpath("//*[@text='点击登录']").click()
        WebDriverWait(start_app, 20).until(EC.visibility_of_element_located((MobileBy.ID, "ayk")))
        start_app.find_element_by_id("ayk").click()
        WebDriverWait(start_app, 20).until(EC.visibility_of_element_located((MobileBy.ID, "aku")))
        start_app.find_element_by_id("aku").click()
        username = '17501033396'
        for i in username:
            if ps.get(i):
                start_app.press_keycode(ps[i])
            else:
                start_app.press_keycode(ps[i.lower()], 64, 59)  # 先把i切换成小写，然后再通过shift+capslock组合键切换成大写
            time.sleep(0.05)
        start_app.keyevent(66)  # 按回车键
        start_app.find_element_by_id("akw").click()
        pwd = 'bmz1989'
        for j in pwd:
            if ps.get(j):
                start_app.press_keycode(ps[j])
            else:
                start_app.press_keycode(ps[j.lower()], 64, 59)
            time.sleep(0.05)
        time.sleep(2)
        start_app.keyevent(66)
        time.sleep(1)
        start_app.find_element_by_id("akt").click()

        WebDriverWait(start_app, 20, 0.01).until(
            EC.presence_of_element_located((MobileBy.XPATH, "//*[@class='android.widget.Toast']")))
        MyLog().info(start_app.find_element_by_xpath("//*[@class='android.widget.Toast']").text)
        assert '登录成功' == start_app.find_element_by_xpath("//*[@class='android.widget.Toast']").text


if __name__ == '__main__':
    pytest.main(['-s', 'test_login.py'])


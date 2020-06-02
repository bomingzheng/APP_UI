import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from page_locat.logging_file.logging_class import *
import yaml
import pytest
mylog = MyLog()


@pytest.fixture(scope='class')
def start_app():
    fp = open(app_start, 'r')
    caps = yaml.load(fp, Loader=yaml.FullLoader)
    wb = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    def load(wb):
        mylog.info(datetime.datetime.now())
        if len(wb.find_elements_by_id("jn")) >= 1:
            wb.find_element_by_xpath("//*[@text='安庆']").click()
            return True
        else:
            return False

    try:
        WebDriverWait(wb, 20).until(load)
    except:
        mylog.info("No update")

    WebDriverWait(wb, 20).until(EC.visibility_of_element_located((MobileBy.XPATH, "//*[@text='安庆市大观区服务门店']")))
    wb.find_element_by_xpath("//*[@text='安庆市大观区服务门店']").click()
    WebDriverWait(wb, 20).until(EC.presence_of_element_located((MobileBy.XPATH, "//*[contains(@text,'安庆')]")))
    mylog.info(wb.find_element_by_xpath("//*[contains(@text,'安庆')]").text)
    WebDriverWait(wb, 20).until(EC.visibility_of_element_located((MobileBy.ID, "bkn")))
    wb.find_element_by_id("bkn").click()
    WebDriverWait(wb, 20).until(EC.visibility_of_element_located((MobileBy.ID, "a0h")))
    wb.find_element_by_id("a0h").click()
    yield (wb) # 分割前置和后置条件（）里面是可以引用的变量
    wb.quit() # 后置条件


if __name__ == '__main__':
    def ee(start_app):
        print(start_app)
pytest.main(['-s', 'app_stast_class.py'])


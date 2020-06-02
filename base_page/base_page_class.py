from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from page_locat.path_config.path_config_class import *
from page_locat.logging_file.logging_class import MyLog
logging = MyLog()


# 封装基本处理，截图，异常处理，日志
class BasePage:

    def __init__(self, driver):
        self.wb = driver

    # app 滑屏封装
    def swipe_up(self):
        pass

    def swipe_down(self):
        pass

    def swipe_left(self, size, doc):
        try:
            self.wb.swipe(size["width"]*0.9, size["height"]*0.5, size["width"]*0.1, size["height"]*0.5, 200)
        except:
            logging.error("从右向左滑动失败")
            self.screenshot(doc)

    def swipe_right(self):
        pass

    def get_windows_size(self):
        # 获取屏幕大小
        return self.wb.get_window_size()

    # 获取toast文本
    def get_toast_text(self, sr):
        loc =  "//*[contains(@text,'{}')]".format(sr)
        try:
            WebDriverWait(self.wb, 20).until(EC.presence_of_element_located((MobileBy.XPATH, loc)))
            return self.wb.find_element_by_xpath(loc).text
        except:
            logging.error("未匹配到toast元素！")
            raise

    # 等待元素可见
    def wait_visible(self, locator, times=30, poll_frequency=0.5, doc=''):
        """
        :param locator: 元素定位元组（元素类型，元素值）
        :param times:   等待时间
        :param poll_frequency:  轮询时间
        :param doc:  日志保存和截图命名的模块名
        """
        logging.info("等待元素可见{}".format(locator))
        try:
            # 等待语句开始执行时间
            start = int(time.time())

            WebDriverWait(self.wb, times, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 等待语句执行结束时间
            end = int(time.time())
            # 实际等待时间
            actual_time = end - start
            logging.info("等待时长{}".format(actual_time))
        except:
            # 捕获异常到日志
            logging.error("等待元素可见失败！")
            # 截图
            self.screenshot(doc)
            # 抛异常
            raise

    # 等待元素存在
    def wait_exit(self, locator, times=30, poll_frequency=0.5, doc=''):
        logging.info("等待元素可见{}".format(locator))
        try:
            # 等待语句开始执行时间
            start = int(time.time())
            WebDriverWait(self.wb, times, poll_frequency).until(EC.presence_of_element_located(locator))
            # 等待语句执行结束时间
            end = int(time.time())
            # 实际等待时间
            actual_time = end - start
            logging.info("等待时长{}".format(actual_time))
        except:
            logging.error("等待元素存在失败！")
            self.screenshot(doc)
            raise

    # 查找元素
    def find_element(self, locator, doc=''):
        try:
            return self.wb.find_element(*locator)
        except:
            logging.error("查找元素失败！")

            # 截图
            self.screenshot(doc)
            raise

    # 点击元素
    def click_element(self, locator, doc):

        # 查找元素
        ele = self.find_element(locator, doc)
        try:
            # 点击操作
            ele.click()
        except:
            logging.error("点击元素失败！")

            # 截图
            self.screenshot(doc)
            raise

    # 输入操作
    def input_keys(self, locator, text, doc=''):
        ele = self.find_element(locator, doc)
        logging.info('{0}模块{1}元素输入操作'.format(doc, text))
        try:
            ele.send_keys(text)
        except:
            logging.error("元素输入内容失败！")

            # 截图
            self.screenshot(doc)
            raise

    # 获取元素的文本信息
    def get_element_text(self, locator, doc=''):

        ele = self.find_element(locator, doc)

        try:
            return ele.text

        except:
            logging.error("获取元素文本内容失败！")
            # 截图
            self.screenshot(doc)
            raise

    # 获取元素属性
    def get_ele_attribute(self, locator, attr, doc=''):
        ele = self.find_element(locator, doc)
        try:
            return ele.get_attribute(attr)

        except:
            logging.error("获取元素属性失败！")
            # 截图
            self.screenshot(doc)
            raise

    # 截图操作

    def screenshot(self, name):
        file_path = test_screen_path + "\\{0}_{1}.png".format(name, time.strftime("%Y_%m_%d %H:%M:%S"))
        self.wb.save_screenshot(file_path)
        logging.info("截图成功存放路径{}".format(file_path))

    # alert 处理
    def alert_acton(self, action="accept"):
        pass

    # iframe 处理
    def switch_frame(self, frame_name):

        pass

    # 上传操作
    def upload(self):
        pass


    # 窗口切换
    # 滚动条处理









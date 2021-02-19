

import unittest
import warnings

from prize_test import caps

from appium.webdriver.webdriver import WebDriver

from appium.webdriver.common.touch_action import TouchAction

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class TestSuite_API(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        warnings.filterwarnings ('ignore')
        desired_caps = caps.get_desired_capabilities()
        url = caps.get_url()
        self.driver = WebDriver(url, desired_caps)
        self.driver.implicitly_wait(20)
        self.driver.find_elements_by_id('com.tencent.mm:id/e3x')[0].click()   

    def test_case_link_elema_zhike(self):
        time.sleep(2)
        self.driver.find_element_by_id('com.tencent.mm:id/iy0').click()
        time.sleep(1)
        self.driver.find_element_by_id('com.tencent.mm:id/iy0').send_keys(
        'https://m.95303.com/mk/yxv/jtgj322/login/UKWH5TOBAJ16J?param1=UKWH5TOBAJ16J-1')
        time.sleep(1)
        self.driver.find_element_by_id ('com.tencent.mm:id/anv').click ( )  # 点击发送按钮
        time.sleep(1)
        TouchAction (self.driver).tap (x=588, y=900.7).release ( ).perform ( )  # 点击链接
        time.sleep(20)
       
        self.driver.get_screenshot_as_file(u'/Users/wangmingxiao/Desktop/王明月/text-python/安心保-万元出行意外险免费领取.png')
        print("页面正常")
        time.sleep(10)

    def tearDown(self) -> None:
        self.driver.quit()

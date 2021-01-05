# -*- coding: utf-8 -*-
'''
created on 2019-12-11
@author: daizhiwei
Project : 水滴保链接测试
'''

# 使用测试框架完成链接测试
# 导入appium的webdriver
from appium.webdriver.webdriver import WebDriver
# 导入selenium的webdriver
from selenium import webdriver
# 导入点击事件类库
from appium.webdriver.common.touch_action import TouchAction
# 导入时间等待类库
from selenium.webdriver.support.wait import WebDriverWait
# 导入time包
import time
# 导入unittest框架
import unittest
# 导入忽略警告的包
import warnings


# 定义测试类
class TestSuite_Partenlink(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        warnings.filterwarnings ('ignore')
        self.caps = {}
        self.caps["AutomationName"] = "Appium"
        self.caps["platformName"] = "Android"
        self.caps["platformVersion"] = "9"
        self.caps["deviceName"] = "huawei-alp_al00-DXT0217A23003150"
        self.caps["udid"] = "172.20.10.8:9966"
        self.caps["newCommandTimeout"] = "60"
        self.caps["appPackage"] = "com.tencent.mm"
        self.caps["appActivity"] = ".ui.LauncherUI"
        self.caps["noReset"] = "True"
        self.driver = WebDriver ('http://127.0.0.1:4723/wd/hub', self.caps)
        self.driver.implicitly_wait(10)
        # 将发送链接使用的群在微信中置顶，寻找elements的id，以索引方式找到第一个对话框进入，即进入群中
        self.driver.find_elements_by_id('com.tencent.mm:id/baj')[0].click()

    def test_case_shuidibao(self):
        self.driver.find_element_by_id ('com.tencent.mm:id/aqe').send_keys('https://www.sdbao.com/lab/u/f7ed22a7bc2079d8')
        self.driver.find_element_by_id('com.tencent.mm:id/aql').click()
        time.sleep(0.5)
        TouchAction(self.driver).tap(x=600, y=800).release().perform()
        time.sleep(0.5)
        a = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            '//android.widget.TextView[@text="赠险"]'))
        self.assertEqual(a.text, "赠险")


    def tearDown(self) -> None:
        self.driver.quit()
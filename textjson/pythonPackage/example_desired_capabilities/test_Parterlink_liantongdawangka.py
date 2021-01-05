# -*- coding: utf-8 -*-
'''
created on 2019-12-20
@author: daizhiwei
Project : 联通大王卡-40G专属全国流量免费-大可链接测试
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
from prize_last import caps
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
        desired_caps = caps.get_desired_capabilities()
        url = caps.get_url()
        self.driver = WebDriver(url, desired_caps)
        self.driver.implicitly_wait(10)
        # 将发送链接使用的群在微信中置顶，寻找elements的id，以索引方式找到第一个对话框进入，即进入群中
        self.driver.find_elements_by_id('com.tencent.mm:id/baj')[0].click()   # 打开置顶的群聊id+index

    def test_case_liantongdawangka(self):
        self.driver.find_element_by_id('com.tencent.mm:id/aqe').send_keys(
            'https://www.m-campaign.net/szking/?channel=212')
        self.driver.find_element_by_id('com.tencent.mm:id/aql').click()
        time.sleep(0.5)
        TouchAction(self.driver).tap(x=416, y=1669).release().perform()
        time.sleep(0.5)
        a = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath (
            '//android.widget.TextView[@text="大王卡"]'))
        self.assertEqual(a.text, "大王卡")

    def tearDown(self):
        self.driver.quit()
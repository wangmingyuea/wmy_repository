# -*- coding: utf-8 -*-
'''
created on 2020-06-22
author: daizhiwei
Project: 拼多多-每天领优惠-H5
interlinkage: https://mobile.yangkeduo.com/duo_collection.html?pid=9954834_144498384&auto_open=1&dis_t=1&cpsSign=CR_
200616_9954834_144498384_90067fd1695163569b1ce21d66f7276b&range_items=2%3A180%3A800&duoduo_type=2
'''

# 使用测试框架完成链接测试
# 导入appium的webdriver
from appium.webdriver.webdriver import WebDriver
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
from prize_test import caps


class TestSuite_API(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        warnings.filterwarnings ('ignore')
        desired_caps = caps.get_desired_capabilities()
        url = caps.get_url()
        self.driver = WebDriver(url, desired_caps)
        self.driver.implicitly_wait(17)
        # 将发送链接使用的群在微信中置顶，寻找elements的id，以索引方式找到第一个对话框进入，即进入群中
        self.driver.find_elements_by_id('com.tencent.mm:id/e3x')[0].click()   # 打开置顶的群聊id+index

    def test_case_link_pinduoduo(self):
        time.sleep(2)
        self.driver.find_element_by_id('com.tencent.mm:id/al_').send_keys(
            'https://mobile.yangkeduo.com/duo_collection.html?pid=9954834_144498384&auto_open=1&dis_t=1&cpsSign=CR_'
            '200616_9954834_144498384_90067fd1695163569b1ce21d66f7276b&range_items=2%3A180%3A800&duoduo_type=2')
        time.sleep(1)
        self.driver.find_element_by_id ('com.tencent.mm:id/anv').click ( )  # 点击发送按钮
        time.sleep(0.5)
        TouchAction (self.driver).tap (x=320, y=837).release ( ).perform ( )  # 点击链接
        time.sleep(3)

        # 页面返回 获取title内容

        a = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            '//android.widget.TextView[@text="拼多多"]'))
        self.assertEqual(a.text, "拼多多")  # 跳转奖品页面之后，对比title，看是否领取成功
        print("页面正常")

    def tearDown(self) -> None:
        self.driver.quit()
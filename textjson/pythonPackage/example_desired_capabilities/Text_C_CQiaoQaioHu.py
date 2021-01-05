# -*- coding: utf-8 -*-
'''
created on 2019-12-11
@author: daizhiwei
Project : 饿了么API域名链接
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

from selenium.webdriver.support import expected_conditions as EC
# 导入time包
import time
# 导入unittest框架
import unittest
# 导入忽略警告的包
import warnings

# 定义测试类
from prize_last import caps


class TestSuite_API(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        warnings.filterwarnings ('ignore')
        desired_caps = caps.get_desired_capabilities()
        url = caps.get_url()
        self.driver = WebDriver(url, desired_caps)
        self.driver.implicitly_wait(10)
        # 将发送链接使用的群在微信中置顶，寻找elements的id，以索引方式找到第一个对话框进入，即进入群中
        self.driver.find_elements_by_id('com.tencent.mm:id/baj')[0].click()   # 打开置顶的群聊id+index

    def test_case_link_qiaoqiaohu(self,number=1):
        # 点击微信输入框
        # 齐装网-免费领取4套装修设计方案，领优惠券链接
        self.driver.find_element_by_id ('com.tencent.mm:id/aqe').send_keys (
         'http://m.qizuang.com/sheji/?src=ajcm-1')

        self.driver.find_element_by_id ('com.tencent.mm:id/aql').click ( )  # 点击发送按钮
        time.sleep(0.5)
        TouchAction (self.driver).tap (x=650.4, y=1153.5).release ( ).perform ( )  # 点击链接
        time.sleep(1)
        # 页面返回 获取title内容
        a = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(
            '//android.widget.TextView[@text="户型设计_装修招标_免费装修设计与报价-齐装网"]'))
        self.assertEqual(a.text, "户型设计_装修招标_免费装修设计与报价-齐装网")  # 跳转奖品页面之后，对比title，看是否领取成功
        print("领取成功")


        def tearDown(self) -> None:
            self.driver.quit()
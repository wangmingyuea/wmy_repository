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
class TestSuite_API(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        warnings.filterwarnings ('ignore')
        self.caps = {}
        self.caps["AutomationName"] = "Appium"
        self.caps["platformName"] = "Android"     # 手机的设配（android或ios）
        self.caps["platformVersion"] = "8.1.0"    # 手机的设备的版本
        self.caps["deviceName"] = "OPPO R15 梦境版"   # 手机的名称
        # self.caps["udid"] = "85f8a8a0"             # 需要测试手机的ID（通过adb devices可获取）
        self.caps["udid"] = "172.20.10.8:9966"
        self.caps["newCommandTimeout"] = "60"
        self.caps["appPackage"] = "com.tencent.mm"    # 打开微信的软件
        self.caps["appActivity"] = ".ui.LauncherUI"
        self.caps["noReset"] = "True"
        self.driver = WebDriver ('http://127.0.0.1:4723/wd/hub', self.caps)
        self.driver.implicitly_wait(10)
        # 将发送链接使用的群在微信中置顶，寻找elements的id，以索引方式找到第一个对话框进入，即进入群中
        self.driver.find_elements_by_id('com.tencent.mm:id/baj')[0].click()   # 打开置顶的群聊id+index

    def test_case_link_jiuxianwang(self,number=1):
        # 点击微信输入框
        # 酒仙网，领优惠券链接
        self.driver.find_element_by_id ('com.tencent.mm:id/aqe').send_keys (
         'https://h5market.jiuxian.com/draw/getDetail/fb787ecc-b2a6-4c41-9ba2-d9e88f010652')
        time.sleep(0.5)
        self.driver.find_element_by_id ('com.tencent.mm:id/aql').click ( )  # 点击发送按钮
        time.sleep(0.5)
        TouchAction (self.driver).tap (x=650.4, y=1223.5).release ( ).perform ( )  # 点击链接
        # # 点击领取按钮
        # time.sleep(2)
        # TouchAction(self.driver).tap(x=549.5,y=2121).release().perform()

        # 页面返回 获取title内容
        time.sleep(1)
        a = WebDriverWait(self.driver, 8).until(lambda x: x.find_element_by_xpath(
            '//android.widget.TextView[@text="恭喜获得399元法国葡萄酒！立即领！"]'))
        self.assertEqual(a.text, "恭喜获得399元法国葡萄酒！立即领！")  # 跳转奖品页面之后，对比title，看是否领取成功
        print("领取成功")


        def tearDown(self) -> None:
            self.driver.quit()
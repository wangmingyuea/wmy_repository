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
        # self.caps["chromeOptions"]={'androidProcess': 'com.tencent.mm:tools'}
        self.driver = WebDriver ('http://127.0.0.1:4723/wd/hub', self.caps)
        self.driver.implicitly_wait(10)
        # 将发送链接使用的群在微信中置顶，寻找elements的id，以索引方式找到第一个对话框进入，即进入群中
        self.driver.find_elements_by_id('com.tencent.mm:id/baj')[0].click()   # 打开置顶的群聊id+index

    def test_case_link_aiqiyi(self,number=2):
        # 点击微信输入框
        # 爱奇艺票务-10元电影票代金券，领优惠券链接
        self.driver.find_element_by_id('com.tencent.mm:id/aqe').send_keys(
            '15513275072')
        self.driver.find_element_by_id('com.tencent.mm:id/aql').click()  # 点击发送按钮
        TouchAction(self.driver).long_press(x=627.4, y=1200.5,duration=2000).perform()
        time.sleep(1)
        TouchAction(self.driver).tap(x=677.4,y=183.8).release().perform() # 点击复制
        time.sleep(2)


        # 爱奇艺票务-10元电影票代金券，领优惠券链接
        self.driver.find_element_by_id ('com.tencent.mm:id/aqe').send_keys (
         'http://iqiyi.cn/lmayt')

        self.driver.find_element_by_id ('com.tencent.mm:id/aql').click ( )  # 点击发送按钮
        time.sleep(0.5)
        TouchAction (self.driver).tap (x=617.4, y=1223.5).release ( ).perform ( )  # 点击链接

        # 粘贴手机号
        time.sleep(2)
        TouchAction(self.driver).long_press(x=364.7, y=958.5, duration=1000).perform()
        # 点击粘贴
        time.sleep(2)
        # TouchAction(self.driver).long_press(x=241.8, y=966.5, duration=1000).perform()
        TouchAction(self.driver).tap(x=362.7, y=1172.5,).release().perform()
        time.sleep(2)
        # 点击"获取验证码"
        TouchAction(self.driver).tap(x=775.2, y=1125.5, ).release().perform()
        # 点击复制"验证码"
        time.sleep(8)
        TouchAction(self.driver).tap(x=519.5, y=395.7 ).release().perform()
        #长按复制验证码
        time.sleep(1)
        TouchAction(self.driver).long_press(x=237.8, y=1130.5, duration=1000).perform()
        # 点击粘贴
        time.sleep(2)
        TouchAction(self.driver).tap(x=242.8, y=1357.4).release().perform()
        # 点击领取
        TouchAction(self.driver).tap(x=552.5, y=1319.4).release().perform()
        for i in range(number):
            loc = ("xpath", "//*[@text='已经领取过了']")
            try:
                e = WebDriverWait(self.driver, 1, 0.01).until(EC.presence_of_element_located(loc))
                print(e)
            except:
                continue




        # # 页面返回 获取title内容
        # a = WebDriverWait(self.driver, 6).until(lambda x: x.find_element_by_xpath(
        #     '//android.widget.TextView[@text="10元电影票代金券"]'))
        # self.assertEqual(a.text, "10元电影票代金券")  # 跳转奖品页面之后，对比title，看是否领取成功
        #
        # print("领取成功")

        # TouchAction(self.driver).tap(x=406.6, y=974.8).release().perform()  # 点击链接
        # time.sleep(1)

        # 点击去使用
        time.sleep(2)
        TouchAction(self.driver).tap(x=498.5,y=1339).release().perform()

        for i in range(number):
            loc = ("xpath", "//*[@text='允许']")

            try:
                e = WebDriverWait(self.driver, 1, 0.01).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                continue



        def tearDown(self) -> None:
            self.driver.quit()
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
        self.caps["udid"] = "172.20.10.8:9966"           # 需要测试手机的ID（通过adb devices可获取）
        # self.caps["udid"] = "85f8a8a0"
        self.caps["newCommandTimeout"] = "60"
        self.caps["appPackage"] = "com.tencent.mm"    # 打开微信的软件
        self.caps["appActivity"] = ".ui.LauncherUI"
        # self.caps["appPackage"] = "com.oppo.launcher"    # 打开微信的软件
        # self.caps["appActivity"] = ".Launcher"
        self.caps["noReset"] = "True"
        self.driver = WebDriver ('http://127.0.0.1:4723/wd/hub', self.caps)
        self.driver.implicitly_wait(10)
        # 将发送链接使用的群在微信中置顶，寻找elements的id，以索引方式找到第一个对话框进入，即进入群中
        # self.driver.find_elements_by_id('com.tencent.mm:id/baj')[0].click()   # 打开置顶的群聊id+index

    def test_case_link_wudongjianghu(self,number=1):
        self.driver.start_activity('com.tencent.mm', '.ui.LauncherUI')
        # 将发送链接使用的群在微信中置顶，寻找elements的id，以索引方式找到第一个对话框进入，即进入群中
        self.driver.find_elements_by_id('com.tencent.mm:id/baj')[0].click()   # 打开置顶的群聊id+index
        # 点击微信输入框
        # 无尽战神
        self.driver.find_element_by_id ('com.tencent.mm:id/aqe').send_keys (
         'http://api.17redbull.cn/connector/theconnect/targetCon.shtml?type=3&id=2c9080e269e727c0016a002ac62c0001')

        self.driver.find_element_by_id ('com.tencent.mm:id/aql').click ( )  # 点击发送按钮
        time.sleep(0.5)
        TouchAction (self.driver).tap (x=284.7, y=1153.5).release ( ).perform ( )  # 点击链接
        # 点击领取按钮
        time.sleep(4)
        TouchAction(self.driver).tap(x=517.5,y=1617).release().perform()
        # 点击。。。
        time.sleep(4)
        self.driver.find_element_by_id('com.tencent.mm:id/lo').click()

        # 点击浏览器
        time.sleep(4)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="在浏览器打开"]').click()

        # 点击下载游戏
        time.sleep(8)
        TouchAction(self.driver).tap(x=500.5, y=1630).release().perform()
        # 点击下载
        time.sleep(6)
        TouchAction(self.driver).tap(x=501.5, y=2023).release().perform()
        # 等待游戏下载
        time.sleep(5)
        #点击打开
        TouchAction(self.driver).tap(x=948,y=509.7).release().perform()
        time.sleep(30)



        # 页面返回 获取title内容
        # time.sleep(3)
        # a = WebDriverWait(self.driver, 7).until(lambda x: x.find_element_by_xpath(
        #     '//android.widget.TextView[@text="下载管理"]'))
        # self.assertEqual(a.text, "下载管理")  # 跳转奖品页面之后，对比title，看是否领取成功
        # print("领取成功")


#     def star_APP(self):
#         time.sleep(5)
#         # 启动游戏
#         self.driver.start_activity('com.yinhu.sdk.fxj.pj', 'prj.chameleon.channelapi.SplashScreenActivity')
#         # 等待游戏加载
#         time.sleep(20)
#         # 等待登录弹窗
#         denglu = self.driver.find_element_by_xpath('//android.widget.TextView[@text="登录"]')
#         # 点击登录
#         TouchAction(self.driver).tap(x=1000, y=720).release().perform()
#         time.sleep(7)
#         cpackage = self.driver.current_package
#         if cpackage == 'com.yinhu.sdk.fxj.pj':
#             print('验证游戏是否能够正常登录：登录成功')
#         else:
#             print('进入游戏失败')
#
#     def tearDown(self) -> None:
#         self.driver.quit()
#
# if __name__ == '__main__':
#     APICheck_obj = TestSuite_API
#     APICheck_obj.test_case_link_wudongjianghu()
#     APICheck_obj.star_APP()
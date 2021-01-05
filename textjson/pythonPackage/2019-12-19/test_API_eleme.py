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
        self.caps["platformName"] = "Android"
        self.caps["platformVersion"] = "10.0.0"
        self.caps["deviceName"] = "HUAWEI Mate 10"
        self.caps["udid"] = "DXT0217A23003150"
        # 通过ip和端口号查找到手机
        # self.caps["udid"] = "192.168.1.37:5566"
        self.caps["newCommandTimeout"] = "60"
        self.caps["appPackage"] = "com.tencent.mm"
        self.caps["appActivity"] = ".ui.LauncherUI"
        self.caps["noReset"] = "True"
        self.driver = WebDriver ('http://127.0.0.1:4723/wd/hub', self.caps)
        # 休眠15s等待程序启动

    time.sleep(5)
    print("aaaaaaa")

    # 获取页面长宽
    def test_a_getSize(self):
       x = self.driver.get_window_size()['width']
       y = self.driver.get_window_size()['height']
       return (x, y)
       print("n")
    # 左向滑动，根据比例实现


    # def test_b_swipeLeft(self):
    #   l = self.test_a_getSize()
    #   x1 = int(l[0] * 0.75)
    #   y1 = int(l[1] * 0.5)
    #   x2 = int(l[0] * 0.25)
    #   self.driver.swipe(x1, y1, x2, y1)
    # # 再滑动一次
    #   self.driver.swipe(x1, y1, x2, y1)
    #   print("a")




#向右滑动
#     def test_swipeRight(self,t):
#       l=self.getSize()
#       x1=int(l[0]*0.25)
#       y1=int(l[1]*0.5)
#       x2=int(l[0]*0.75)
#       self.driver.swipe(x1,y1,x2,y1,t)
#
#
#
#向上滑动
    def test_swipeUp(self,t):
      l=self.getSize()
      x1=int(l[0]*0.5)
      y1=int(l[1]*0.75)
      y2=int(l[1]*0.25)

      self.driver.swipe(x1,y1,x1,y2,t)
      print("b")
#
#
# #向下滑动
#
#     def test_swipeDown(self,t):
#       l=self.getSize()
#       x1=int(l[0]*0.5)
#       y1=int(l[1]*0.25)
#       y2=int(l[1]*0.75)
#       self.driver.swipe(x1, y1, x1, y2, t)

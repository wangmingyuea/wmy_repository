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
import  os
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

    def test_case_link_Fwudongjianghu(self,number=1):
        self.driver.start_activity('com.tencent.mm', '.ui.LauncherUI')
        # 将发送链接使用的群在微信中置顶，寻找elements的id，以索引方式找到第一个对话框进入，即进入群中
        self.driver.find_elements_by_id('com.tencent.mm:id/baj')[0].click()   # 打开置顶的群聊id+index
        # 点击微信输入框
        # 无尽战神
        self.driver.find_element_by_id ('com.tencent.mm:id/aqe').send_keys (
         'http://api.redbull01.cn/connector/theconnect/targetCon.shtml?type=3&id=2c9080e269e727c0016a002ac62c0001')

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
        time.sleep(30)
        #点击打开
        TouchAction(self.driver).tap(x=948,y=509.7).release().perform()
        # 点击安装引用程序
        time.sleep(10)
        TouchAction(self.driver).tap(x=518.5, y=1918).release().perform()
        # 点击打开应用
        time.sleep(12)
        TouchAction(self.driver).tap(x=531.5, y=1964).release().perform()
        # 进入游戏出现的弹窗
        time.sleep(2)
        for i in range(number):
            loc = ("xpath", "//*[@text='允许']")
            try:
                e = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                continue
        time.sleep(5)
        TouchAction(self.driver).tap(x=754.2, y=1390.4).release().perform()

        time.sleep(45)

        # def uninstall_app(self):
        #     """
        #     卸载应用
        #     :return:
        #     """
        result_file = os.popen("adb uninstall com.wjzsql.union.ql")
        result = result_file.read()
        if "Success" in result:
            print("应用卸载成功")
        elif "Failure" in result:
            print("应用卸载失败")

if __name__ == '__main__':
    unittest.main()
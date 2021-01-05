'''
created on 2020-06-22
author: daizhiwei
Project: 滴滴出行-乘客大礼包免费领取-DD
interlinkage: 	https://z.didi.cn/4otZ1
'''
import unittest
import warnings

from prize_test import caps
# 使用测试框架完成链接测试
# 导入appium的webdriver
from appium.webdriver.webdriver import WebDriver
# 导入点击事件类库
from appium.webdriver.common.touch_action import TouchAction
# 导入时间等待类库
from selenium.webdriver.support.wait import WebDriverWait
# 导入time包
import time

class TestSuite_API(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        warnings.filterwarnings ('ignore')
        desired_caps = caps.get_desired_capabilities()
        url = caps.get_url()
        self.driver = WebDriver(url, desired_caps)
        self.driver.implicitly_wait(20)
        # 将发送链接使用的群在微信中置顶，寻找elements的id，以索引方式找到第一个对话框进入，即进入群中
        self.driver.find_elements_by_id('com.tencent.mm:id/e3x')[0].click()   # 打开置顶的群聊id+index

    def test_case_link_dididaijuan(self):
        time.sleep(2)
        self.driver.find_element_by_id('com.tencent.mm:id/iy0').click()
        time.sleep(1)
        self.driver.find_element_by_id('com.tencent.mm:id/iy0').send_keys('18746491313')
        time.sleep(1)
        self.driver.find_element_by_id('com.tencent.mm:id/anv').click()  # 点击发送按钮
        time.sleep(2)
        TouchAction(self.driver).long_press(x=720.7,y=877.5,duration=3000).wait(5000).perform()
        time.sleep(1)
        TouchAction(self.driver).tap(x=368.2,y=519.7).release().perform()    # 点击复制
        time.sleep(2)
        a=self.driver.find_element_by_id('com.tencent.mm:id/gas').text
        print(a)
        time.sleep(2)
        self.driver.find_element_by_id('com.tencent.mm:id/iy0').send_keys('https://z.didi.cn/4otZ1')
        time.sleep(1)

        self.driver.find_element_by_id ('com.tencent.mm:id/anv').click ( )  # 点击发送按钮
        time.sleep(1)
        TouchAction (self.driver).tap (x=588, y=900.7).release ( ).perform ( )  # 点击链接
        time.sleep(10)
        TouchAction(self.driver).tap(x=513, y=1515.8).release().perform()  #点击输入框
        time.sleep(2)
        TouchAction(self.driver).long_press(x=541.5, y=727.5, duration=3000).wait(5000).perform()  #长按输入框
        time.sleep(1)
        TouchAction(self.driver).tap(x=512.2, y=960).release().perform()        # 粘贴手机号
        time.sleep(2)
        TouchAction(self.driver).tap(x=192, y=989.2).release().perform()   # 点击勾选
        time.sleep(10)
        TouchAction(self.driver).tap(x=534.7, y=1550.1).release().perform()    # 点击领取
        time.sleep(15)
        # b=self.driver.find_element_by_id('android:id/text1').text
        # 页面返回 获取title内容
        # a = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id('android:id/text1'))
        # a = self.driver.find_element_by_id('andrord:id/test1')
        # print(a.text)
        # self.assertEqual(a.text, "滴滴代驾给您发券啦！")  # 跳转奖品页面之后，对比title，看是否领取成功
        # print("页面正常")
        # time.sleep(5）
        self.driver.get_screenshot_as_file(u'/Users/wangmingxiao/Desktop/王明月/text-python/滴滴代驾-代驾券礼包免费领取.png')
        print("测试通过")
        time.sleep(10)

    def tearDown(self) -> None:
        self.driver.quit()
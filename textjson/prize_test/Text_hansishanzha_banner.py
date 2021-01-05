'''
created on 2020-06-22
author: daizhiwei
Project: 汉斯山楂广告位banner（9月6日到期）
interlinkage: https://pro.m.jd.com/mall/active/2PdBahnMxWusxZFGrvCSKnzPwjAy/index.html
'''
import unittest
import warnings

from appium.webdriver import webdriver

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

    def test_case_link_hansishanzha(self):
        time.sleep(2)
        self.driver.find_element_by_id('com.tencent.mm:id/iy0').click()
        time.sleep(1)
        self.driver.find_element_by_id('com.tencent.mm:id/iy0').send_keys(
        'http://coupon.m.jd.com/coupons/show.action?'
        'key=e6111bd638334965b32d60e799fa983d&roleId=42027371&to=mall.jd.com/index-10204497.html')
        time.sleep(1)
        self.driver.find_element_by_id ('com.tencent.mm:id/anv').click ( )  # 点击发送按钮
        time.sleep(1)
        TouchAction (self.driver).tap (x=590.5, y=810.7).release ( ).perform ( )  # 点击链接
        time.sleep(10)
        # 获取屏幕的size
        print(self.driver.get_window_size())
        # 获取屏幕的高
        x = self.driver.get_window_size()['width']
        # 获取屏幕宽
        y =self.driver.get_window_size()['height']
        print(x+y)

        self.driver.swipe(806.2, 1405.5, 471, 603.7, 4000)
        time.sleep(8)
        TouchAction(self.driver).tap(x=423,y=1250.1).release().perform()
        time.sleep(15)
        # 页面返回 获取title内容
        #
        # a = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
        #     '//android.widget.TextView[@text="轻生活零负担"]'))
        # self.assertEqual(a.text, "轻生活零负担")  # 跳转奖品页面之后，对比title，看是否领取成功
        self.driver.get_screenshot_as_file(u'/Users/wangmingxiao/Desktop/王明月/text-python/汉斯山楂广告位banner.png')
        print("页面正常")
        time.sleep(10)

    def tearDown(self) -> None:
        self.driver.quit()

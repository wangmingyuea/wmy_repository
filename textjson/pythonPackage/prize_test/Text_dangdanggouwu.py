'''
created on 2020-06-22
author: daizhiwei
Project: 当当购物-百元优惠券免费领取
interlinkage: https://mp.weixin.qq.com/s/NZ5138zhgR089KPq3vQmGg
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

    def test_case_link_tongchengyilong(self):
        time.sleep(2)
        self.driver.find_element_by_id('com.tencent.mm:id/al_').click()
        time.sleep(1)
        self.driver.find_element_by_id('com.tencent.mm:id/al_').send_keys(
         'https://mp.weixin.qq.com/s/NZ5138zhgR089KPq3vQmGg')
        time.sleep(1)
        self.driver.find_element_by_id ('com.tencent.mm:id/anv').click ( )  # 点击发送按钮

        time.sleep(2)
        TouchAction(self.driver).tap(x=413, y=883).release().perform()  # 点击链接
        time.sleep(7)
        TouchAction(self.driver).tap(x=477, y=1104).release().perform()
        time.sleep(15)
        # a = WebDriverWait (self.driver, 10).until (lambda x: x.find_element_by_id('com.tencent.mm:id/dl'))
        # time.sleep(5)
        # print(a.text)
        # self.assertEqual(a.text, "领优惠券")  # 跳转奖品页面之后，对比title，看是否领取成功
        # time.sleep(5)
        self.driver.get_screenshot_as_file(u'/Users/wangmingxiao/Desktop/王明月/text-python/当当购物-百元优惠券免费领取.png')
        print("测试通过")
        time.sleep(10)
    def tearDown(self) -> None:
        self.driver.quit()
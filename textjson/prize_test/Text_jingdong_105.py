'''
created on 2020-06-22
author: daizhiwei
Project: 京东-105元减5元券--免费，领优惠券（12.31到期）
interlinkage: http://api.qcoder.com.cn/webService/shopGather/jingdongAllPrize/index.html
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

    def test_case_link_Text_API_jingdong_105(self):
        time.sleep(2)
        self.driver.find_element_by_id('com.tencent.mm:id/iy0').click()
        time.sleep(1)
        self.driver.find_element_by_id('com.tencent.mm:id/iy0').send_keys(
        'http://api.qcoder.com.cn/webService/shopGather/jingdongAllPrize/index.html')
        time.sleep(1)
        self.driver.find_element_by_id ('com.tencent.mm:id/anv').click ( )  # 点击发送按钮
        time.sleep(2)
        TouchAction (self.driver).tap (x=590.5, y=810.7).release ( ).perform ( )  # 点击链接
        time.sleep(8)
        # self.driver.swipe(552.7,1221,525,707.2,4000)
        # time.sleep(3)
        TouchAction(self.driver).tap(x=540.7,y=1768.5).release().perform()#点击立即领取
        print("是否走到领取页面")
        time.sleep(10)
        TouchAction(self.driver).tap(x=529.5,y=1250.1).release().perform()#点击领取优惠卷
        print("点击领取优惠卷")
        time.sleep(18)
        # 页面返回 获取title内容

        # a = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
        #     '//android.widget.TextView[@text="京东满105减5"]'))
        # self.assertEqual(a.text, "京东满105减5")  # 跳转奖品页面之后，对比title，看是否领取成功
        # print("页面正常")
        self.driver.get_screenshot_as_file(u'/Users/wangmingxiao/Desktop/王明月/text-python/京东-105元减5元券--免费，领优惠券.png')
        time.sleep(10)

    def tearDown(self) -> None:
        self.driver.quit()
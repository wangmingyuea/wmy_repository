'''
created on 2020-06-22
author: daizhiwei
Project: 优爱购-七彩云南专区限时抢券）
interlinkage: https://mp.weixin.qq.com/s/h0wNWEKH8oQIIq9V9GcYrw
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
        self.driver.implicitly_wait(25)
        # 将发送链接使用的群在微信中置顶，寻找elements的id，以索引方式找到第一个对话框进入，即进入群中
        self.driver.find_elements_by_id('com.tencent.mm:id/e3x')[0].click()   # 打开置顶的群聊id+index

    def test_case_link_youaigou_qicaiyunnan(self):
        time.sleep(2)
        self.driver.find_element_by_id('com.tencent.mm:id/al_').send_keys(
        'https://mp.weixin.qq.com/s/h0wNWEKH8oQIIq9V9GcYrw')
        time.sleep(1)
        self.driver.find_element_by_id ('com.tencent.mm:id/anv').click ( )  # 点击发送按钮
        time.sleep(0.5)
        TouchAction (self.driver).tap (x=590.5, y=810.7).release ( ).perform ( )  # 点击链接
        time.sleep(5)
        TouchAction(self.driver).tap (x=519,y=1092).release().perform()


        # 页面返回 获取title内容
        time.sleep(6)
        a = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            '//android.widget.TextView[@text="万券齐发 现金补贴"]'))
        self.assertEqual(a.text, "万券齐发 现金补贴")  # 跳转奖品页面之后，对比title，看是否领取成功
        print("页面正常")
        time.sleep(2)

    def tearDown(self) -> None:
        self.driver.quit()
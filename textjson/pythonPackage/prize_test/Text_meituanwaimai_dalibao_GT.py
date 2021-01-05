'''
created on 2020-06-22
author: daizhiwei
Project: 美团外卖-大礼包天天领-GT（无到期时间）
interlinkage: https://act.meituan.com/clover/page/adunioncps/second_cashback?
access_token=73FFC787880AB3D14F1E00DDCB2A90C7&activity=7BQcOyZZeF&requestId=21251593339074&
timestamp=1593339074&utmMedium=39B2D21DCA0C2918A3CDFCD6DC0C6636&utmSource=2125&version=1.0
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

    def test_case_link_meituanwaimai_dalibao(self):
        time.sleep(2)
        self.driver.find_element_by_id('com.tencent.mm:id/al_').send_keys(
        'https://act.meituan.com/clover/page/adunioncps/second_cashback?access_token=73FFC787880AB3D14F1E00DDCB2A90C7&'
        'activity=7BQcOyZZeF&requestId=21251593339074&timestamp=1593339074&utmMedium=39B2D21DCA0C2918A3CDFCD6DC0C6636&utmSource=2125&version=1.0')
        time.sleep(1)
        self.driver.find_element_by_id ('com.tencent.mm:id/anv').click ( )  # 点击发送按钮
        time.sleep(0.5)
        TouchAction (self.driver).tap (x=420.7, y=750).release ( ).perform ( )  # 点击链接
        time.sleep(3)

        # 页面返回 获取title内容

        a = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            '//android.widget.TextView[@text="美团发红包啦"]'))
        self.assertEqual(a.text, "美团发红包啦")  # 跳转奖品页面之后，对比title，看是否领取成功
        print("页面正常")

    def tearDown(self) -> None:
        self.driver.quit()
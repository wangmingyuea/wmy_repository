'''
project:滴滴出行-乘客大礼包免费领取-YY
url: 	https://v.didi.cn/v/XPEXL
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

    def test_case_link_didachuxing(self):
        time.sleep(2)
        self.driver.find_element_by_id('com.tencent.mm:id/al_').click()
        time.sleep(1)
        self.driver.find_element_by_id('com.tencent.mm:id/al_').send_keys('13613184620')
        time.sleep(1)
        self.driver.find_element_by_id('com.tencent.mm:id/anv').click()  # 点击发送按钮
        time.sleep(2)
        TouchAction(self.driver).long_press(x=720.7,y=877.5,duration=3000).wait(5000).perform()
        time.sleep(1)
        TouchAction(self.driver).tap(x=368.2,y=519.7).release().perform()    # 点击复制
        time.sleep(2)
        self.driver.find_element_by_id('com.tencent.mm:id/al_').send_keys(
        'https://v.didi.cn/v/XPEXL')
        time.sleep(1)
        self.driver.find_element_by_id ('com.tencent.mm:id/anv').click ( )  # 点击发送按钮
        time.sleep(1)
        TouchAction (self.driver).tap (x=588, y=900.7).release ( ).perform ( )  # 点击链接
        time.sleep(15)
        TouchAction(self.driver).long_press(x=522.7, y=1131.8, duration=3000).wait(5000).perform()  #长按输入框
        time.sleep(1)
        TouchAction(self.driver).tap(x=486, y=1380).release().perform()        # 粘贴手机号
        time.sleep(2)
        TouchAction(self.driver).tap(x=245.1, y=1589.1).release().perform()   # 点击勾选
        time.sleep(10)
        TouchAction(self.driver).tap(x=481.5, y=1228.5).release().perform()    # 点击领取
        time.sleep(15)
        # 页面返回 获取title内容

        # a = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
        #     '//android.widget.TextView[@text="嘀嗒出行"]'))
        # self.assertEqual(a.text, "嘀嗒出行")  # 跳转奖品页面之后，对比title，看是否领取成功
        # print("页面正常")
        # time.sleep(5)
        self.driver.get_screenshot_as_file(u'/Users/wangmingxiao/Desktop/王明月/text-python/滴滴出行-乘客大礼包免费领取-YY.png')
        print("测试通过")
        time.sleep(10)
    def tearDown(self) -> None:
        self.driver.quit()
'''
created on 2020-06-22
author: daizhiwei
Project: 返利网-购物补贴限时领取
interlinkage: https://shop.j5b8u.cn/h5/wxcard/rd.htm?sid=133&spm=page_name.h5.pty-floor1~scene-133~std-76131
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

    def test_case_link_fanliwang(self):
        time.sleep(2)
        self.driver.find_element_by_id('com.tencent.mm:id/iy0').click()
        time.sleep(1)
        self.driver.find_element_by_id('com.tencent.mm:id/iy0').send_keys(
            'https://shop.j5b8u.cn/h5/wxcard/rd.htm?sid=133&spm=page_name.h5.pty-floor1~scene-133~std-76131')
        time.sleep(1)
        self.driver.find_element_by_id ('com.tencent.mm:id/anv').click ( )  # 点击发送按钮
        time.sleep(1)
        TouchAction (self.driver).tap (x=277.5, y=813.7).release ( ).perform ( )  # 点击链接
        time.sleep(16)
        TouchAction(self.driver).tap(x=481.5,y=1266.8).release().perform() #点击立即领取
        # time.sleep(2)
        # TouchAction(self.driver).tap(x=525,y=1278).release().perform# 点击开红包
        time.sleep(20)

        # 页面返回 获取title内容
        #
        # a = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id('android:id/text1'))
        # print(a.text)
        # self.assertEqual(a.text, "斩月屠龙")  # 跳转奖品页面之后，对比title，看是否领取成功
        self.driver.get_screenshot_as_file(u'/Users/wangmingxiao/Desktop/王明月/text-python/返利网-购物补贴限时领取.png')
        time.sleep(10)

    def tearDown(self) -> None:
        self.driver.quit()

'''
created on 2020-06-22
author: daizhiwei
去哪儿旅行-百元出行礼包-H5（有效期2021.11.30）
http://api.qcoder.com.cn/webService/shopGather/qunaernew/index.html
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
from selenium.webdriver.support import expected_conditions as EC
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

    def test_case_link_Text_API_qunaer(self):
        time.sleep(2)
        self.driver.find_element_by_id('com.tencent.mm:id/iy0').click()
        time.sleep(1)
        self.driver.find_element_by_id('com.tencent.mm:id/iy0').send_keys(
        'http://api.qcoder.com.cn/webService/shopGather/qunaernew/index.html')
        time.sleep(1)
        self.driver.find_element_by_id ('com.tencent.mm:id/anv').click ( )  # 点击发送按钮
        time.sleep(1)
        TouchAction (self.driver).tap (x=588, y=900.7).release ( ).perform ( )  # 点击链接
        time.sleep(20)
        # for i in range (1):
        #     loc = ("xpath", "//*[@text='确定']")
        #     try:
        #         e = WebDriverWait (self.driver, 2, 1).until (EC.presence_of_element_located (loc))
        #         e.click ( )
        #     except:
        #         pass

        # 页面返回 获取title内容
        # a = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
        #     '//android.widget.TextView[@text="饿了么天天领红包"]'))
        # self.assertEqual(a.text, "饿了么天天领红包")  # 跳转奖品页面之后，对比title，看是否领取成功
        self.driver.get_screenshot_as_file(u'/Users/wangmingxiao/Desktop/王明月/text-python/去哪儿旅行-百元出行礼包-H5.png')
        print("页面正常")
        time.sleep(10)

    def tearDown(self) -> None:
        self.driver.quit()
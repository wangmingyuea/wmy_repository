from appium.webdriver.common.touch_action import TouchAction

import time

from appium.webdriver.webdriver import WebDriver

# 引入智能等待
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

# 定义API奖品监控类
class API_Check:
    # 定义初始化方法，存放字典，华为mate20手机参数
    def __init__(self):
        self.caps = {}
        self.caps["AutomationName"] = "Appium"
        self.caps["platformName"] = "Android"     # 手机的设配（android或ios）
        self.caps["platformVersion"] = "8.1.0"    # 手机的设备的版本
        self.caps["deviceName"] = "OPPO R15 梦境版"   # 手机的名称
        # self.caps["udid"] = "85f8a8a0"             # 需要测试手机的ID（通过adb devices可获取）
        self.caps["udid"] = "172.20.10.8:9966"
        self.caps["newCommandTimeout"] = "60"
        self.caps["appPackage"] = "com.oppo.launcher"    # 打开微信的软件
        self.caps["appActivity"] = ".Launcher"
        self.caps["noReset"] = "True"
        self.driver = WebDriver('http://127.0.0.1:4723/wd/hub', self.caps)
        self.driver.implicitly_wait(10)

    # 定义通用查找进入业务测试群方法
    def find_enter_share(self):
        self.driver.start_activity('com.tencent.mm', '.ui.LauncherUI')
        time.sleep(1)
        self.driver.find_elements_by_id('com.tencent.mm:id/baj')[0].click()   # 打开置顶的群聊id+index

    # 定义通用点击链接方法
    def click_link_API(self):
        TouchAction(self.driver).tap(x=500, y=600).release().perform()
        time.sleep(5)

    # 定义发送无尽战神-redbullosa域名链接方法
    def send_link_wujinzhanshen_API(self):
        print('现在进行无尽战神-redbullosa域名下链接测试-------------------------------------------------action')
        self.driver.find_element_by_id('com.tencent.mm:id/aqe').send_keys(
            'http://api.redbullosa.cn/connector/theconnect/targetCon.shtml?type=3&id=2c9080e269e727c0016a002ac62c0001')
        self.driver.find_element_by_id('com.tencent.mm:id/aql').click()
        time.sleep(3)

    # 定义对比无尽战神-redbullosa域名下API页面方法
    def contrast_link_wujinzhanshen_RedbullOsa(self):
        time.sleep(7)
        a = self.driver.find_element_by_id('android:id/text1')
        if a.text == '无尽战神':
            print('redbullosa域名下无尽战神API页面链接正常')
            time.sleep(2)
            self.driver.find_element_by_id('mobile').send_keys('15210059795')
            time.sleep(2)
            self.driver.find_element_by_id('btnSubmit').click()
            time.sleep(3)
            b = self.driver.find_element_by_id('android:id/text1')
            if b.text == '无尽战神':
                print('输入手机号后领取后页面正常')
                time.sleep(3)
                # 进入浏览器中下载
                self.driver.find_element_by_id('com.tencent.mm:id/lo').click()
                time.sleep(3)
                TouchAction(self.driver).tap (x=650, y=1100).release ( ).perform ( )
                time.sleep(3)
                self.driver.find_element_by_xpath('//android.widget.Button[@text="仅一次"]').click()
                time.sleep(10)
                # 第一次点击下载
                self.driver.find_element_by_xpath ('//android.widget.TextView[@text="直接下载"]').click ( )
                time.sleep (6)
                # 第二次点击下载
                self.driver.find_element_by_xpath ('//android.widget.TextView[@text="直接下载"]').click ( )
                # 使用智能等待
                find = WebDriverWait(self.driver, 20).until(lambda x : x.find_element_by_xpath(
                    '//android.widget.Button[@text="继续安装"]'))
                if find:
                    print ('下载成功，即将进行安装')
                    TouchAction (self.driver).tap (x=950, y=830).release ( ).perform ( )
                    time.sleep (15)
                    TouchAction (self.driver).tap (x=500, y=1680).release ( ).perform ( )
                    time.sleep (15)
                    print ('文件安装成功，等待清理安装包')
                    # 清空安装包，为下次测试做准备
                    TouchAction (self.driver).tap (x=700, y=850).release ( ).perform ( )
                    time.sleep(15)
                    print ('安装包清理成功，即将进行app测试')
            else:
                print('输入手机号后页面有问题')
        else:
            print('链接异常，请查看')

    def star_APP(self):
        # 启动游戏
        self.driver.start_activity('com.yinhu.sdk.fxj.pj','prj.chameleon.channelapi.SplashScreenActivity')
        # 等待游戏加载
        time.sleep(20)
        # 等待登录弹窗
        denglu = self.driver.find_element_by_xpath('//android.widget.TextView[@text="登录"]')
        # 点击登录
        TouchAction(self.driver).tap(x=1000,y=720).release().perform()
        time.sleep(7)
        cpackage = self.driver.current_package
        if cpackage == 'com.yinhu.sdk.fxj.pj':
            print('验证游戏是否能够正常登录：登录成功')
        else:
            print('进入游戏失败')


if __name__ == '__main__':
    APICheck_obj = API_Check()
    APICheck_obj.find_enter_share()
    APICheck_obj.send_link_wujinzhanshen_API()
    APICheck_obj.click_link_API()
    APICheck_obj.contrast_link_wujinzhanshen_RedbullOsa()
    # APICheck_obj.star_APP()
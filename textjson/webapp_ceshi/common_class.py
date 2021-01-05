# 公共类：设置整个项目的驱动参数并返回驱动引擎
from appium.webdriver.webdriver import WebDriver


class comm_class():
    # 设置驱动参数
    def _init_(self):
        self.caps={}
        self.caps['automationName'] = 'UiAutomator2'
        self.caps['platformName'] = 'Android'
        self.caps['platformVersion'] = '6.0'
        self.caps['deviceName'] = '192.168.141.101:5555'
        self.caps['appPackage'] = 'com.youdao.note'
        self.caps['appActivity'] = '.activity2.MainActivity t362'
#get_driver方法
def get_driver(self):
    self.driver = WebDriver('http://127.0.0.1:4723/wd/hub', self.caps)
    self.driver.implicitly_wait(10)
    return self.driver

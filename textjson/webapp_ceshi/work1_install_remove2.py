#V2.0 实现两个模拟器设备安装卸载的兼容性测试
#导入appium类库
from appium.webdriver.webdriver import WebDriver
import time
#继承导入V1.0类
from youdaoproject.work1_install_remove import yd_install_removeV1

class yd_install_removeV2(yd_install_removeV1):
    def __init__(self):
        self.caps = {}
        self.caps['automationName'] = 'UiAutomator2'
        self.caps['platformName'] = 'Android'

    def setdevice_6(self):
        self.caps['platformVersion'] = '6.0'
        self.caps['deviceName'] = '192.168.141.101:5555'
        self.caps['appPackage'] = 'com.android.launcher3'
        self.caps['appActivity'] = '.Launcher t238'
        self.driver = WebDriver('http://127.0.0.1:4723/wd/hub', self.caps)

    def setdevice_7(self):
        self.caps['platformVersion'] = '7.1'
        self.caps['deviceName'] = '192.168.141.102:5555'
        self.caps['appPackage'] = 'com.android.launcher3'
        self.caps['appActivity'] = '.Launcher t2'
        self.driver = WebDriver('http://127.0.0.1:4723/wd/hub', self.caps)

if __name__ == '__main__':
    yd_install_removeV2_obj=yd_install_removeV2()
    #6.0版本的测试
    yd_install_removeV2_obj.setdevice_6()
    yd_install_removeV2_obj.test_install_remove()
    yd_install_removeV2_obj.check_install()
    #7.0版本的测试
    yd_install_removeV2_obj.setdevice_7()
    yd_install_removeV2_obj.test_install_remove()
    yd_install_removeV2_obj.check_install()


# #添加笔记的测试
#
# # 导入appium类库
# from appium.webdriver.webdriver import WebDriver
# import time
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
#
# caps={}
# caps['automationName']='UiAutomator2'
# caps['platformName']='Android'
# caps['platformVersion']='6.0'
# caps['deviceName']='192.168.141.101:5555'
# caps['appPackage']='com.youdao.note'
# caps['appActivity']='.activity2.MainActivity t362'
#
# driver=WebDriver('http://127.0.0.1:4723/wd/hub',caps)
# driver.implicitly_wait(10)
# el=WebDriverWait(driver,10).until(lambda x:x.find_element_by_id('com.android.packageinstaller:id/permission_allow_button'))
# if el:
#     #点击允许按钮
#     driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
#     #点击新增按钮
#     time.sleep(2)
#     driver.find_element_by_id('com.youdao.note:id/add_note').click()
#     #点击新建笔记
#     time.sleep(2)
#     driver.find_element_by_id('com.youdao.note:id/add_note_floater_add_note').click()
#     #点击取消按钮
#     time.sleep(2)
#     driver.find_element_by_id('com.youdao.note:id/btn_cancel').click()
#     #输入内容
#     time.sleep(2)
#     #driver.find_element_by_class_name('android.widget.EditText').send_keys('testcontex1231')
#     driver.find_element_by_xpath("//*[@resource-id='com.youdao.note:id/note_content']/android.widget.EditText").send_keys('testcontex1231')
#
#     #输入标题
#     time.sleep(2)
#     driver.find_element_by_id('com.youdao.note:id/note_title').send_keys('testtitle')
#     #点击完成按钮
#     time.sleep(2)
#     driver.find_element_by_class_name('android.support.v7.widget.LinearLayoutCompat').click()
#
#
#V1.0 实现新增笔记测试
# # 导入appium类库
import unittest

from appium.webdriver.webdriver import WebDriver
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class yd_addnote(unittest.TestCase):
    # 使用初始化方法设置测试参数
    def setUp(self):
        self.caps = {}
        self.caps['automationName']='Appium'
        self.caps['platformName']='Android'
        self.caps['platformVersion']='6.0'
        self.caps['deviceName']='192.168.141.101:5555'
        self.caps['appPackage']='com.youdao.note'
        self.caps['appActivity']='.activity2.MainActivity t362'

        self.driver=WebDriver('http://127.0.0.1:4723/wd/hub',self.caps)
        self.driver.implicitly_wait(10)
        pass

    #进行新增笔记的测试
    def test_addnote(self):
        el = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_id('com.android.packageinstaller:id/permission_allow_button'))
        if el:
            #点击允许按钮
            self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
            #点击新增按钮
            self.driver.find_element_by_id('com.youdao.note:id/add_note').click()
            #点击新建笔记
            self.driver.find_element_by_id('com.youdao.note:id/add_note_floater_add_note').click()
            #点击取消按钮
            self.driver.find_element_by_id('com.youdao.note:id/btn_cancel').click()
            #输入内容
            #driver.find_element_by_class_name('android.widget.EditText').send_keys('testcontex1231')
            self.driver.find_element_by_xpath("//*[@resource-id='com.youdao.note:id/note_content']/android.widget.EditText").send_keys('testcontex1231')

            #输入标题
            self.driver.find_element_by_id('com.youdao.note:id/note_title').send_keys('testtitle')
            #点击完成按钮
            self.driver.find_element_by_class_name('android.support.v7.widget.LinearLayoutCompat').click()

    def test_addnote_flow(self,driver):
        el = WebDriverWait(driver, 10).until(
            lambda x: x.find_element_by_id('com.android.packageinstaller:id/permission_allow_button'))
        if el:
            # 点击允许按钮
            driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
            # 点击新增按钮
            driver.find_element_by_id('com.youdao.note:id/add_note').click()
            # 点击新建笔记
            driver.find_element_by_id('com.youdao.note:id/add_note_floater_add_note').click()
            # 点击取消按钮
            driver.find_element_by_id('com.youdao.note:id/btn_cancel').click()
            # 输入内容
            # driver.find_element_by_class_name('android.widget.EditText').send_keys('testcontex1231')
            driver.find_element_by_xpath(
                "//*[@resource-id='com.youdao.note:id/note_content']/android.widget.EditText").send_keys(
                'testcontex1231')

            # 输入标题
            driver.find_element_by_id('com.youdao.note:id/note_title').send_keys('testtitle')
            # 点击完成按钮
            driver.find_element_by_class_name('android.support.v7.widget.LinearLayoutCompat').click()
    def check_addnote(self):
        title=self.driver.find_element_by_id('com.youdao.note:id/title').text
        print(title)

if __name__ == '__main__':

    yd_addnote_obj=yd_addnote()
    yd_addnote_obj.test_addnote()
    yd_addnote_obj.check_addnote()

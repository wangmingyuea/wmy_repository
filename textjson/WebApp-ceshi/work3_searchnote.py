#进行查询功能的测试
# # 导入appium类库
from appium.webdriver.webdriver import WebDriver
import time

class yd_searchnote():
    def __init__(self):
        # self.caps = {}
        # self.caps['automationName']='UiAutomator2'
        # self.caps['platformName']='Android'
        # self.caps['platformVersion']='6.0'
        # self.caps['deviceName']='192.168.141.101:5555'
        # self.caps['appPackage']='com.youdao.note'
        # self.caps['appActivity']='.activity2.MainActivity t362'
        #
        # self.driver=WebDriver('http://127.0.0.1:4723/wd/hub',self.caps)
        # self.driver.implicitly_wait(10)
        pass

    def test_searchnote(self):
        #点击搜索按钮
        self.driver.find_element_by_id('com.youdao.note:id/search').click()
        #输入搜索关键字
        self.driver.find_element_by_id('com.youdao.note:id/search_edit_view').send_keys("test")
        #点击搜索按钮
        self.driver.find_element_by_id('com.youdao.note:id/clear_search_text_btn').click()
        self.driver.get_screenshot_as_file('searchnote.png')
        time.sleep(3)

    def test_searchnote_flow(self,driver):
        # 点击搜索按钮
        driver.find_element_by_id('com.youdao.note:id/search').click()
        # 输入搜索关键字
        driver.find_element_by_id('com.youdao.note:id/search_edit_view').send_keys("test")
        # 点击搜索按钮
        driver.find_element_by_id('com.youdao.note:id/clear_search_text_btn').click()
        #抓取查询结果对应的界面图
        driver.get_screenshot_as_file('searchnote.png')
        time.sleep(3)
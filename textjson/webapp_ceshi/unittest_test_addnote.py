#使用unittest框架完成新增笔记的脚本
# # 导入appium类库
from appium.webdriver.webdriver import WebDriver
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import unittest
import warnings
from webapp_ceshi.HTMLTestRunner  import HTMLTestRunner
#定义测试类
class TestAddnote(unittest.TestCase):
    def setUp(self):
        warnings.filterwarnings("ignore") #过滤警告信息
        self.caps = {}
        self.caps['automationName'] = 'UiAutomator2'
        self.caps['platformName'] = 'Android'
        self.caps['platformVersion'] = '6.0'
        self.caps['deviceName'] = '192.168.141.101:5555'
        self.caps['appPackage'] = 'com.youdao.note'
        self.caps['appActivity'] = '.activity2.MainActivity t362'

        self.driver = WebDriver('http://127.0.0.1:4723/wd/hub', self.caps)
        self.driver.implicitly_wait(10)
    #测试新增笔记
    def test_case1(self):
        el = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_id('com.android.packageinstaller:id/permission_allow_button'))
        if el:
            # 点击允许按钮
            self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
            # 点击新增按钮
            self.driver.find_element_by_id('com.youdao.note:id/add_note').click()
            # 点击新建笔记
            self.driver.find_element_by_id('com.youdao.note:id/add_note_floater_add_note').click()
            # 点击取消按钮
            self.driver.find_element_by_id('com.youdao.note:id/btn_cancel').click()
            # 输入内容
            # driver.find_element_by_class_name('android.widget.EditText').send_keys('testcontex1231')
            self.driver.find_element_by_xpath(
                "//*[@resource-id='com.youdao.note:id/note_content']/android.widget.EditText").send_keys(
                'testcontex1231')

            # 输入标题
            self.driver.find_element_by_id('com.youdao.note:id/note_title').send_keys('testtitle')
            # 点击完成按钮
            self.driver.find_element_by_class_name('android.support.v7.widget.LinearLayoutCompat').click()
            time.sleep(3)
            #获取新增成功后的标题内容
            rtitle = self.driver.find_element_by_id('com.youdao.note:id/title').text
            self.assertEqual(rtitle,'testtitle',"新增笔记测试失败")

    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    #unittest.main()
    # 生成测试套
    suiteObj = unittest.makeSuite(TestAddnote)
    # 创建测试报告文件
    file = open("d:\\reportydaddnote.html", "wb")
    runner = HTMLTestRunner(stream=file, title='独立脚本测试', description='新增')
    runner.run(suiteObj)

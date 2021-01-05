# # 导入appium类库
from appium.webdriver.webdriver import WebDriver
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class yd_addnotev3:
    def test_addnote(self,driver):

        el = WebDriverWait(driver, 10).until(
            lambda x: x.find_element_by_id('com.android.packageinstaller:id/permission_allow_button'))
        if el:
            #点击允许按钮
            driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
            #点击新增按钮
            driver.find_element_by_id('com.youdao.note:id/add_note').click()
            #点击新建笔记
            driver.find_element_by_id('com.youdao.note:id/add_note_floater_add_note').click()
            #点击取消按钮
            driver.find_element_by_id('com.youdao.note:id/btn_cancel').click()
            #输入内容
            #driver.find_element_by_class_name('android.widget.EditText').send_keys('testcontex1231')
            driver.find_element_by_xpath("//*[@resource-id='com.youdao.note:id/note_content']/android.widget.EditText").send_keys('testcontex1231')

            #输入标题
            driver.find_element_by_id('com.youdao.note:id/note_title').send_keys('testtitle')
            #点击完成按钮
            driver.find_element_by_class_name('android.support.v7.widget.LinearLayoutCompat').click()

    def check_addnote(self,driver):
        title=driver.find_element_by_id('com.youdao.note:id/title').text
        print(title)
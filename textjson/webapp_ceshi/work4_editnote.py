#进行修改功能的测试
from appium.webdriver.webdriver import WebDriver
from webapp_ceshi.common_class import comm_class
import time

class yd_editnote():
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

    def test_editnote(self):
        self.driver.find_element_by_id('com.youdao.note:id/title').click()
        self.driver.find_element_by_id('com.youdao.note:id/edit').click()
        # 修改内容
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.youdao.note:id/note_content']/android.widget.EditText").send_keys('editcon')

        # 输入标题
        self.driver.find_element_by_id('com.youdao.note:id/note_title').send_keys('editt')
        # 点击完成
        self.driver.find_element_by_class_name('android.support.v7.widget.LinearLayoutCompat').click()
        # driver.find_element_by_class_name('android.widget.ImageButton').click()
        time.sleep(3)

    def test_editnote_flow(self,driver):
        driver.find_element_by_id('com.youdao.note:id/title').click()
        driver.find_element_by_id('com.youdao.note:id/edit').click()
        # 修改内容
        driver.find_element_by_xpath(
            "//*[@resource-id='com.youdao.note:id/note_content']/android.widget.EditText").send_keys('editcon')

        # 输入标题
        driver.find_element_by_id('com.youdao.note:id/note_title').send_keys('editt')
        # 点击完成
        driver.find_element_by_class_name('android.support.v7.widget.LinearLayoutCompat').click()
        # driver.find_element_by_class_name('android.widget.ImageButton').click()
        #获取修改后的标题
        rtitle=driver.find_element_by_id('com.youdao.note:id/note_title').text
        print(rtitle)
        if(rtitle=="editt"):
            print("修改成功")
        else:
            print("修改失败")

        time.sleep(3)


if __name__ == '__main__':

    editobj=yd_editnote()


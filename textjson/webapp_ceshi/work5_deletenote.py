#删除笔记测试
class yd_deletenote:
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

    def test_deletenote(self):
        self.driver.find_element_by_id('com.youdao.note:id/menu_more').click()
        self.driver.find_element_by_id('com.youdao.note:id/delete').click()
        self.driver.find_element_by_id('com.youdao.note:id/btn_ok').click()

    def test_deletenote_flow(self,driver):
        driver.find_element_by_id('com.youdao.note:id/menu_more').click()
        driver.find_element_by_id('com.youdao.note:id/delete').click()
        driver.find_element_by_id('com.youdao.note:id/btn_ok').click()
        num=driver.find_elements_by_class_name('android.widget.LinearLayout')
        print(num)
        if len(num)>0:
            print("删除不成功")
            driver.get_screenshot_as_file('deleteerror.png')
        else:
            print("删除成功")
            driver.get_screenshot_as_file('deletesucc.png')

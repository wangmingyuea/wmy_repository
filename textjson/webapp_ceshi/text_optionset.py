#使用unittest框架完成新增笔记的脚本
# 自动化脚本框架：
#1，导入unittest包
# 2，定义测试类（继承testcase类）
# 3，定义测试方法（测试用例）；a，setup方法初始化
#                b，test_XXX，执行测试方法/assert断言进行结果比对
#                c，teardown测试后续收尾（关闭驱动），
# 4，在主函数main中进行调用
# # 导入appium类库
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
import time
from selenium.webdriver.support.wait import WebDriverWait
import unittest #1，导入unittest包
import warnings
#定义测试类
class yd_addnote(unittest.TestCase): #2.定义测试类TestCase
    def setUp(self):
        warnings.filterwarnings("ignore") #过滤警告信息
        self.caps={}
        self.caps['automationName']='Appium'
        self.caps['platformName']='Android'
        self.caps['platformVersion']='10'
        self.caps['deviceName']='HUAWEI Mate 10'
        self.caps['udid']='DXT0217A23003150'
        self.caps['appPackage'] = 'com.youdao.note'
        self.caps['appActivity'] = '.activity2.MainActivity t2079'

        self.driver = WebDriver('http://127.0.0.1:4723/wd/hub', self.caps)
        self.driver.implicitly_wait(10)

    # #测试新增笔记
    def test_case1(self):
        # el = WebDriverWait(self.driver, 10).until(
        #     lambda x: x.find_element_by_id('com.android.permissioncontroller:id/permission_allow_button'))
        # if el:
        #     # 点击允许按钮
        #     print("点击允许按钮")
        #     self.driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_button').click()
            # 点击新增按钮
            time.sleep(2)
            self.driver.find_element_by_id('com.youdao.note:id/add_note').click()
            print("点击新增按钮")
            # 点击新建笔记
            time.sleep(2)
            # self.driver.find_element_by_id('com.youdao.note:id/add_note_floater_add_note').click()
            TouchAction(self.driver).tap(x=117,y=1122).release().perform()
            print("点击新建笔记")
            # 输入内容
            # driver.find_element_by_class_name('android.widget.EditText').send_keys('testcontex1231')
            time.sleep(2)
            self.driver.find_element_by_xpath(
                "//*[@resource-id='com.youdao.note:id/note_content']/android.widget.EditText").send_keys(
                'testcontex1231')

            # 输入标题
            time.sleep(2)
            self.driver.find_element_by_id('com.youdao.note:id/note_title').send_keys('testtitle')
            # 点击完成按钮
            time.sleep(2)
            TouchAction(self.driver).tap(x=939,y=147).release().perform()
            # self.driver.find_element_by_class_name('android.support.v7.widget.LinearLayoutCompat').click()
            time.sleep(3)
            #获取新增成功后的标题内容
            rtitle = self.driver.find_element_by_id('com.youdao.note:id/title').text
            self.assertEqual(rtitle,'testtitle',"新增笔记测试失败")

    # def test_case2(self):
    #         #选中某个笔记内容，点击打开
    #         self.driver.find_element_by_id('com.youdao.note:id/title').click()
    #         #选中设置菜单按钮
    #         TouchAction(self.driver).tap(x=588, y=900.7).release().perform()
    #         #设置加密单选按钮
    #         self.driver.find_element_by_id('com.youdao.note:id/favorite').click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
import unittest
import warnings

from appium.webdriver.webdriver import WebDriver
import random
# 计算机自动测试2.2版，使用循环实现多组数据
#定义一个字典类型，存放参数设置
class yd_addnote(unittest.TestCase):
    def setUp(self):
        warnings.filterwarnings("ignore") #过滤警告信息
        self.caps={}
        self.caps['automationName']='Appium'
        self.caps['platformName']='Android'
        self.caps['platformVersion']='10'
        self.caps['deviceName']='HUAWEI Mate 10'
        self.caps['udid']='DXT0217A23003150'
        self.caps['appPackage']='com.youdao.note'
        self.caps['appActivity']='.activity2.MainActivity t2079'

        self.driver=WebDriver('http://127.0.0.1:4723/wd/hub',self.caps)
        self.driver.implicitly_wait(25)

        # #传入相关测试数据
        x=7
        x=input("请输入一个值：")
        # 生成随机数
        def test_case1(self):
            for i in range(0,8):
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                exresult = int(x) + int(y)
                self.driver.find_element_by_id('com.android.calculator2:id/digit_' + str(x)).click()
                self.driver.find_element_by_id('com.android.calculator2:id/op_add').click()
                self.driver.find_element_by_id('com.android.calculator2:id/digit_'+str(y)).click()
                self.driver.find_element_by_id('com.android.calculator2:id/eq').click()
                # 获取运行结果
                result = self.driver.find_element_by_id('com.android.calculator2:id/formula').text
                print(result)
                # 进行结果比对
                if (int(result) == int(exresult)):
                    print(str(x)+"+"+str(y)+"测试通过")
                else:
                    print("测试失败")

if __name__ == '__main__':
    # yd_addnote_obj=yd_addnote()
    unittest.main()
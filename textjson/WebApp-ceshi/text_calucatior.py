from appium.webdriver.webdriver import WebDriver
# 计算机自动测试2.1版
#定义一个字典类型，存放参数设置
caps={}
caps['automationName']='Appium'
caps['platformName']='Android'
caps['platformVersion']='10'
caps['deviceName']='HUAWEI Mate 10'
caps['deviceName']='192.168.1.37:5566'
caps['appPackage']='com.android.calculator2'
caps['appActivity']='.Calculator'

driver=WebDriver('http://127.0.0.1:4723/wd/hub',caps)
# driver.implicitly_wait(25)
#
# # #传入相关测试数据
# x=7
x=input("请输入一个值：")
exresult=int(x)+8
driver.find_element_by_id('com.android.calculator2:id/digit_'+str(x)).click()
driver.find_element_by_id('com.android.calculator2:id/op_add').click()
driver.find_element_by_id('com.android.calculator2:id/digit_8').click()
driver.find_element_by_id('com.android.calculator2:id/eq').click()
#获取运行结果
result=driver.find_element_by_id('com.android.calculator2:id/formula').text
print(result)
#进行结果比对
if(int(result)==int(exresult)):
    print("测试通过")
else:
    print("测试失败")
#V1.0 实现手机端计算器自动化测试：使用常量进行参数传递

#导入appium类库
from appium.webdriver.webdriver import WebDriver

#定义一个字典类型，存放参数设置
# caps={}
# caps['automationName']='UiAutomator2'
# caps['platformName']='Android'
# caps['platformVersion']='6.0'
# caps['deviceName']='192.168.141.101:5555'
# caps['appPackage']='com.android.calculator2'
# caps['appActivity']='.Calculator'
#
# driver=WebDriver('http://127.0.0.1:4723/wd/hub',caps)
# #传入相关测试数据
# driver.find_element_by_id('com.android.calculator2:id/digit_7').click()
# driver.find_element_by_id('com.android.calculator2:id/op_add').click()
# driver.find_element_by_id('com.android.calculator2:id/digit_8').click()
# driver.find_element_by_id('com.android.calculator2:id/eq').click()
# #获取运行结果
# result=driver.find_element_by_id('com.android.calculator2:id/formula').text
# #print(result)
# #进行结果比对
# if(int(result)==15):
#     print("测试通过")
# else:
#     print("测试失败")



#V2.1 实现手机端计算器自动化测试：使用变量进行参数传递

#导入appium类库
# from appium.webdriver.webdriver import WebDriver
#
# #定义一个字典类型，存放参数设置
# caps={}
# caps['automationName']='UiAutomator2'
# caps['platformName']='Android'
# caps['platformVersion']='6.0'
# caps['deviceName']='192.168.141.101:5555'
# caps['appPackage']='com.android.calculator2'
# caps['appActivity']='.Calculator'
#
# driver=WebDriver('http://127.0.0.1:4723/wd/hub',caps)
# #传入相关测试数据
# x=input("请输入一个值")
# exresult=int(x)+8
# driver.find_element_by_id('com.android.calculator2:id/digit_'+str(x)).click()
# driver.find_element_by_id('com.android.calculator2:id/op_add').click()
# driver.find_element_by_id('com.android.calculator2:id/digit_8').click()
# driver.find_element_by_id('com.android.calculator2:id/eq').click()
# #获取运行结果
# result=driver.find_element_by_id('com.android.calculator2:id/formula').text
# #print(result)
# #进行结果比对
# if(int(result)==int(exresult)):
#     print("测试通过")
# else:
#     print("测试失败")

# #V2.2 实现手机端计算器自动化测试：使用循环+多组变量进行参数传递
#
# #导入appium类库
# from appium.webdriver.webdriver import WebDriver
# import random
# #定义一个字典类型，存放参数设置
# caps={}
# caps['automationName']='UiAutomator2'
# caps['platformName']='Android'
# caps['platformVersion']='6.0'
# caps['deviceName']='192.168.141.101:5555'
# caps['appPackage']='com.android.calculator2'
# caps['appActivity']='.Calculator'
#
# driver=WebDriver('http://127.0.0.1:4723/wd/hub',caps)
# #传入相关测试数据
# #生成随机数
# for i in range(0,3):
#     x = random.randint(0, 9)
#     y = random.randint(0, 9)
#     exresult=int(x)+int(y)
#     driver.find_element_by_id('com.android.calculator2:id/digit_'+str(x)).click()
#     driver.find_element_by_id('com.android.calculator2:id/op_add').click()
#     driver.find_element_by_id('com.android.calculator2:id/digit_'+str(y)).click()
#     driver.find_element_by_id('com.android.calculator2:id/eq').click()
#     #获取运行结果
#     result=driver.find_element_by_id('com.android.calculator2:id/formula').text
#     #print(result)
#     #进行结果比对
#     if(int(result)==int(exresult)):
#         print(str(x)+"+"+str(y)+"测试通过")
#     else:
#         print(str(x)+"+"+str(y)+"测试失败")
#


#V3.0 实现手机端计算器自动化测试：使用文件方式进行参数传递

#导入appium类库
# from appium.webdriver.webdriver import WebDriver
# import random
# import csv
#
# #定义一个字典类型，存放参数设置
# caps={}
# caps['automationName']='UiAutomator2'
# caps['platformName']='Android'
# caps['platformVersion']='6.0'
# caps['deviceName']='192.168.141.101:5555'
# caps['appPackage']='com.android.calculator2'
# caps['appActivity']='.Calculator'
#
# driver=WebDriver('http://127.0.0.1:4723/wd/hub',caps)
# #传入相关测试数据
# #通过文件获取测试数据
# file=open("testdata.csv","r")
# table=csv.reader(file)
# file2=open("testresult.csv","w",newline='')
# writer=csv.writer(file2)
# for row  in table:
#     x=row[0]
#     y=row[1]
#     exresult=row[2]
#
#     driver.find_element_by_id('com.android.calculator2:id/digit_'+str(x)).click()
#     driver.find_element_by_id('com.android.calculator2:id/op_add').click()
#     driver.find_element_by_id('com.android.calculator2:id/digit_'+str(y)).click()
#     driver.find_element_by_id('com.android.calculator2:id/eq').click()
#     #获取运行结果
#     result=driver.find_element_by_id('com.android.calculator2:id/formula').text
#     #print(result)
#     #进行结果比对
#     if(int(result)==int(exresult)):
#         row.append("测试通过")
#         writer.writerow(row)
#     else:
#         row.append("测试失败")
#         writer.writerow(row)
#
# file2.close()

#V4.0从文件中读取多位多组数的混合运算的测试
#导入appium类库
from appium.webdriver.webdriver import WebDriver
import random
import csv

#定义一个字典类型，存放参数设置
caps={}
caps['automationName']='Appium'
caps['platformName']='Android'
caps['platformVersion']='10'
caps['deviceName']='HUAWEI Mate 10'
caps['udid']='DXT0217A23003150'
caps['appPackage']='com.android.calculator2'
caps['appActivity']='.Calculator'

driver=WebDriver('http://127.0.0.1:4723/wd/hub',caps)
#传入相关测试数据
#通过文件获取测试数据
file=open("testdata3.csv","r")
tables=csv.reader(file)
for row in tables:
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])
    driver.find_element_by_id('com.android.calculator2:id/formula').send_keys(row[0]+row[1]+row[2])
    driver.find_element_by_id('com.android.calculator2:id/eq').click()
    result=driver.find_element_by_id('com.android.calculator2:id/formula').text
    if(int(result)==int(row[3])):
        print("测试通过")
    else:
        print("测试失败")
    driver.fin
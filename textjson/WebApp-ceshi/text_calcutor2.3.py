from appium.webdriver.webdriver import WebDriver
import random
import csv

# 实现手机自动化V2.3版，从文件中读取测试数据
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

# 生成随机数
# 通过文件读取随机数
file=open("textdatas.csv","r")
table=csv.reader(file)
for row in table:
    x=row[0]
    y=row[1]
    exresult = row[2]
    driver.find_element_by_id('com.android.calculator2:id/digit_' + str(x)).click()
    driver.find_element_by_id('com.android.calculator2:id/op_add').click()
    driver.find_element_by_id('com.android.calculator2:id/digit_'+str(y)).click()
    driver.find_element_by_id('com.android.calculator2:id/eq').click()
    # 获取运行结果
    result = driver.find_element_by_id('com.android.calculator2:id/formula').text
    print(result)
    # 进行结果比对
    if (int(result) == int(exresult)):
        print(str(x)+"+"+str(y)+"测试通过")
    else:
        print(str(x)+"+"+str(y)+"测试失败")
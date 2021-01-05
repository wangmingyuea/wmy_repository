from appium.webdriver.webdriver import WebDriver

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
driver.install_app('/Users/wangmingxiao/Downloads/YoudaoNote.dmg')

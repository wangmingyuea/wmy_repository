import csv

from appium.webdriver.webdriver import WebDriver

if __name__ == '__main__':
    caps = {}
    caps['automationName'] = 'Appium'
    caps['platformName'] = 'Android'
    caps['platformVersion'] = '10'
    caps['deviceName'] = 'HUAWEI Mate 10'
    caps['deviceName'] = '192.168.1.37:5566'
    caps['appPackage'] = 'com.android.calculator2'
    caps['appActivity'] = '.Calculator'

    driver = WebDriver('http://127.0.0.1:4723/wd/hub', caps)
    # 传入相关测试数据
    # 通过文件获取测试数据
    file = open("textdatas.csv", "r")
    tables = csv.reader(file)
    for row in tables:
        caps[row[0]] = row[1]
        caps[row[2]] = row[3]
        caps[row[4]] = row[5]
        caps[row[6]] = row[7]
        print(row[0])
        print(row[1])
        print(row[2])
        print(row[3])
        driver.find_element_by_id('com.android.calculator2:id/formula').send_keys(row[0] + row[1] + row[2])
        driver.find_element_by_id('com.android.calculator2:id/eq').click()
        result = driver.find_element_by_id('com.android.calculator2:id/formula').text
        if (int(result) == int(row[3])):
            print("测试通过")
        else:
            print("测试失败")







#V3.0 实现任意设备的兼容性测试
import csv
#导入appium类库
from appium.webdriver.webdriver import WebDriver
#导入V1.0相关内容
from youdaoproject.work1_install_remove import yd_install_removeV1

if __name__ == '__main__':
    #实例化测试V1.0对象
    yd_install_remove_Obj=yd_install_removeV1()

    #从文件中读取相关的参数值

    file = open("testpara.csv", "r")
    tables = csv.reader(file)
    yd_install_remove_Obj.caps = {}
    yd_install_remove_Obj.caps['automationName'] = 'UiAutomator2'
    yd_install_remove_Obj.caps['platformName'] = 'Android'
    for rows in tables:
        # print(rows[0])
        # print(rows[1])
        # print(rows[2])
        # print(rows[3])
        # print(rows[4])
        # print(rows[5])

        yd_install_remove_Obj.caps[rows[0]] = rows[1]
        yd_install_remove_Obj.caps[rows[2]] = rows[3]
        yd_install_remove_Obj.caps[rows[4]] = rows[5]
        yd_install_remove_Obj.caps[rows[6]] = rows[7]

        yd_install_remove_Obj.driver = WebDriver('http://127.0.0.1:4723/wd/hub', yd_install_remove_Obj.caps)
        yd_install_remove_Obj.test_install_remove()
        yd_install_remove_Obj.check_install()
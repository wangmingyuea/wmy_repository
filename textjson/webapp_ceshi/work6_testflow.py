
#进行业务场景的测试（新增—>查询—>修改—>删除）

# # 导入appium类库
from appium.webdriver.webdriver import WebDriver
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webapp_ceshi.work2_addnote import yd_addnote
from webapp_ceshi.work3_searchnote import yd_searchnote
from webapp_ceshi.common_class import comm_class
from webapp_ceshi.work4_editnote import yd_editnote
from webapp_ceshi.work5_deletenote import yd_deletenote
#加入新增功能脚本测试
if __name__ == '__main__':
    #实例化公共类，进行参数设置，返回driver
    comobj=comm_class()
    driver=comobj.get_driver()
    #进行对象的实例化
    addobj=yd_addnote()
    searchobj=yd_searchnote()
    editobj=yd_editnote()
    deletobj=yd_deletenote()
    #进行功能测试
    addobj.test_addnote_flow(driver)
    searchobj.test_searchnote_flow(driver)
    editobj.test_editnote_flow(driver)
    deletobj.test_deletenote_flow(driver)






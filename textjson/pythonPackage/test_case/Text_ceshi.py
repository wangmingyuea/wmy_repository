from selenium import webdriver
import time
# 导入提供拖拽元素方法的模块ActionChains
from selenium.webdriver import ActionChains
from selenium.webdriver.common import action_chains

class Selenium(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        time.sleep(2)

    def visit_index(self):
        self.driver.get ('http://business-management.redbull05.top/login.html')
        time.sleep(5)
        # 输入账号、密码
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('ceshi')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
        time.sleep(3)
        # 拖动滚动条
        handler_bg = self.driver.find_element_by_xpath('//*[@id="drag"]/div[3]')
        action = ActionChains(self.driver)
        action.click_and_hold(handler_bg).perform()
        action.reset_actions()
        action.move_by_offset(xoffset=220, yoffset=0).perform()
        # move_list = ([0, 0], [199, 199])
        # if handler_bg:
        #     ActionChains(self.driver).click_and_hold(on_element=handler_bg).perform()
        #     for m in move_list:
        # ActionChains(self.driver).drag_and_drop_by_offset(handler_bg, xoffset=199, yoffset=199)
        time.sleep(3)

        self.driver.find_element_by_class_name('loginBut').click()
        time.sleep(10)


if __name__ == '__main__':
    New_Selenium = Selenium()
    New_Selenium.visit_index()
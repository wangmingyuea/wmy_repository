# -*- coding: utf-8 -*-
# @Time        : 2020/7/20 10:02 上午
# @Author      : 代志伟
# @Email       : daizhiwei@aojinzhice.com
# @File        : business_management.py
import pyautogui
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
        self.driver.get('http://business-management.redbull05.top/login.html')
        time.sleep(1)
        # 浏览器窗口最大化
        self.driver.maximize_window()
        time.sleep(2)
        # 输入账号、密码
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('ceshi')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
        time.sleep(1)
        # 拖动滚动条
        handler_bg = self.driver.find_element_by_xpath('//*[@id="drag"]/div[3]')
        action = ActionChains(self.driver)
        action.click_and_hold(handler_bg).perform()
        action.reset_actions()
        action.move_by_offset(xoffset=230, yoffset=0).perform()
        time.sleep(3)

        self.driver.find_element_by_class_name('loginBut').click()
        time.sleep(3)

    def income_settlement_statistics(self):
        """
        进入收入结算统计页面
        """
        self.driver.find_element_by_xpath('//*[@id="nav"]/li[3]/a/cite').click()
        time.sleep(2)

    def find_export_date(self):
        """
        滑动滚动条到底部
        """
        # # 保护措施，避免失控
        # pyautogui.FAILSAFE = True
        # # 为所有的PyAutoGUI函数增加延迟。默认延迟时间是0.1秒。
        # pyautogui.PAUSE = 0.5
        # 鼠标移动到屏幕正中间，并点击，以使鼠标聚焦在页面中
        screenWidth, screenHeight = pyautogui.size()
        pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
        pyautogui.click()
        # 模拟键盘，点按向下箭头5次
        pyautogui.press(['down', 'down', 'down', 'down', 'down'])

        time.sleep(1)

    def internal_data_export(self):
        """
        导出内部数据
        """
        time.sleep(10)
        # self.driver.find_elements_by_class_name('addBut').click()
        self.driver.find_element_by_css_selector('button.addBut.bggreen').click()

        time.sleep(1)
        # 由于默认选中导出内部数据按钮，因此直接点击确认导出按钮
        self.driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a').click()
        time.sleep(15)

    def external_data_export(self):
        """
        导出外部数据
        """
        time.sleep(3)
        self.driver.find_elements_by_class_name ('addBut bggreen')[0].click ( )
        time.sleep(1)
        # 选中导出外部数据前面的单选按钮
        self.driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[2]/div[2]/input').click()
        time.sleep(1)
        # 点击确认导出按钮
        self.driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a').click()
        time.sleep(15)

if __name__ == '__main__':
    New_Selenium = Selenium()
    New_Selenium.visit_index()
    New_Selenium.income_settlement_statistics()
    New_Selenium.find_export_date()
    New_Selenium.internal_data_export()
    New_Selenium.external_data_export()
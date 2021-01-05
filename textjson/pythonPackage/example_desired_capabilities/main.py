#!/usr/bin/python
# -*- coding: UTF-8 -*-

from appium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import  expected_conditions as EC

import unittest

import time

from time import sleep

from pythonPackage.example_desired_capabilities import desired_capabilities


class AndroidTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # 获取（引用）desired_capabilities.py 里面get_desired_capabilities()的方法
        desired_cap = desired_capabilities.get_desired_capabilities()
        # 获取（引用）desired_capabilities.py 里面get_uri()的方法
        uri = desired_capabilities.get_uri()

        self.driver = webdriver.Remote(uri,desired_cap) # 调用uri,desired_cap

    def test_case_link_wudongjianghu(self,number=1):
        time.sleep(4)
        # self.driver.find_element_by_id('com.tencent.mm:id/r_').click()
        self.driver.find_elements_by_id('com.tencent.mm:id/baj')[0].click()

if __name__ == '__main__':
    unittest.main()
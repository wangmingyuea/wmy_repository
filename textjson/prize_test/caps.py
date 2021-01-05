#!/usr/bin/python
# -*- coding: UTF-8 -*-


def get_desired_capabilities():
    desired_caps = {
        "AutomationName": "Appium",
        "platformName": "Android",
        "platformVersion": "10.0.0",
        "deviceName": "HUAWEI Mate 10",
        # "udid": "DXT0217A23003150",
        "udid": "192.168.1.2:4520",
        "newCommandTimeout": "60",
        "appPackage": "com.tencent.mm",
        "appActivity": ".ui.LauncherUI",
        "chromeOptions": {'androidProcess': 'com.tencent.mm:tools'},
        "noReset": True
    }

    return desired_caps


def get_url():
    return 'http://127.0.0.1:4723/wd/hub'
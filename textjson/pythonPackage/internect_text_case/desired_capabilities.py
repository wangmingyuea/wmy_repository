#!/usr/bin/python
# -*- coding: UTF-8 -*-

def get_desired_capabilities():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "8.1.0",
        "udid": "10.224.136.13:4455",
        # "app": "/Users/xxxx/Desktop/appium自动化测试/AndroidTest-8.0.apk",
        "automationName": "Appium",
        "deviceName": "OPPO R15 梦境版",
        "newCommandTimeout": 60,
        # "appWaitActivity": "com.ut.roidpt.engine.app.core.BootActivity",
        "appPackage":"com.tencent.mm",
        "appActivity":".ui.LauncherUI",
        # "unicodeKeyboard": True,
        # "resetKeyboard": True,
        # "autoGrantPermissions": True,
        "noReset": True

    }
    return desired_caps

def get_uri():
    return 'http://127.0.0.1:4723/wd/hub'
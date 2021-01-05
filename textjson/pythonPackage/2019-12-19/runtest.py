# -*- coding: utf-8 -*
import unittest

import os

from unittest_fram.test_case.HTMLTestRunner import HTMLTestRunner




# discover找出以test开头的用例
def allTests():
    suite = unittest.TestLoader().discover(
        start_dir=os.path.dirname('formal_prize_test.test_case_old')
        , pattern='test_*.py',
        top_level_dir=None)
    return suite


def run():
    unittest.TextTestRunner(verbosity=2).run(allTests())


if __name__ == '__main__':
    # 测试报告为result.html
    result_path = os.path.join("/Users/daizhiwei/Desktop/testRunner/", "result.html")

    # 打开文件，把结果写进文件中，w，有内容的话，清空了再写进去
    file = open(result_path, "wb")

    runner = HTMLTestRunner(stream=file, title='线上奖品测试', description='API奖品')
    # 调用all_case函数返回值
    runner.run(allTests())
# -*- coding: utf-8 -*
import unittest

import os

from pythonPackage.test_case.HTMLTestRunner import HTMLTestRunner




# discover找出以test开头的用例(固定)
def allTests():
    suite = unittest.TestLoader().discover(
        start_dir=os.path.dirname('pythonPackage.test_case')  # 执行pythonPackage包下的test_case文件夹的python文件
        , pattern='test_*.py',      # 执行以test_文件开头的.py文件
        top_level_dir=None)
    return suite


def run():
    unittest.TextTestRunner(verbosity=2).run(allTests())  # 固定格式


if __name__ == '__main__':
    # 测试报告为result.html
    result_path = os.path.join("/Users/wangmingxiao/Desktop/王明月/text-python", "result.html")



    # 定义测试报告
    # 打开文件，把结果写进文件中，w，有内容的话，清空了再写进去
    file = open(result_path, "wb")

    # stream是一个二进制文件
    # title：测试报告标题
    # description：测试报告的描述
    runner = HTMLTestRunner(stream=file, title='线上奖品测试', description='API奖品')
    # 调用all_case函数返回值
    runner.run(allTests())
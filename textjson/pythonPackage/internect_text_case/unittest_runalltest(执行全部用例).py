# -*- coding: utf-8 -*
# jenkins执行定时任务做断言时，需要在x.text后面加上.encode('UTF-8')

import unittest
import os
import time
import sys
from email.mime.multipart import MIMEMultipart
from pythonPackage.test_case.HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
import smtplib

from bs4 import BeautifulSoup

report_path = '/Users/wangmingxiao/Desktop/王明月/text-python/textresult.html'


# discover找出以test开头的用例
def allTest():
    suite = unittest.TestLoader().discover(
        start_dir=os.path.dirname('pythonPackage/internect_text_case')
        , pattern='Text_*.py',
        top_level_dir=None)
    return suite

# verbosity：测试结果的复杂成都
def run():
    unittest.TextTestRunner(verbosity=2).run(allTest())


def send_mail(report_path,receiver):
    a = open(report_path, "rb")  # rb 使用二进制格式打开一个文件，用于只读
    # mail_body = a.read()
    # a = open(report_path, "rb")
    mail_body = a.read()  # 读取测试报告作为邮件正文

    # 编写html类型邮件（固定）

    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = u"warn"  # Subject邮件标题
    msg["from"] = "monitor@aojinzhice.com"  # from发件邮箱
    msg["to"] = ";".join(receiver)   # to 收件邮箱
    # 邮件正文（固定）
    msg.attach(body)
    att = MIMEText(mail_body, 'base64', _charset='utf-8')
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="zhuti_jiekou_baogao.html"' # filename：附件名称 ； 添加附件
    msg.attach(att)
    smtp = smtplib.SMTP_SSL("smtp.aojinzhice.com", 465)       #全球网邮箱服务器
    smtp.login("monitor@aojinzhice.com", "MKjkx520")
    smtp.sendmail("monitor@aojinzhice.com", receiver, msg.as_string())
    smtp.quit()

def Error_sendEmail(report_path,receiver):
    try:
        # 打开html文件，读取报告内容
        print(report_path)
        with open(report_path, "r", encoding="utf-8") as fp:       #注意：python3这里一定要加encoding="utf-8"；否则会包gbk错误；
            f = fp.read()  # 读报告

         # 解析html，查找class属性attribute
        soup = BeautifulSoup(f, "html.parser")
        status = soup.find_all(class_="attribute")
        print(status)

        resul = status[2].contents[-1]  # 获取报告结果
        print(resul)
        result = str(resul)
        print(result)

        if "Failure" in result or "Error" in result:
            print("测试过程有不通过用例：%s" % result)
            send_mail(report_path, receiver)
            return False
        else:
            return True
    except:
        print("判断过程出现异常")
        return False


# 查找目录下最新生成的测试报告,返回最新报告的详细路径
def find_report(report_path):
    lists = os.listdir("/Users/wangmingxiao/Desktop/王明月/text-python/textresult.html")
    lists.sort(key=lambda fn: os.path.getmtime(report_path + "\\" + fn))
    newfile = os.path.join(report_path, lists[-1])
    print(newfile)
    print(report_path)
    return newfile



if __name__ == '__main__':
    now = time.strftime ("%Y-%m-%d %H_%M_%S", time.localtime ( ))
    report_path = r"/Users/wangmingxiao/Desktop/王明月/text-python/textresult" + now + ".html"
    fp = open(report_path, "wb")
    # 定义测试报告
    # stream是一个二进制文件
    # title：测试报告标题
    # description：测试报告的描述
    runner = HTMLTestRunner(stream=fp, title=u'自动化测试生成测试报告-练习', description=u"测试结果：通过")
    # 用来运行测试用例
    runner.run(allTest())
    fp.close()
    receiver = ["wangmingyue@aojinzhice.com"]

    Error_sendEmail(report_path, receiver)
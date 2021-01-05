# -*- coding: utf-8 -*
# jenkins执行定时任务做断言时，需要在x.text后面加上.encode('UTF-8')
import sys
import os
rootpath=str("/Users/wangmingxiao/PycharmProjects/textjson")
syspath=sys.path
sys.path=[]
sys.path.append(rootpath)#将工程根目录加入到python搜索路径中
sys.path.extend([rootpath+i for i in os.listdir(rootpath) if i[0]!="."])#将工程目录下的一级目录添加到python搜索路径中
sys.path.extend(syspath)
import time
import unittest
from email.mime.multipart import MIMEMultipart
from prize_test.HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
import smtplib
from bs4 import BeautifulSoup

report_path = '/Users/wangmingxiao/Desktop/王明月/text-python/textresult.html'

# discover找出以test开头的用例
def allTest():
    suite = unittest.TestLoader().discover(
        start_dir=os.path.dirname('prize_last')
        , pattern='Text_*.py',
        top_level_dir=None)
    return suite


def run():
    unittest.TextTestRunner(verbosity=2).run(allTest())

def send_mail(report_path, receiver):
    a = open(report_path, "rb")
    mail_body = a.read()
    a = open(report_path, "rb")
    mail_body = a.read()
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = u"warn"
    msg["from"] = "monitor@aojinzhice.com"
    msg["to"] = ";".join(receiver)
    msg.attach(body)
    att = MIMEText(mail_body, 'base64', _charset='utf-8')
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="zhuti_jiekou_baogao.html"'
    msg.attach(att)
    smtp = smtplib.SMTP_SSL("smtp.aojinzhice.com", 465)       #全球网邮箱服务器
    smtp.login("monitor@aojinzhice.com", "MKjkx520")
    smtp.sendmail("monitor@aojinzhice.com", receiver, msg.as_string())
    smtp.quit()


def Error_sendEmail(report_path,receiver,):
    try:
        # 打开html文件，读取报告内容
        print(report_path)
        with open(report_path, "r", encoding="utf-8") as fp:       #注意：python3这里一定要加encoding="utf-8"；否则会包gbk错误；
            f = fp.read()  # 读报告
        soup = BeautifulSoup(f, "html.parser")
        print(soup)
        status = soup.find_all(class_="attribute")
        print(status)
        resul = status[2]  # 获取报告结果
        print(resul)
        result = str(resul)
        print(result)
        if "Failure" in result or "Error" in result:
            print ("测试过程有不通过用例：%s" % result)
            send_mail (report_path, receiver)
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
    print(time.strftime('%Y-%m-%d %X', time.localtime()))
    now = time.strftime ("%Y-%m-%d %H_%M_%S", time.localtime ( ))
    report_path = r"/Users/wangmingxiao/Desktop/王明月/text-python/textresult" + now + ".html"
    fp = open(report_path, "wb")
    runner = HTMLTestRunner(stream=fp, title=u'线上项目自动化测试报告', description=u"测试结果：通过")
    runner.run(allTest())
    fp.close()
    receiver = ["wangmingyue@aojinzhice.com"]

    Error_sendEmail(report_path, receiver)
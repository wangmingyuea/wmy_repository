#V2.0 从文件中读取测试数据进行新增笔记的测试
import time

from webapp_ceshi.work2_addnote import yd_addnote
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import csv

#定义一个子类
class yd_addnoteV2(yd_addnote):
    def test_addnote(self,title,content):
        el = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_id('com.android.packageinstaller:id/permission_allow_button'))
        if el:
            # 点击允许按钮
            self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
            # 点击新增按钮
            self.driver.find_element_by_id('com.youdao.note:id/add_note').click()
            # 点击新建笔记
            self.driver.find_element_by_id('com.youdao.note:id/add_note_floater_add_note').click()
            # 点击取消按钮
            self.driver.find_element_by_id('com.youdao.note:id/btn_cancel').click()
            # 输入内容
            # driver.find_element_by_class_name('android.widget.EditText').send_keys('testcontex1231')
            self.driver.find_element_by_xpath(
                "//*[@resource-id='com.youdao.note:id/note_content']/android.widget.EditText").send_keys(
                content)

            # 输入标题
            self.driver.find_element_by_id('com.youdao.note:id/note_title').send_keys(title)
            # 点击完成按钮
            self.driver.find_element_by_class_name('android.support.v7.widget.LinearLayoutCompat').click()
            # list=self.driver.find_elements_by_class_name("")
            # list.__len__()
            time.sleep(5)
    # def click(self):
    #         self.driver.find_element_by_class_name('android.widget.RelativeLayout').click()
    #         self.driver.get_screenshot_as_file("aaa.png")
    def check_addnote(self,title):
        rtitle = self.driver.find_element_by_id('com.youdao.note:id/title').text
        if(rtitle==title):
            return 1
        else:
            return 0
if __name__ == '__main__':
    yd_addnote_obj2 = yd_addnoteV2()
    #打开csv文件
    file=open("addnotedata.csv","r")
    tables=csv.reader(file)

    #以写模式打开测试报告文件
    file2=open("addnotetest.csv","w",newline='')
    writer=csv.writer(file2)

    for rows in tables:
        # dic[rows[0]]=rows[1]
        # print(dic)

        title=rows[0]
        content=rows[1]
        #调用新增笔记测试方法
        yd_addnote_obj2.test_addnote(title,content)
        #检查新增是否正确
        r=yd_addnote_obj2.check_addnote(title)
        if r:
            rows.append('测试通过')
            writer.writerow(rows)
        else:
            rows.append('测试失败')
            writer.writerow(rows)
        #yd_addnote_obj2.click()

    file2.close()


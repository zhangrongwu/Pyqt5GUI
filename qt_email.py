#!/usr/bin/env python
#-*- coding:utf-8 -*- 
#@Time: 2018/5/2上午11:27
#@Author:zhangrongwu
#@File:qt_email.py


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

import smtplib
from email.mime.text import MIMEText
from email.header import  Header


class Email_MaiWindow(object):
    def setupUI(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")#相当于iOS contentview

        self.label_Host = QtWidgets.QLabel(self.centralwidget)
        self.label_Host.setGeometry(QtCore.QRect(30, 10, 200, 20))
        self.label_Host.setObjectName("label_Host")
        self.label_Host.setText("webmail.xinaogroup.com")#每个公司地址不一样


        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)#相当于iOS addsubview 到父控件
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 200, 30))#相当于iOS self.lineEdit.frame = ...
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("输入你的邮箱")#站位字符串


        self.lineEdit_Pwd = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Pwd.setGeometry(QtCore.QRect(30, 90, 200, 30))
        self.lineEdit_Pwd.setObjectName("lineEdit_Pwd")
        self.lineEdit_Pwd.setPlaceholderText("输入邮箱密码")

        self.lineEdit_To = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_To.setGeometry(QtCore.QRect(260, 50, 200, 30))
        self.lineEdit_To.setObjectName("lineEdit_To")
        self.lineEdit_To.setPlaceholderText("收件人邮箱")

        self.lineEdit_Subject = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Subject.setGeometry(QtCore.QRect(260, 90, 200, 30))
        self.lineEdit_Subject.setObjectName("lineEdit_Subject")
        self.lineEdit_Subject.setPlaceholderText("主题")


        self.contentMsg = QtWidgets.QTextEdit(self.centralwidget)#多行文本框,相当于iOS UITextview
        self.contentMsg.setGeometry(QtCore.QRect(30, 130, 400, 100))
        self.contentMsg.setObjectName("contentMsg")
        self.contentMsg.setPlaceholderText("填写发送的内容")



        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(30,250, 80, 50))
        self.sendButton.setObjectName("sendButton")
        self.sendButton.setStyleSheet("font:20pt \"Agency FB\";")
        self.sendButton.setText("发送")
        self.sendButton.clicked.connect(lambda : self.send())




        MainWindow.setCentralWidget(self.centralwidget)#把父控件添加到窗口上

    def send(self):
        sender = self.lineEdit.text()
        receiver = self.lineEdit_To.text()
        content = self.contentMsg.toPlainText()
        passWord = self.lineEdit_Pwd.text()
        message = MIMEText(content, 'plain', 'utf-8')
        message["From"] = Header(sender, 'utf-8')
        message["To"] = Header(receiver, 'utf-8')

        subject = self.lineEdit_Subject.text()
        message['Subject'] = Header(subject, 'utf-8')

        mailhost = self.label_Host.text()





        # 构造附件1，传送当前目录下的 test.txt 文件
        # att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
        # att1["Content-Type"] = 'application/octet-stream'
        # # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        # att1["Content-Disposition"] = 'attachment; filename="test.txt"'
        # message.attach(att1)
        #
        # # 构造附件2，传送当前目录下的 runoob.txt 文件
        # att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
        # att2["Content-Type"] = 'application/octet-stream'
        # att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
        # message.attach(att2)

        try:
            # smtpObj = smtplib.SMTP(localhost) #如果 SMTP 在你的本机上，你只需要指定服务器地址为 localhost 即可，无需密码登陆
            smtpObj = smtplib.SMTP(mailhost, 25)#25为 SMTP 默认端口号
            smtpObj.login(sender, passWord)

            smtpObj.sendmail(sender, [receiver], message.as_string())
            smtpObj.quit()
            print("邮件发送成功")
        except smtplib.SMTPException as msg:
            print(msg)
            print("邮件无法发送")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()#创建窗口
    ui = Email_MaiWindow()#初始化Email_MaiWindow类
    ui.setupUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



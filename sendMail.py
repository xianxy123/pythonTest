#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

recvFile = open('recv_addr.csv','r',encoding='gbk') # 打开文件
recvReader = csv.reader(recvFile) # 读取收件箱
recvData = list(recvReader) # 接收邮件列表

# 第三方 SMTP 服务
send_host = 'smtp.chinaunicom.cn'  # 设置服务器
send_user = 'xianxy3@chinaunicom.cn' # 用户名
send_pwd = '*********' # 口令授权码

sender = 'xianxy3@chinaunicom.cn'

message = MIMEText('xianxy3_Python作业', 'plain', 'utf-8')
message['From'] = Header("python全栈教程", 'utf-8')
message['To'] = Header("xianxy3", 'utf-8')

subject = 'xianxy3_Python作业'
message['Subject'] = Header(subject, 'utf-8')
try:
    smtpObj = smtplib.SMTP(send_host, 25)
    smtpObj.login(send_user, send_pwd)
    smtpObj.sendmail(sender, recvData, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print( "Error: 无法发送邮件")

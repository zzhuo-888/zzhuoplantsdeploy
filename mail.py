import streamlit as st
from smtplib import SMTP_SSL

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import random
import re
from threading import Timer

data = {
    'sender':"2577982484@qq.com", # 发送者邮箱，自己用可写死
    'password':"regdayyboktpeacc", # 在

    'subject':"农作物健康识别系统", # 邮件主题名，没有违规文字都行
}


@st.cache(ttl=900)
def load_message(data, receiver, mailusername, diseasename, diseaseinfo, diseasesolve):
    sender = data.get('sender', '')  # 发送者QQ邮箱
    receiver = receiver  # 接收者邮箱
    password = data.get('password', '')
    subject = data.get('subject', '')
    message = MIMEMultipart('related')
    subject = ' 您好，请接收您的检测结果--'
    message['Subject'] = Header(subject, 'utf-8')

    msgAlternative = MIMEMultipart('alternative')
    message.attach(msgAlternative)
    mailusername = mailusername
    diseasename = diseasename
    diseaseinfo = diseaseinfo
    diseasesolve = diseasesolve
    mail_msg = f"""
    <p><img src="cid:image1"></p>
    <p>您好，{mailusername}！</p>
    <p>您的检查结果是：{diseasename}</p>
    <p>该病虫害的详细信息如下：{diseaseinfo}</p>
    <p>该病虫害的防治措施如下：{diseasesolve}</p>
    """
    msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

    # 指定图片为当前目录
    fp = open("./data/twotest/test.jpg", 'rb')

    msgImage = MIMEImage(fp.read())
    fp.close()

    # 定义图片 ID，在 HTML 文本中引用
    msgImage.add_header('Content-ID', '<image1>')
    message.attach(msgImage)
    message["Subject"] = Header(subject, "utf-8")  # 邮箱主题
    message["From"] = Header(sender)  # 发送者
    message["To"] = Header(receiver, "utf-8")  # 接收者
    #message = load_message()

    smtp = SMTP_SSL("smtp.qq.com")  # 需要发送者QQ邮箱开启SMTP服务
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, message.as_string())
    return message


class SendEmail:

    def __init__(self, data,receiver):
        self.sender = data.get('sender','') # 发送者QQ邮箱
        self.receiver = receiver # 接收者邮箱
        self.password = data.get('password','')
        self.subject = data.get('subject','')

    def load_message(self):
        verification_code = self.generate_verification()
        text = f'验证码为：{verification_code}，请您在15分钟内进行填写。' \
               f''
        message = MIMEText(text, "plain", "utf-8") # 文本内容，文本格式，编码
        message["Subject"] = Header(self.subject, "utf-8") # 邮箱主题
        message["From"] = Header(self.sender) # 发送者
        message["To"] = Header(self.receiver, "utf-8") # 接收者
        return message,verification_code

    @st.cache(ttl=900)
    def send_email(self):

        message,verification_code = self.load_message()

        smtp = SMTP_SSL("smtp.qq.com")  #需要发送者QQ邮箱开启SMTP服务
        smtp.login(self.sender, self.password)
        smtp.sendmail(self.sender, self.receiver, message.as_string())
        return verification_code

    # 生成6位随机数验证码
    @st.cache(ttl=900)
    def generate_verification(self):

        random_list = list(map(lambda x:random.randint(0,9),[y for y in range(6)])) # 这里使用map函数跟lambda匿名函数来生成随机的六位数
        code = "".join('%s' % i for i in random_list)
        return code




regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    if re.fullmatch(regex, email):
        print("有效的email地址")
        return True
    else:
        print("无效的email地址")
        return False
#调用
#receiver里放上发送对象的邮箱
#verification = SendEmail(data=data,receiver='1596214205@qq.com').send_email()
#print(verification)

#SendPessage(data=data,receiver='2577982484@qq.com').send_email()

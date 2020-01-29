from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText



def main():
    #邮件发送者和接受者

    sender='1040775289@qq.com'
    receivers='13457563463@163.com'
    message=MIMEText('用python发送邮件实例代码'，'plain','utf-8')
    message['from']=Header('网大水','utf-8')
    message['to']=Header('hansome boy','utf-8')
    message['subject']=Header('例子代码邮件'，'utf-8')
    smtper=SMTP('smtp.163.com')

     # 请自行修改下面的登录口令
    smtper.login(sender, 'secretpass')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')

    if __name__ == "__main__":
        main()
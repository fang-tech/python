# 需要实现的内容

# 使用python发邮件
# 同样可以发送带附件的邮件, 需要时自行查阅
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

def test_email():
    '''
    @brife : 发送简单邮件
    '''
    sender = "tianyufang978@gmail.com"
    receiver = ['2819187982@qq.com']
    message = MIMEText('test use python to send email', 'plain', 'utf-8')
    message['From'] = Header('发送端', 'utf-8')
    message['To'] = Header('接收端', 'utf-8')
    message['Subject'] = Header('test for python', 'utf-8')

    #  Connect to the Gmail SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port =  465
    username = 'tianyufang978@gmail.com'
    app_password = 'sbre uopx dahc toou'

    # Send the email
    try:
        print("Connecting to SMTP server")
        server = SMTP_SSL(smtp_server, smtp_port, timeout=600)
        # print("Starting TLS encryption")
        # server.starttls()  # Start TLS encryption
        print("loggin in...")
        server.login(username, app_password)
        print("Sending email...")
        server.sendmail(sender, receiver, message.as_string())
        print("Email sent successfully")
    finally:
        server.quit()


def main():
    test_email()

if __name__ == "__main__":
    main()

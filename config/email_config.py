import smtplib
from email.mime.text import MIMEText
from config.setting import EMAIL_FROM, KEY, EMAIL_TO


def send_email_html_report(content):
    """邮件提醒"""

    server = smtplib.SMTP_SSL('smtp.qq.com', 465)  # 创建SMTP连接,host服务器地址、port端口
    server.login(EMAIL_FROM, KEY)  # 邮箱登录：EMAIL_FROM发件人邮箱地址、KEY授权码
    print(KEY)

    # 创建邮件对象，邮件内容为html格式
    message = MIMEText(content, 'html', 'utf-8')
    message['From'] = EMAIL_FROM  # 发件人邮箱
    message['To'] = EMAIL_TO  # 收件人邮箱
    message['Subject'] = '自动化测试结果'

    try:
        server.sendmail(EMAIL_FROM, [message['To']], message.as_string())
        print("邮件发送成功!")
    except smtplib.SMTPException as e:
        print(f"Error: {e}")
    finally:
        server.quit()  # 关闭SMTP连接

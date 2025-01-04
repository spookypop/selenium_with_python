import base64
import smtplib
from email.mime.text import MIMEText


KEY = base64.b64decode('bnNsZWt2Z2JreHdnZWJlYQ==').decode('utf-8')

EMAIL_FROM = '2528674211@qq.com'
EMAIL_TO = '414071473@qq.com'


def send_email_html_report(content):
    mail_host = 'smtp.qq.com'  # 示例：QQ邮箱的SMTP服务器
    mail_port = 465  # 示例：使用SSL加密的端口

    # SSL加密方式
    server = smtplib.SMTP_SSL(mail_host, mail_port)
    # 或 STARTTLS方式（如果使用587端口）
    # server = smtplib.SMTP(mail_host, 587)
    # server.starttls()
    server.login(EMAIL_FROM, KEY)

    # 创建邮件对象
    message = MIMEText(content, 'html', 'utf-8')
    message['From'] = EMAIL_FROM
    message['To'] = EMAIL_TO  # 收件人邮箱
    message['Subject'] = '自动化测试结果'


    try:
        server.sendmail(EMAIL_FROM, [message['To']], message.as_string())
        print("Email sent successfully!")
    except smtplib.SMTPException as e:
        print(f"Error: {e}")
    finally:
        server.quit()  # 关闭SMTP连接

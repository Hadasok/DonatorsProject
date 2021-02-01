import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Mailer:
    __mail_server_address = 'smtp.gmail.com'
    __mail_server_port = 465

    __mail_address = 'hadasok@gmail.com'
    __mail_password = 'O30091980o'

    __mail_connection = None

    def __get_instance():
        if Mailer.__mail_connection:
            return Mailer.__mail_connection
        else:
            Mailer.__mail_connection = Mailer.__initialize_mail_server()
            return Mailer.__mail_connection

    def __initialize_mail_server():
        connection = smtplib.SMTP_SSL(
            Mailer.__mail_server_address,
            Mailer.__mail_server_port,
            context=ssl.create_default_context()
        )

        connection.login(Mailer.__mail_address, Mailer.__mail_password)

        return connection

    def send_mail(recipient, subject, content):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = Mailer.__mail_address
        msg['To'] = recipient
        mail_message = (
            '<html><body><div dir="rtl">{}</div></body></html>'
        ).format(content)
        msg.attach(MIMEText(mail_message, 'html'))

        Mailer.__get_instance().sendmail(Mailer.__mail_address, recipient, msg.as_string())

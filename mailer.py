import smtplib
import ssl


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
        mail_message = (
            'From: {}\n' +
            'To: {}\n' +
            'Subject: {}\n\n' +
            '<html><body><div dir="rtl">{}</div></body></html>'
        ).format(Mailer.__mail_address, recipient, subject, content).encode('utf8')

        Mailer.__get_instance().sendmail(Mailer.__mail_address, recipient, mail_message)

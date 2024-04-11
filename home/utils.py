'''from django.core.mail import send_mail
import smtplib
def send_email_client():
    server= smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("sinhahishere4@gmail.com","dkkhs12345")
    message="This Is a Verification Mail"
    subject="Verifiacation Mail"
    server.sendmail("sinhaishere4@gmail.com","ash8959749452@gmail.com",subject,message)
    server.quit()'''
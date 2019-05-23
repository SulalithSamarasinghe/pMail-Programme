#pMail is a programme that can send e-mails
#
import smtplib
#
print('***************************')
print('*          pMail          *')
print('***************************')
print('')
print('')
print('+++  Sign in  +++')
print('')
emailAddress = input('E-mail address ==> ')
password = input('Password       ==> ')
print('')
receiverEMail = input('Receiver E-mail address ==> ')
subject = input('Subject of the mail ==> ')
message = input('Message to sent     ==> ')
print('')
#
def sendMail(emailAddress,receiverEMail,password,subject,message):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(emailAddress,password)
        message = 'Subject: {}\n\n{}'.format(subject,message)
        server.sendmail(emailAddress,receiverEMail,message)
        server.quit()
        print("e-mail sent succsessfully!!!")
    except:
        print("Problem detected!!!")
        print("")
        print("   + Pleace check your e-mail has enabled less secure apps. If not pleace enable.")
        print("   + Check the internet connection")
        print("   + Check whether you have given the correct e-mail address and password.")
#
sendMail(emailAddress,receiverEMail,password,subject,message)

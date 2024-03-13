import smtplib
from email.mime.text import MIMEText


def sendMail(msg):


    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login("itsishu0505@gmail.com", "xjee crny ubkq icne")
    # message to be sent
    message = "this is a test message for smtp python"
    # sending the mail
    s.sendmail("itsishu0505@gmail.com", "iparmar0505@gmail.com", msg)

    # terminating the session
    s.quit()
    print('sucess', msg)  # Press Ctrl+F8 to toggle the breakpoint.

def curateMail(bdayArr):

    bdayNames = ""
    bdayMsg = ""
    for bday in bdayArr:
        bdayNames += (bday["Nick name"]) + " "
        bdayMsg += f'Happy Birthday {bday["Nick name"]} from Ishu and Riyu \n'

    msg = MIMEText(bdayMsg)

    msg['Subject'] = bdayNames + "Birthday"


    # msg['From'] = 'admin@example.com'
    # msg['To'] = 'info@example.com'
    print(msg.as_string())
    return (msg.as_string())


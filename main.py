from mail import *
from traverseBdaycsv import *







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    todayBirthday = getTodayBday()
    msg = curateMail(todayBirthday)
    if(msg):
        print('here is msg')
        sendMail(msg)
        print(('mail sent'))
    else:
        print('no msg')




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

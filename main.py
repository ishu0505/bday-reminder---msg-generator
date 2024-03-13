from mail import *
from traverseBdaycsv import *







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    todayBirthday = getTodayBday()
    msg = curateMail(todayBirthday)
    sendMail(msg)
    print(('mail sent'))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

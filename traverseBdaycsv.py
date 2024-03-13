from csv import DictReader
import datetime


def tess():
    print('hey')
def importCSV():
    # open file in read mode
    with open("Birthdays.csv", 'r') as file:
        dict_reader = DictReader(file)

        bdays = list(dict_reader)

        print(bdays)
        return bdays
def getTodayBday():
    bdaysArr = importCSV() # using import csv function to get array of objects contaning bdays
    todayDate = datetime.date.today().strftime("%d/%m")
    todayBdays = []
    for bday in bdaysArr:
        # print(bday["Date"])
        if(bday["Date"] == todayDate):
            todayBdays.append(bday)


    print(todayBdays)
    return todayBdays # returns an array containing all the bdays that are today




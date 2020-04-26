import datetime
from datetime import date
from collections import defaultdict
import dateutil.relativedelta
import calendar
import sqlite3
from database import *
import json

class Transact:
    def __init__(self, date, amount, description):
        self.date = date
        self.amount = amount
        self.description = description

class TransactionList:
    def __init__(self):
        self.List = []
        
    def add_transaction(self, date, amount, description):
        self.List.append(Transact(date, amount, description))
           
    def transacPie(self, cat_list):
        categories = ["Housing", "Food", "Phone", "Entertainment", "Travel", "Car", "Other", "Health"]
        money = {}
        for category in categories:
            money[category] = 0
                
        for x in cat_list:
            check = False
            for category in categories:
                if category == x.description:
                    check = True
                    money[category] += abs(x.amount)
                    money[category] = round(money[category], 2)
            if check is False:
                money['Other'] += abs(x.amount)
                money['Other'] = round(money['Other'], 2)    
        
        money2 = [ v for v in money.values() ]
            
        with open('static/money.js', 'w') as out_file:
            out_file.write('var data_transac = %s;\n' % json.dumps(money2))

    def categoryPie(self, catList):
            dict1 = []
            list1 = []
            num = 0;
            for cat in catList:
                dict1 = [cat.date, cat.amount, cat.description] 
                dict2 = dict1.copy()  
                list1.append(dict2) 
                num = num + 1
            Housing = []
            Housing2 = 0
            Food = []
            Food2 = 0
            Phone = []
            Phone2 = 0
            Entertainment = []
            Entertainment2 = 0
            Travel = []
            Travel2 = 0
            Car = []
            Car2 = 0
            Other = []
            Other2 = 0
            Health = []
            Health2 = 0
            for x in list1:
                if (x[2] == "Housing"):
                    copy = x.copy()
                    Housing.append(copy)
                    Housing2 = Housing2 +1
                elif (x[2] == "Food"):
                    copy = x.copy()
                    Food.append(copy)
                    Food2 = Food2 + 1
                elif (x[2] == "Phone"):
                    copy = x.copy()
                    Phone.append(copy)
                    Phone2 = Phone2 + 1
                elif (x[2] == "Entertainment"):
                    copy = x.copy()
                    Entertainment.append(copy)
                    Entertainment2 = Entertainment2 + 1
                elif (x[2] == "Travel"):
                    copy = x.copy()
                    Travel.append(copy)
                    Travel2 = Travel2 + 1 
                elif (x[2] == "Car"):
                    copy = x.copy()
                    Car.append(copy)
                    Car2 = Car2 + 1 
                elif (x[2] == "Health"):
                    copy = x.copy()
                    Health.append(copy)
                    Health2 = Health2 + 1
                elif (x[2] == "Other"):
                    copy = x.copy()
                    Other.append(copy)
                    Other2 = Other2 +1
                                   
            with open('static/categoryPie.js', 'w') as out_file:
                out_file.write('var Num = %s;\n' % json.dumps(num))
                out_file.write('var Housing = %s;\n' % json.dumps(Housing))
                out_file.write('var Housing2 = %s;\n' % json.dumps(Housing2))
                out_file.write('var Food = %s;\n' % json.dumps(Food))
                out_file.write('var Food2 = %s;\n' % json.dumps(Food2))
                out_file.write('var Phone = %s;\n' % json.dumps(Phone))
                out_file.write('var Phone2 = %s;\n' % json.dumps(Phone2))
                out_file.write('var Entertainment = %s;\n' % json.dumps(Entertainment))
                out_file.write('var Entertainment2 = %s;\n' % json.dumps(Entertainment2))
                out_file.write('var Travel = %s;\n' % json.dumps(Travel))
                out_file.write('var Travel2 = %s;\n' % json.dumps(Travel2))
                out_file.write('var Car = %s;\n' % json.dumps(Car))
                out_file.write('var Car2 = %s;\n' % json.dumps(Car2))
                out_file.write('var Health = %s;\n' % json.dumps(Health))
                out_file.write('var Health2 = %s;\n' % json.dumps(Health2))
                out_file.write('var Other = %s;\n' % json.dumps(Other))
                out_file.write('var Other2 = %s;\n' % json.dumps(Other2))
                                     
    def findhistory(self):
        filename = 'data.txt'
        out = open(filename, 'r')
        string1 = out.readline().strip("\n")
        string2 = out.readline().strip("\n")
        date_object = datetime.datetime.strptime(string1, '%d/%m/%Y').date()
        date_object1 = datetime.datetime.strptime(string2, '%d/%m/%Y').date()

        newList=[]
        for x in self.List:
            string3 = x.date
            date_object2 = datetime.datetime.strptime(string3, '%Y-%m-%d').date()

            if date_object2 < date_object1:
                if date_object2 > date_object:
                    newList.append(x)
        count = len(newList)
        for i in range(count):
            for j in range(0,count-i-1):
                if newList[j].date < newList[j+1].date:
                    newList[j],newList[j+1] = newList[j+1],newList[j]

        self.transacPie(newList)
        self.categoryPie(newList)
        return newList

    def allHistory(self):
        cat_list = self.List
        self.transacPie(cat_list)
        self.categoryPie(cat_list)
        return self.List        

    def monthlyExpenditureData(self):
        mainList = []
        today = date.today()
        today = today.replace(day=1)
        d2 = today - dateutil.relativedelta.relativedelta(months=12)

        for x in self.List:
            date_object = datetime.datetime.strptime(x.date, '%Y-%m-%d').date()
            if d2 < date_object:
                if x.amount < 0:
                    list1 = []                   
                    list1.append(date_object)
                    list1.append(x.amount)
                    mainList.append(list1)
                    
        d = defaultdict(int)
        for x, val in mainList:
            d[x.strftime('%Y-%m')] += val
            d[x.strftime('%Y-%m')] = round(d[x.strftime('%Y-%m')], 2)    
        monthlyExp = list(map(list, d.items()))
                
        mE = []
        for x, y in monthlyExp:
            mE.append(abs(y))

        monthNames = self.monthLabels()            
            
        with open('static/data_me.js', 'w') as out_file:
            out_file.write('var data_exp = %s;\n' % json.dumps(mE))
            out_file.write('var months_mE = %s;\n' % json.dumps(monthNames))
            
    def accountBalData(self):
        mainList = []
        today = date.today()
        today = today.replace(day=1)
        d2 = today - dateutil.relativedelta.relativedelta(months=12)

        for x in self.List:
            date_object = datetime.datetime.strptime(x.date, '%Y-%m-%d').date()
            if d2 < date_object:
                list1 = []                   
                list1.append(date_object)
                list1.append(x.amount)
                mainList.append(list1)
                    
        d = defaultdict(int)
        for x, val in mainList:
            d[x.strftime('%Y-%m')] += val
            d[x.strftime('%Y-%m')] = round(d[x.strftime('%Y-%m')], 2)    
        monthlyExp = list(map(list, d.items()))
                
        aB1 = []
        for x, y in monthlyExp:
            aB1.append(y)
        aB = []
        num = 0
        for i in aB1:
            num += i
            aB.append(num)
                    
        monthNames = self.monthLabels()

        with open('static/data_aB.js', 'w') as out_file:
            out_file.write('var data_aB = %s;\n' % json.dumps(aB))
            out_file.write('var months_aB = %s;\n' % json.dumps(monthNames))  
                  
    def monthLabels(self):
        months = []
        currentMonth = datetime.datetime.now().month
        currentMonth = int(currentMonth)
        while currentMonth in range(13):
            months.append(calendar.month_abbr[currentMonth])
            currentMonth+=1
        i = 1
        while len(months) != 13:
            months.append(calendar.month_abbr[i])
            i+= 1
        return months
    def newCat(self):
        categories = ["Housing", "Food", "Phone", "Entertainment", "Travel", "Car", "Other", "Health"]
        today = date.today()
        d2 = today - dateutil.relativedelta.relativedelta(months=12)

        money = {}
        for category in categories:
            money[category] = 0
                
        for x in self.List:
            date_object = datetime.datetime.strptime(x.date, '%Y-%m-%d').date()
            if d2 < date_object:
                check = False
                for category in categories:
                    if category == x.description:
                        check = True
                        money[category] += abs(x.amount)
                        money[category] = round(money[category], 2)
                    if check is False:
                        money['Other'] += abs(x.amount)
                        money['Other'] = round(money['Other'], 2)    
        
        return money                      


class ReminderList:
    def __init__(self):
        self.List = []
    def add_reminder(self, date1, amount, description):
        error = None
        today = date.today()
        date_object = datetime.datetime.strptime(date1, '%m/%d/%Y').date()
        check = True
        for x in self.List:
            if x[0] == date1 and x[0] == amount and x[0] == description:
                check = False
                error = "Reminder already exists"
                break
        if today <= date_object and check is True:
            con = create_connection()
            with con:
                values = (date1, amount, description)
                insert_rem(con, values)
                self.List = list_of_rem(con)

        elif date_object < today:
            error = "Date invalid"
            
        return error
            
    def removeReminder(self, date, amount, description):
        con = create_connection()
        with con:
            values = (date, amount, description)
            removeReminder(con, values)
            
    def allReminders(self):
        con = create_connection()
        with con:
            self.List = list_of_rem(con)    
            return self.List


    
   

payment_reminders = ReminderList()

transaction_history = TransactionList()

from flask import Flask, render_template, redirect, url_for, request
from backend import *
import requests
from datetime import datetime
import sqlite3
from database import *
import names
app = Flask(__name__)

filename = 'data.txt'


@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/Login', methods=['GET', 'POST'])
def login():
    return redirect(
        "https://sandbox.api.macquariebank.io/connect/v1/user-interface/login?client_id=z8rTxN9UcRbzabplD5FR0GGrPtyBa3dy")


@app.route('/Transaction_history')
def profile():

    if names.checking == 0:
        k = request.url
        num = len(k)
        counter = 0
        start = 0
        finish = 0
        check = 0
        while (counter < num):
            if (k[counter] == '=' and check == 0):
                start = counter
                check = 1

            if (k[counter] == '&'):
                finish = counter

            counter = counter + 1
        token1 = k[start + 1:finish]
        print(token1)
        headers = {'client_id': 'z8rTxN9UcRbzabplD5FR0GGrPtyBa3dy', 'client_secret': '4x3aGo5MBn3W9LyL',
                   'content-type': 'application/x-www-form-urlencoded'}
        payload = {'grant_type': 'authorization_code', 'code': token1}
        r = requests.post("https://sandbox.api.macquariebank.io/connect/v1/oauth2/token", headers=headers,
                          params=payload)
        print(r.text)
        r = r.json()
        access_token = r['access_token']
        refresh_token = r['refresh_token']
        header2 = {'authorization': 'Bearer ' + access_token, 'client_id': 'z8rTxN9UcRbzabplD5FR0GGrPtyBa3dy'}

        r1 = requests.get("https://sandbox.api.macquariebank.io/connect/v1/accounts", headers=header2)
        print(r1.text)
        r1 = r1.json()
        print(r1)
        p = r1['accounts']
        for x in p:
            if (x['account_status'] == 'Active'):
                names.account_id = x['account_id']
                names.account_name = x['account_nickname']
                names.account_number = x['account_number']

        r2 = requests.get("https://sandbox.api.macquariebank.io/connect/v1/accounts/" + names.account_id + "/balances",
                          headers=header2)
        print(r2.text)
        r2 = r2.json()
        listy = r2['balances']
        names.avail_funds = listy[0]["uncleared_funds"]
        names.bal = listy[0]["balance"]
        names.lim = listy[0]["limit"]
        r3 = requests.get("https://sandbox.api.macquariebank.io/connect/v1/accounts/" + names.account_id + "/transactions",
                          headers=header2)

        r3 = r3.json()
        list = r3['transactions']
        Descriptions = ["Food", "Phone", "Entertainment", "Travel", "Car", "Health", "Other"]
        from random import seed
        from random import randint
        seed(1)
        for x in list:
            if (int(x['amount']) > 100):
                x['description'] = "Housing"
            else:
                x['description'] = Descriptions[randint(0, 6)]

            print(x)
        print(list)
        names.checking = 1
        for x in list:
            transaction_history.add_transaction(x['transaction_date'], -1*int(x['amount']), x['description'])
        '''
        for x in transaction_history.List:
            
            print(x.date+"    " + str(x.amount) + "   " + x.description)
            print('\n')
        '''
    transaction_history.monthlyExpenditureData()
    transaction_history.accountBalData()
    return render_template('Transaction_history.html', lim=names.lim,account_id=names.account_id,account_name=names.account_name,account_number=names.account_number,bal=names.bal,avail_funds=names.avail_funds)


@app.route('/Expenditure', methods=['GET','POST'])
def expenditure():
    error = None
    if request.method == 'POST':
        date = request.form['date']
        date1 = request.form['date1']
        out = open(filename, 'w')
        out.write(date + '\n')
        out.write(date1 + '\n')
        out.close()
        categories = transaction_history.newCat()
        trans_list = transaction_history.findhistory()

        return render_template('Expenditure.html', trans_list=trans_list, categories = categories)
    
    else:
        trans_list = transaction_history.allHistory() 
        categories = transaction_history.newCat()       
        return render_template('Expenditure.html', trans_list=trans_list, categories = categories)





@app.route('/Offers')
def offers():
    return render_template('Offers.html')


@app.route('/Payment_reminders', methods=['GET', 'POST', 'DELETE'])
def reminder():
    error = None
    remin_list = payment_reminders.allReminders()     
    if request.method == 'POST':
        date = request.form['date']
        amount = request.form['amount']
        amount = float(amount) * -1
        description = request.form['description']
        new = date
        new2 = 0
        error = payment_reminders.add_reminder(date, amount, description)
        remin_list = payment_reminders.allReminders()
        return render_template('Payment_reminders.html', remin_list=remin_list,new=new, new2=0, error = error)
    elif request.method == 'DELETE':
        date = request.form['d1']
        amount = request.form['a1']
        description = request.form['d2']
        payment_reminders.removeReminder(date, amount, description)
        remin_list = payment_reminders.allReminders()
        return render_template('Payment_reminders.html', remin_list=remin_list, new='000000000', new2=1, error = error)
    else:        
        return render_template('Payment_reminders.html', remin_list=remin_list, new='000000000', new2=0, error = error)
    


    


@app.route('/Projections')
def projections():
    return render_template('Projections.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port = 8000, debug=True)

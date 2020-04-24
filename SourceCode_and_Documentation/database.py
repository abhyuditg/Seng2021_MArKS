import sqlite3
from sqlite3 import Error

def create_connection():
    con = None
    try:
        con = sqlite3.connect('reminders.db')
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS reminders(date VARCHAR NOT NULL, amount VARCHAR NOT NULL, description VARCHAR)')
        con.commit()
        return con
    except Error as e:
        print(e)
    
    return con

def insert_rem(con, values):
    sql = '''INSERT INTO reminders(date,amount,description) VALUES(?, ?, ?)'''
    cur = con.cursor()
    cur.execute(sql, values) 
    con.commit()

def list_of_rem(con):
    cur = con.cursor()
    cur.execute('SELECT * from reminders')
    List = list(cur.fetchall())
    return List

def removeReminder(con, values):
    cur = con.cursor()
    cur.execute('DELETE FROM reminders where date = ? and amount = ? and description = ?', (values))
    con.commit()




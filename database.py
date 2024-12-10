# Database Managment File

import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    password="system",
    database="bank"
)

cursor = mydb.cursor()


def db_query(str):
    cursor.execute(str)
    result = cursor.fetchall()
    return result


def create_customer_table():
    cursor.execute('''
    Create table IF NOT EXISTS customers 
                (username varchar(20) not null,
                password varchar(20) not null,
                name varchar(20) not null,
                age integer not null,
                city varchar(20) not null,
                balance integer not null,
                account_number integer not null,
                status boolean not null)
                ''')


mydb.commit()

if __name__ == '__main__':
    create_customer_table()

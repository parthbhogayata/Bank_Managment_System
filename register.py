# User Registration SignIn SignUp
from database import *
import random
from customer import *
from bank import Bank


def signup():
    username = input('Enter Your Username : ')
    temp = db_query(
        f"select username from customers where username = '{username}'")
    if temp:
        print('Username is Already Exists')
        signup()
    else:
        print('Username is Available please Procedd')
        password = input('\n Enter Your Password : ')
        name = input('Enter Your Name : ')
        age = int(input('Enter Your Age : '))
        city = input('Enter Your City :')
        status = 1
        while True:
            account_number = random.randint(10000000, 99999999)
            temp = db_query(
                f"select account_number from customers where account_number = '{account_number}'")
            if temp:
                continue
            else:
                print('Your Account Number : ', account_number)
                break

    cobj = Customer(username, password, name, age,
                    city, account_number, status)
    cobj.create_user()
    bonj = Bank(username, account_number)
    bonj.create_transaction_table()


def signin():
    username = input('Enter Usename : ')
    temp = db_query(
        f"select username from customers where username = '{username}'")
    if temp:
        while True:
            password = input('Enter Your Password : ')
            temp = db_query(
                f"select password from customers where username ='{username}'")
            if temp[0][0] == password:
                print('| | | | | | | | | | Sign In Sucessfully | | | | | | | | | |')
                return username
            else:
                print('ERROR : Wrong Password Try again')
                continue

    else:
        print('ERROR : Username Does Not Exists...')
        signin()

# Bank Services
from database import *
import datetime as dt


class Bank:

    def __init__(self, username, account_number):
        self.__username = username
        self.__account_number = account_number

    def create_transaction_table(self):
        db_query(
            f"create table IF NOT EXISTS {self.__username}_transaction (timedate varchar(30),account_number integer,remarks varchar(30),amount integer)")

    def current_balance(self):
        temp = db_query(
            f"select balance from customers where username = '{self.__username}'")
        return int(temp[0][0])

    def balance_enquiry(self):
        balance = self.current_balance()
        print(f"{self.__username} Your Balance is : Rs.{balance}")

    def deposit(self, amount):
        balance = self.current_balance()
        balance += amount
        temp = db_query(
            f"update customers set balance = '{balance}' where username = '{self.__username}'")
        print('\n')
        self.balance_enquiry()
        db_query(
            f"insert into {self.__username}_transaction values ('{dt.datetime.now()}','{self.__account_number}','(+) Deposit','{amount}')")
        mydb.commit()

    def withdraw(self, amount):
        balance = self.current_balance()
        balance -= amount
        temp = db_query(
            f"update customers set balance = '{balance}' where username = '{self.__username}'")
        print('\n')
        self.balance_enquiry()
        db_query(
            f"insert into {self.__username}_transaction values ('{dt.datetime.now()}','{self.__account_number}','(-) Withdraw','{amount}')")
        mydb.commit()

    def fund_transfer(self, sender_acc_no, amount):
        balance = self.current_balance()
        sender_bal = db_query(
            f"select balance,username from customers where account_number = '{sender_acc_no}'")
        balance -= amount
        sbal = sender_bal[0][0]
        sbal += amount
        db_query(
            f"update customers set balance = '{balance}' where username = '{self.__username}'")
        db_query(
            f"update customers set balance = '{sbal}' where account_number = '{sender_acc_no}'")
        print('\n')
        self.balance_enquiry()
        db_query(
            f"insert into {self.__username}_transaction values ('{dt.datetime.now()}','{self.__account_number}','(-) Transfer to {sender_acc_no}','{amount}')")
        uname = sender_bal[0][1]
        db_query(
            f"insert into {uname}_transaction values ('{dt.datetime.now()}','{self.__account_number}','(+) Transfer from {self.__account_number}','{amount}')")
        mydb.commit()

#Customer Details 
from database import *;
class Customer:
    def __init__(self,username,password,name,age,city,account_number,status):
        self.__username = username
        self.__password = password
        self.__name = name
        self.__age = age
        self.__city = city
        self.__account_number = account_number
        self.__status = status

    def create_user(self):
        db_query(f"insert into customers values ('{self.__username}','{self.__password}','{self.__name}','{self.__age}','{self.__city}',0,'{self.__account_number}','{self.__status}')")
        mydb.commit()
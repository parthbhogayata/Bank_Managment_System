from register import *
from bank import *
print('* * * * * * * * * * Welcome to Banking System * * * * * * * * * * ')
status = False
while True:
    try:
        register = int(input('1.Sign Up \n'
                             '2.Sign In \n :->  '))
        if register == 1 or register == 2:
            if register == 1:
                signup()
            if register == 2:
                user = signin()
                status = True
                break
        else:
            print('Please Enter Valid Input From Opions')

    except ValueError:
        print('Invalid Input Try Again with Numbers...')

account_number = db_query(
    f"select account_number from customers where username = '{user}';")
bobj = Bank(user, account_number[0][0])
while status:
    try:
        print('- - - - - - - - - - Which Facility you want to use - - - - - - - - - -')
        facility = int(input('\n1.Balance Enquiry \n'
                             '2.Cash Deposit \n'
                             '3.Cash Withdraw \n'
                             '4.Fund Transfer \n'
                             ':-'))
        if facility >= 1 and facility <= 4:
            if facility == 1:
                print('\n')
                bobj.balance_enquiry()
                print('\n')

            elif facility == 2:
                amount = int(input('Enter Amount You Want to deposit : Rs.'))
                bobj.deposit(amount)

            elif facility == 3:
                amount = int(input('Enter Amount you want to Withdraw : Rs.'))
                bal = bobj.current_balance()
                if amount < bal:
                    bobj.withdraw(amount)
                else:
                    print('\n You do not have suficient balance for withdraval...')

            elif facility == 4:
                amount = int(input('Enter Amount You want to Transfer : Rs.'))
                bal = bobj.current_balance()
                if amount < bal:
                    sender_acc_no = int(input('Enter Senders Account no : '))
                    temp = db_query(
                        f"select account_number from customers where account_number = '{sender_acc_no}'")

                    if temp[0][0] == sender_acc_no:
                        if temp[0][0] != account_number[0][0]:
                            bobj.fund_transfer(sender_acc_no, amount)
                        else:
                            print("ERROR : Same Account fund Transfer is not Valid")
                    else:
                        print(
                            "ERROR : This account does not exists. please varify Account no.")
                else:
                    print('\n You do not have suficient balance for Transfer...')

        else:
            print('ERROR : Please Enter Valid Input From Given Options')
    except ValueError:
        print('ERROR : Invalid Input Please Try With Given Numbers ')

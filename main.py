""" Main program """
import os
import sys
import time

from colorama import Fore
from colorama import init

from optionpanel import main_option_panel, log_in_panel, log_in_verification
from optionpanel import home_user_panel, display_account_balance
from optionpanel import display_deposit_panel, display_withdraw_panel
from operations import view_customer_transactions, process_all_transactions
from workfile import create_database, get_database_info, save_database_info

init()

# Global Variables
database_data = ''


def begin():
    """ Start the program with the user interface """
    option_list = ['0', '1', '2', '3']
    option_number = '99'
    while option_number not in option_list:
        option_number = main_option_panel(option_list)

    main_option_selection(option_number)


def create_new_user():
    """ Will create a new user """
    os.system('cls')
    print(" New User creation")
    print("-----------------------------")
    print()
    print(Fore.YELLOW + ' Full name include name and last name -' + Fore.RESET)
    name = ""
    while name == "":
        name = input(" Full Name: ")
        if name == "":
            print(Fore.YELLOW + ' Please enter a name -' + Fore.RESET)

    pin_number = ''
    acceptable_range = range(0, 10000)
    in_range = False

    print()
    print(Fore.YELLOW + ' Pin Number should be 4 digit long -' + Fore.RESET)
    while (not pin_number.isdigit() or not in_range or len(pin_number) < 4):
        pin_number = input(" Enter pin number from 0000 to 9999: ")
        if pin_number.isdigit():
            if int(pin_number) in acceptable_range:
                in_range = True
            else:
                in_range = False
        else:
            pass

    os.system('cls')
    print(" New User will be: ")
    print("-----------------------------")
    print("New Customer name: " + name)
    print("The Pin Number for customer " + name + " is: " + pin_number)
    # print('Is this correct? Y/N')

    print()
    print(Fore.YELLOW + ' Type Y or y for accept the new customer -' + Fore.RESET)
    print(Fore.YELLOW + ' Type N or n to try again -' + Fore.RESET)
    print(Fore.YELLOW + ' Type C or c to Cancel -' + Fore.RESET)

    affirmation = ['Y', 'N', 'C', 'y', 'n', 'c']
    selected = ""
    while selected not in affirmation:
        selected = input(" Is the information correct? Y/N: ")

    if selected == 'c' or selected == 'C':
        print('Canceled')
        begin()
    elif selected == 'y' or selected == 'Y':
        creating_user(name, pin_number)
        begin()
    else:
        print('REJECTED')
        create_new_user()


def define_next_account_number():
    """ Define Next Account Number for new customer """
    number = 0
    data_lines = database_data.splitlines()
    for data_line in data_lines:
        line_parts = data_line.split('\t')
        if int(line_parts[2]) > number:
            number = int(line_parts[2])

    # increment the account number then apply 5 digits format
    number = number + 1
    next_account_number = str(number).zfill(5)

    return next_account_number


def define_next_transaction_id():
    """ Define Next Transaction ID for the record """
    number = 0
    data_lines = database_data.splitlines()

    for data_line in data_lines:
        line_parts = data_line.split('\t')
        if (int(line_parts[0]) > number):
            number = int(line_parts[0])

    # increment the transaction number then apply 6 digits format
    number = number + 1
    transaction_number = str(number).zfill(6)

    return transaction_number


def reset_database_use():
    """ Reset the use of the data from the database """
    global database_data
    database_data = get_database_info()


create_database()
reset_database_use()


def creating_user(name, pin):
    """ Creating a user """
    print('Creating . . . .')
    transaction_id = define_next_transaction_id()
    account_number = define_next_account_number()
    line = transaction_id + '\t' + name + '\t' + account_number + \
        '\t' + str(pin) + '\t' + 'c' + '\t' + '0.00' + '\n'

    save_database_info(line)
    reset_database_use()
    time.sleep(1.5)
    print('Created!')
    print('----------------------------------------------------------------')
    print(' Transaction Id: ' + transaction_id)
    print('      Full Name: ' + name)
    print(' Account Number: ' + account_number)
    print('     Pin Number: ' + str(pin))
    print('----------------------------------------------------------------')
    time.sleep(2.5)


def home_option_selection(user_choice, active_user, continue_loop):
    """ Home Panel Options """
    if user_choice == '1':
        print('Loading Balance ...')
        time.sleep(1)
        display_account_balance(active_user, database_data)
        continue_loop = False
        return continue_loop

    if user_choice == '2':
        deposit_info = display_deposit_panel(active_user)
        to_currency = f"${float(deposit_info[0]):,.2f}"
        print(f'Amount for deposit is: {to_currency}')

        time.sleep(3)
        transaction_id = define_next_transaction_id()
        line = transaction_id + '\t' + active_user.fullname + '\t' + active_user.account_number + \
            '\t' + active_user.pin_number + '\t' + \
            'd' + '\t' + deposit_info[0] + '\n'
        save_database_info(line)
        reset_database_use()
        transaction_id = define_next_transaction_id()
        new_balance = f'{(float(deposit_info[0]) + float(active_user.balance)):.2f}'
        line = transaction_id + '\t' + active_user.fullname + '\t' + active_user.account_number + \
            '\t' + active_user.pin_number + '\t' + \
            'b' + '\t' + str(new_balance) + '\n'
        save_database_info(line)
        reset_database_use()
        active_user.balance = new_balance
        print('Deposit Completed.')
        time.sleep(2.5)
        continue_loop = False
        return continue_loop

    if user_choice == '3':
        withdraw_info = display_withdraw_panel(active_user)
        to_currency = f"${float(withdraw_info[0]):,.2f}"
        print(f'Amount for withdraw is: {to_currency}')
        time.sleep(3)
        transaction_id = define_next_transaction_id()
        line = transaction_id + '\t' + active_user.fullname + '\t' + active_user.account_number + \
            '\t' + active_user.pin_number + '\t' + \
            'w' + '\t' + withdraw_info[0] + '\n'
        save_database_info(line)
        reset_database_use()
        transaction_id = define_next_transaction_id()
        new_balance = f'{(float(active_user.balance) - float(withdraw_info[0])):.2f}'
        line = transaction_id + '\t' + active_user.fullname + '\t' + active_user.account_number + \
            '\t' + active_user.pin_number + '\t' + \
            'b' + '\t' + str(new_balance) + '\n'
        save_database_info(line)
        reset_database_use()
        active_user.balance = new_balance
        print('Withdraw Completed.')
        time.sleep(2.5)
        continue_loop = False
        return continue_loop

    if user_choice == '4':
        print('Transactions')
        view_customer_transactions(
            active_user.account_number, active_user.pin_number, database_data, active_user.fullname)
        time.sleep(1)
        continue_loop = False
        return continue_loop

    if user_choice in ['C', 'c']:
        print("Canceled *")
        time.sleep(1)
        begin()


def main_option_selection(option):
    """ Guide the user main options """
    if option == '0':
        os.system('cls')
        print('  FAKEBANK ->')
        print("-----------------------------")
        print(" Thank you for visit us!")
        print("-----------------------------")
        print(' Jose Figueroa / 2025')
        sys.exit(0)

    if option == '1':
        active_user_confirmation = ''
        loop = True
        while loop:
            result = log_in_panel()
            active_user_confirmation = log_in_verification(
                result[0], result[1], database_data)
            if active_user_confirmation[0]:
                print(
                    '---------------------------------------------------------------------------------')
                print('--- Log In Successful ----------')
                print(
                    '---------------------------------------------------------------------------------')
                print(active_user_confirmation[1].fullname)
                print(active_user_confirmation[1].account_number)
                print(active_user_confirmation[1].pin_number)
                print(active_user_confirmation[1].balance)
                print(
                    '---------------------------------------------------------------------------------')
                time.sleep(2)
                options_list = ['1', '2', '3', '4', 'C', 'c']
                inner_loop = True
                while inner_loop:
                    choice = home_user_panel(
                        active_user_confirmation[1], options_list)
                    if choice == 99:
                        inner_loop = True
                    elif choice in options_list:
                        if choice in ['C', 'c']:
                            break

                        else:
                            inner_loop2 = True
                            while inner_loop2:
                                continue_loop = home_option_selection(
                                    choice, active_user_confirmation[1], inner_loop2)
                                inner_loop2 = continue_loop
                    else:
                        pass

                begin()

            else:
                print()
                print(
                    '---------------------------------------------------------------------------------')
                print('---- Log In Fail ---------------')
                print(
                    '---------------------------------------------------------------------------------')
                print()
                inner_loop = True
                while inner_loop:
                    print()
                    print('[ ' + Fore.GREEN + "R or r" +
                          Fore.RESET + ' ] for Re-Try   ' + '[ ' + Fore.GREEN + "C or c" +
                          Fore.RESET + ' ] for Cancel')
                    print()
                    choice = input(' Option: ')
                    if choice in ['R', 'r']:
                        loop = True
                        break

                    if choice in ['C', 'c']:
                        loop = False
                        break
        begin()

    if option == '2':
        create_new_user()

    if option == '3':
        process_all_transactions(database_data)
        begin()


begin()

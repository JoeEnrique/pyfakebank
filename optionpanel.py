"""Module providing all options panels interactions."""
import os
import time

from objectclasslist import ActiveCustomer
from colorama import Fore
from colorama import init
init()


# MAIN PANEL
def main_option_panel(option_list):
    """ Display the main option panel """
    os.system('cls')
    print(" Welcome to FakeBank !!")
    print()
    print(" Please select an option number >")
    print("-------------------------------- ---")

    print(" [ " + Fore.GREEN + '1' + Fore.RESET + " ] " + 'Log-In into System')
    print(" [ " + Fore.GREEN + '2' + Fore.RESET + " ] " + 'Create New User')
    print(" [ " + Fore.GREEN + '3' + Fore.RESET + " ] " +
          'Show all Transactions')
    print()
    print(" [ " + Fore.GREEN + '0' + Fore.RESET + " ] Exit")
    print()

    loop = True
    counter = -1
    while loop:
        counter += 1
        choice = input(' Option: ')
        if choice not in option_list:
            if counter == 3:
                choice = 99
                loop = False
            print(Fore.YELLOW + ' Please enter a number between 0 and 3 -' + Fore.RESET)
        else:
            loop = False

    return choice


def customer_options_panel(name):
    """ Display the options available for the customer after Log-In """
    options_list = ['1', '2', '3', '4', 'C', 'c']
    print(f" Welcome back {name}")
    print()
    print(" Please select an Transaction Option number >")
    print("-------------------------------------------- ---")

    print(" [ " + Fore.GREEN + '1' + Fore.RESET + " ] " + 'View Balance')
    print(" [ " + Fore.GREEN + '2' + Fore.RESET + " ] " + 'Make a Deposit')
    print(" [ " + Fore.GREEN + '3' + Fore.RESET + " ] " + 'Make a Withdraw')
    print(" [ " + Fore.GREEN + '4' + Fore.RESET + " ] " +
          'View all Your transactions')
    print()
    print(" [ " + Fore.GREEN + 'C or c' + Fore.RESET + " ] to Cancel")
    print()

    selected = ''
    counter = -1
    while selected not in options_list:
        counter += 1
        if counter == 4:
            selected = ''
        else:
            selected = input(' Option: ')

    return selected


def log_in_verification(account, pin, database_data):
    """ Confirmation the customer is legit """
    confirmation = False
    data_lines = database_data.splitlines()
    results = []
    active_user_info = []
    for data_line in data_lines:
        line_parts = data_line.split('\t')
        if (line_parts[2] == account and line_parts[3] == pin):
            confirmation = True
            results = []
            active_user_info = []
            active_user_info.append(line_parts[1])
            active_user_info.append(line_parts[2])
            active_user_info.append(line_parts[3])
            active_user_info.append(line_parts[5])

    if confirmation:
        active_user = ActiveCustomer(
            active_user_info[0], active_user_info[1], active_user_info[2], active_user_info[3])
        results.append(confirmation)
        results.append(active_user)
    else:
        results.append(confirmation)
        results.append('No Data')

    return results


def log_in_panel():
    """ Log In panel options """
    os.system('cls')
    print(Fore.GREEN + ' Log-in **' + Fore.RESET)
    print('----------------------------------------------')

    not_valid_account_number = True
    not_valid_pin_number = True
    acc_number = ''
    pin_number = ''

    while not_valid_account_number:
        acc_number = input(' Please enter your Account Number: ')
        if len(acc_number) != 5:
            print(Fore.YELLOW + " Please enter a 5 digits number ----- " + Fore.RESET)
            print()
        if not acc_number.isdigit():
            print(Fore.YELLOW + " Please enter a only numbers ----- " + Fore.RESET)
            print()
        if (len(acc_number) == 5 and acc_number.isdigit()):
            not_valid_account_number = False

    while not_valid_pin_number:
        pin_number = input(' Enter your PIN number: ')
        if len(pin_number) != 4:
            print(Fore.YELLOW +
                  " Please enter a 4 digits pin number ----- " + Fore.RESET)
            print()
        if not pin_number.isdigit():
            print(Fore.YELLOW + " Please enter a only numbers ----- " + Fore.RESET)
            print()
        if len(pin_number) == 4 and pin_number.isdigit():
            not_valid_pin_number = False

    return [acc_number, pin_number]


def home_user_panel(active_user, option_list):
    """ Home Panel for the active customer """
    os.system('cls')
    print('-------------------------------------------------------')
    print(Fore.GREEN + ' Home Panel ' + Fore.RESET +
          ' - User: ' + f'{active_user.fullname}')
    print('-------------------------------------------------------')
    print(f" Welcome back {active_user.fullname}")
    print()
    print(" Please select an Transaction Option number >")
    print("-------------------------------------------- ---")

    print(" [ " + Fore.GREEN + '1' + Fore.RESET + " ] " + 'View Balance')
    print(" [ " + Fore.GREEN + '2' + Fore.RESET + " ] " + 'Make a Deposit')
    print(" [ " + Fore.GREEN + '3' + Fore.RESET + " ] " + 'Make a Withdraw')
    print(" [ " + Fore.GREEN + '4' + Fore.RESET + " ] " +
          'View all Your transactions')
    print()
    print(" [ " + Fore.GREEN + 'C or c' + Fore.RESET + " ] to Cancel")
    print()

    loop = True
    counter = -1
    while loop:
        counter += 1
        choice = input(' Option: ')
        if choice not in option_list:
            if counter == 3:
                choice = 99
                break
            # print(Fore.YELLOW + ' Please enter a number between 0 and 3 -' + Fore.RESET)
            print()
        else:
            loop = False

    return choice
    # active_user.show_active_user()


def look_for_account_balance(active_user, database_data):
    """ Process the data to collect the last transaction balance """
    data_lines = database_data.splitlines()
    balance = 0
    for data_line in data_lines:
        line_parts = data_line.split('\t')
        if line_parts[2] == active_user.account_number:
            balance = line_parts[5]

    return balance


def display_account_balance(active_user, database_data):
    """ Look for the customer account balance """
    os.system('cls')
    print('-------------------------------------------------------')
    print(Fore.GREEN + ' Home Panel ' + Fore.RESET +
          ' - User: ' + f'{active_user.fullname}')
    print('-------------------------------------------------------')
    amount = look_for_account_balance(active_user, database_data)
    to_currency = f"${float(amount):,.2f}"
    print(' Account Balance is: ' + to_currency)
    print('-------------------------------------------------------')
    print('Enter [ ' + Fore.GREEN + "Any Key" + Fore.RESET + ' ] to go back')
    print()
    selection = ''
    while selection == '':
        selection = input(' Option: ')


def numeric_verification(number_string):
    """ Verify if the string can be used as a amount, float or integer """
    is_a_float = False
    is_a_integer = False

    try:
        float(number_string)
        is_a_float = True
    except ValueError:
        pass

    try:
        int(number_string)
        is_a_integer = True
    except ValueError:
        pass

    return [is_a_float, is_a_integer]


def display_deposit_panel(active_user):
    """ Display Deposit panel """
    os.system('cls')
    print('-------------------------------------------------------')
    print(Fore.GREEN + ' Home Panel ' + Fore.RESET +
          ' - User: ' + f'{active_user.fullname}')
    print('-------------------------------------------------------')
    print('-  DEPOSIT ---- ')
    print('-------------------------------------------------------')
    print()

    loop = True
    while loop:
        deposit = input(' Enter amount of deposit: ')
        # print(numeric_verification(deposit))
        if True not in numeric_verification(deposit):
            print()
            print(Fore.YELLOW + " Please enter only numbers -" + Fore.RESET)
            time.sleep(1.5)
            print()
        else:
            loop = False
    return_data = []
    return_data.append(deposit)
    return_data.append(active_user.balance)
    return return_data


def display_withdraw_panel(active_user):
    """ Display Withdraw panel """
    os.system('cls')
    print('-------------------------------------------------------')
    print(Fore.GREEN + ' Home Panel ' + Fore.RESET +
          ' - User: ' + f'{active_user.fullname}')
    print('-------------------------------------------------------')
    print('-  WITHDRAW ---- ')
    print('-------------------------------------------------------')
    print()

    loop = True
    while loop:
        withdraw = input(' Enter amount to withdraw: ')
        if True not in numeric_verification(withdraw):
            print()
            print(Fore.YELLOW + " Please enter only numbers -" + Fore.RESET)
            time.sleep(1.5)
            print()
        else:
            loop = False
    return_data = []
    return_data.append(withdraw)
    return_data.append(active_user.balance)
    return return_data

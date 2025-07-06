""" All Fakeback Transactions """
import os
# from present import display_notification
from optionpanel import log_in_panel

from colorama import Fore
from colorama import init
init()


def display_notification(message):
    """Function printing informative indication."""
    return Fore.GREEN + message + Fore.RESET


def display_table_header(message):
    """Function printing colored header for the table."""
    return Fore.YELLOW + message + Fore.RESET


def log_in_(database_data):
    """ Log In Process """
    continue_loop = True
    continue_loop_options = ['T', 't', 'C', 'c']
    # selected = ''
    while (continue_loop):
        option_data_array = log_in_panel()
        if option_data_array[0]:
            return option_data_array
        else:
            choice = ''
            while (choice == ''):
                print('[ ' + Fore.GREEN + "T or t" + Fore.RESET + ' ] for Try again - [ ' +
                      Fore.GREEN + "C or c" + Fore.RESET + ' ] for Cancel')
                print()
                choice = input('Option: ')
                if (choice not in continue_loop_options):
                    choice = ''

                if (choice == 'T' or choice == 't'):
                    continue_loop = True
                    break

                if (choice == 'C' or choice == 'c'):
                    continue_loop = False
                    break

    return option_data_array


def process_customer_transactions(acount, pin, data):
    """ Collect all transactions of the Customer only """
    column_gap = "  "
    page = []
    pages = []

    data_lines = data.splitlines()
    for data_line in data_lines:
        line_parts = data_line.split('\t')
        line = ''
        if (line_parts[2] == acount and line_parts[3] == pin):
            to_currency = f"${float(line_parts[5]):,.2f}"
            line = line + line_parts[0] + column_gap + \
                line_parts[4] + column_gap + to_currency
            page.append(line)
            if (len(page) == 10):
                pages.append(page)
                page = []
    if page:
        pages.append(page)

    return pages


def display_all_customer_transactions(paginas, numero_pagina, active_user):
    """ Display the customers transactions by page """
    page_number = int(numero_pagina)
    pages_count = len(paginas)
    pages = paginas

    os.system('cls')
    print('----------------------------------------------------------------------------------')
    print(Fore.GREEN + ' Home Panel ' + Fore.RESET +
          ' - User: ' + f'{active_user}')
    print('----------------------------------------------------------------------------------')

    pageinfo = pages[page_number]

    for lineinfo in pageinfo:
        print(lineinfo)

    print('-----------------------------------------------------------------------------------')
    print(
        f'                           Page: {page_number + 1} of {pages_count}')
    print('-----------------------------------------------------------------------------------')
    print('[ ' + display_notification("F or f") +
          ' ] for Page Forward - [ ' + display_notification("B or b") +
          ' ] for Page Backward - [ ' + display_notification("C or c") +
          ' ] for Cancel')

    loop = True
    while loop:
        selected = input('Option: ')
        if selected in ('F', 'f'):
            page_number = page_number + 1
            if page_number + 1 > pages_count:
                page_number = pages_count - 1
                display_all_customer_transactions(
                    pages, page_number, active_user)
                loop = False
            else:
                display_all_customer_transactions(
                    pages, page_number, active_user)
                loop = False
        elif selected in ('B', 'b'):
            page_number = page_number - 1
            if page_number < 0:
                page_number = 0
                display_all_customer_transactions(
                    pages, page_number, active_user)
                loop = False
            else:
                display_all_customer_transactions(
                    pages, page_number, active_user)
                loop = False
        elif selected in ('C', 'c'):
            loop = False


def view_customer_transactions(account, pin, data, active_user):
    """ All Customer Transactions """
    pages = process_customer_transactions(account, pin, data)
    display_all_customer_transactions(pages, 0, active_user)


def display_all_transactions(paginas, numero_pagina):
    """ Display the transactions by page """
    page_number = int(numero_pagina)
    pages_count = len(paginas)
    pages = paginas

    os.system('cls')
    print(display_notification("All Transactions Table"))
    print("----------------------------------------------------------------------------------")
    print(display_table_header(
        ' Trans_id  Full Name                   Acct   Pin   Typ  Balance'))
    print('----------------------------------------------------------------------------------')
    pageinfo = pages[page_number]

    for lineinfo in pageinfo:
        print(lineinfo)

    print('---------------------------------------------------------------------------------')
    print(
        f'                           Page: {page_number + 1} of {pages_count}')
    print('---------------------------------------------------------------------------------')
    print('[ ' + display_notification("F or f") +
          ' ] for Page Forward - [ ' + display_notification("B or b") +
          ' ] for Page Backward - [ ' + display_notification("C or c") +
          ' ] for Cancel')

    loop = True
    while (loop):
        selected = input('Option: ')
        if (selected == 'F' or selected == 'f'):
            page_number = page_number + 1
            if (page_number + 1 > pages_count):
                page_number = pages_count - 1
                display_all_transactions(pages, page_number)
                loop = False
            else:
                display_all_transactions(pages, page_number)
                loop = False
        elif (selected == 'B' or selected == 'b'):
            page_number = page_number - 1
            if (page_number < 0):
                page_number = 0
                display_all_transactions(pages, page_number)
                loop = False
            else:
                display_all_transactions(pages, page_number)
                loop = False
        elif (selected == 'C' or selected == 'c'):
            loop = False


def process_all_transactions(data):
    """ Process all transactions for later presentation"""

    # Columns distributions
    c1 = 8
    c2 = 26
    column_gap = "  "
    line = " "
    page = []
    pages = []

    data_lines = data.splitlines()

    for data_line in data_lines:
        line_parts = data_line.split('\t')
        trimmed_name = ""
        gap_string = ""
        line = " "
        define_spaces = -1
        # start visual organization
        if len(line_parts[0]) < c1:
            define_spaces = c1 - len(line_parts[0])
            while define_spaces != 0:
                gap_string = gap_string + " "
                define_spaces = define_spaces - 1
            line = line + line_parts[0] + gap_string + column_gap
            gap_string = ""
            define_spaces = -1
        else:
            line = line + line_parts[0] + column_gap
            gap_string = ""
            define_spaces = -1

        # If name is too long remove extra characters
        if (len(line_parts[1]) > c2):
            remove_extra = len(line_parts[1]) - c2
            trimmed_name = line_parts[1][:-remove_extra]

        # adding spaces for visual organization to the name
        if (len(line_parts[1]) < c2):
            define_spaces = c2 - len(line_parts[1])
            while (define_spaces != 0):
                gap_string = gap_string + " "
                define_spaces = define_spaces - 1

            trimmed_name = line_parts[1] + gap_string
            gap_string = ""
            define_spaces = -1

        to_currency = f"${float(line_parts[5]):,.2f}"
        line = line + trimmed_name + column_gap + \
            line_parts[2] + column_gap + line_parts[3] + column_gap + \
            line_parts[4] + column_gap + column_gap +\
            to_currency + column_gap
        page.append(line)
        # print(line)
        if (len(page) == 10):
            pages.append(page)
            page = []

    if page:
        pages.append(page)
        page = []

    display_all_transactions(pages, 0)

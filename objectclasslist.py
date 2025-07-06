""" List of all objects created """


class ActiveCustomer():
    """Class representing a active log-in user information"""

    def __init__(self, fullname, account_number, pin_number, balance):
        self.fullname = fullname
        self.account_number = account_number
        self.pin_number = pin_number
        self.balance = balance

    def __main__(self):
        pass

    def show_active_user(self):
        """ Display the information on the instance """
        print('      Full Name: ' + self.fullname)
        print(' Account Number: ' + self.account_number)
        print('     Pin Number: ' + self.pin_number)
        print('        Balance: ' + self.balance)

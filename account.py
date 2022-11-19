class Account:
    def __init__(self, name: str):
        """
        Creates account object
        :param name: Name of account
        """
        self.account_name = name
        self.account_balance = 0

    def deposit(self, amount: float):
        """
        Method to deposit money into account. Adds the amount entered to account balance
        :param amount: deposit amount
        :return: if the deposit was successful or not
        """
        if amount <= 0:
            return False
        else:
            self.account_balance += amount
            return True

    def withdraw(self, amount: float):
        """
        Method to withdraw money out of account. Subtracts the amount entered from account balance
        :param amount: withdraw amount
        :return: if the withdrawal was successful or not
        """
        if 0 >= amount >= self.account_balance:
            return False
        else:
            self.account_balance -= amount
            return True

    def get_balance(self):
        """
        retrieves balance on the account
        :return self.account_balance
        """
        return self.account_balance

    def get_name(self):
        """
        retrieves name on the account
        :return: self.account_name
        """
        return self.account_name

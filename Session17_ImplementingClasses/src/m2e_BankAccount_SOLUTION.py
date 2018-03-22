"""
A simple   BankAccount   class, to serve as a first example.

In examining the code, note that:

  1. The __init__ method sets initial values for instance variables,
     using the   self   notation, like this:
        self.blah = ...

     Often, but not always, these initial values come from the
     arguments to the __init__ method.

  2. Some methods, like the   deposit   and   withdraw   methods below,
     have arguments and modify the instance variables (which use
     the self.XXX notation) based on those arguments, like this:
        self.balance = self.balance + amount

  3. Some methods, like the  number_of_deposits  method below,
     return information that is based on the current value of the
     instance variables, like this:
        return self.transactions.count('Deposit')

  4. Some methods, like the   combine_from   and   combine_into  methods
     below, take other objects as arguments. Also, sometimes those
     arguments are the same type as the class being defined.  In that
     case, one uses the usual dot notation on such objects, like this:
        other_balance = another_bank_account.balance

  5. Some methods return objects, possibly even the object on which
     the method was called.  To return the object on which the method
     was called, return   self.

     For example, if from OUTSIDE the class we wrote statements:
     a1 = BankAccount(700)
     a2 = BankAccount(400)

     then when the following expression is evaluated:
        a1.richer(a2)
     (where the richer method returns whichever account has a
     greater balance, a1 or a2 in this example), the  richer  method
     would return   self   which here would be the   a1   object.

Authors: David Mutchler, Mark Hays, Michael Wollowski, Amanda Stouder,
         Chandan Rupakheti, Katie Dion, Claude Anderson, Delvin Defoe,
         Curt Clifton, Matt Boutell, Dave Fisher and their colleagues,
         and SOLUTION by David Mutchler.  October 2014.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE


def main():
    """ Not used here, but could be used for informal testing. """
    pass


class BankAccount(object):
    """ A very simple representation of a Bank Account. """

    def __init__(self, balance=0):
        """ Constructs a new Bank Account with the given balance. """
        self.balance = balance
        self.transactions = []

        if balance > 0:
            format_string = 'Initial deposit of {}'
            self.transactions.append(format_string.format(balance))

    def __repr__(self):
        """ Returns a string representation of this Bank Account. """
        format_string = 'BankAccount with balance ${:,} and transactions: {}.'
        return format_string.format(self.balance, self.transactions)

    def deposit(self, amount):
        """
        Deposits the given amount into this BankAccount.

        Precondition: the given   amount   is a positive number.
        """
        self.balance = self.balance + amount
        self.transactions.append('Deposit {}.'.format(amount))

    def withdraw(self, amount):
        """
        Withdraws the given   amount   from this BankAccount,
        unless the withdrawal would make a negative balance
        (in which case the transaction is logged but nothing
        is actually withdrawn).
        Returns True if the withdrawal succeeded, else returns False.

        Precondition: the given   amount   is a positive number.
        """
        # DONE: 2. We put an ERROR here (on purpose) so that your
        #          testing can expose/debug it.  Correct that error.
        if self.balance - amount >= 0:
            self.balance = self.balance - amount
            self.transactions.append('Withdraw {}.'.format(amount))
            return True
        else:
            message = 'Refuse withdrawal of {}.'
            self.transactions.append(message.format(amount))
            return False

    def number_of_deposits(self):
        """
        Returns the number of deposits made to this BankAccount,
        including the initial deposit (if any).
        """
        # DONE: 3. We put an ERROR here (on purpose) so that your
        #          testing can expose/debug it.  Correct that error.
        count = 0
        for k in range(len(self.transactions)):
            if 'eposit' in self.transactions[k]:
                count = count + 1

        return count

    def number_of_withdrawals(self):
        """
        Returns the number of successful withdrawals
        made from this BankAccount.
        """
        # DONE: 4. Implement and test this method.
        count = 0
        for k in range(len(self.transactions)):
            if 'Withdraw' in self.transactions[k]:
                count = count + 1

        return count

    def number_of_refused_withdrawals(self):
        """
        Returns the number of times that a requested withdrawal was
        refused because it would have made a negative balance.
        """
        count = 0
        for k in range(len(self.transactions)):
            if 'Refuse withdrawal of' in self.transactions[k]:
                count = count + 1

        return count

    def transfer_from(self, another_bank_account):
        """
        Withdraws all the money OUT of the given   another_bank_account
        and deposits it all INTO this BankAccount.

        Precondition:
          :type another_bank_account: BankAccount
        """
        other_balance = another_bank_account.balance
        another_bank_account.withdraw(other_balance)
        self.deposit(other_balance)

    def transfer_into(self, another_bank_account):
        """
        Withdraws all the money OUT of THIS BankAccount and deposits it
        INTO the given   another_bank_account.

        Precondition:
          :type another_bank_account: BankAccount
        """
        # DONE: 5. Implement and test this method.
        balance = self.balance
        self.withdraw(balance)
        another_bank_account.deposit(balance)

    def richer(self, another_bank_account):
        """
        Returns whichever BankAccount has more money,
        this one or the given another_bank_account.
        If tied, returns this one.

        Precondition:
          :type another_bank_account: BankAccount
        """
        # DONE: 6. We put an ERROR here (on purpose) so that your
        #          testing can expose/debug it.  Correct that error.
        if self.balance >= another_bank_account.balance:
            return self
        else:
            return another_bank_account

    def transfer_to_new_account(self):
        """
        Withdraws all the money OUT of THIS BankAccount,
        putting it into a new BankAccount.
        Returns the new BankAccount.
        """
        # DONE: 7. Implement and test this method.
        balance = self.balance
        self.withdraw(balance)

        return BankAccount(balance)

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()

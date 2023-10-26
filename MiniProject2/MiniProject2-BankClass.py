# <<< Bank Account Class >>>
class BankAccount():
    def __init__(self, customer_name, checking_bal, savings_bal):
        self.customer_name = customer_name
        self.savings_bal = float(savings_bal)
        self.checking_bal = float(checking_bal)

    def deposit_checking(self, amount):
        amount = float(amount)
        if amount > 0:
            self.checking_bal += amount
            return f'< New Checking Balance is: ${self.checking_bal:,.2f} >'
        else:
            return '< Amount Entered is Negative >'

    def deposit_savings(self, amount):
        amount = float(amount)
        if amount > 0:
            self.savings_bal += amount
            return f'< New Savings Balance is: ${self.savings_bal:,.2f} >'
        else:
            return '< Amount Entered is Negative >'

    def withdraw_checking(self, amount):
        amount = float(amount)
        if amount > 0:
            if self.checking_bal - amount > 0:
                self.checking_bal -= amount
                return f'< New Checking Balance is: ${self.checking_bal:,.2f} >'
            else:
                print('< Amount is Greater Than Current Balance >')
        else:
            print('< Amount Entered is Negative >')

        return self.withdraw_checking(input('How much would you like to withdraw from checking: '))



    def withdraw_savings(self, amount):
        amount = float(amount)
        if amount > 0:
            if self.savings_bal - amount > 0:
                self.savings_bal -= amount
                return f'< New Savings Balance is: ${self.savings_bal:,.2f} >'
            else:
                print('< Amount is Greater Than Current Balance >')
        else:
            print('< Amount Entered is Negative >')

        return self.withdraw_savings(input('How much would you like to withdraw from savings: '))

    def transfer_to_savings(self, amount):
        amount = float(amount)
        if amount > 0:
            if self.checking_bal - amount > 0:
                self.checking_bal -= amount
                self.savings_bal += amount
                return f'< New Checking Balance is: ${self.checking_bal:,.2f} >\n< New Savings Balance is: ${self.savings_bal:,.2f} >'
            else:
                print('< Amount is Greater Than Current Balance >')
        else:
            print('< Amount Entered is Negative >')

        return self.transfer_to_savings(input('How much would you like to transfer to savings: '))

    def print_account_statement(self):
        print()
        print(f'{"<<< Account Statement >>>":^39}\n{f"Checking Account Balance:":<}{f"${self.checking_bal:>,.2f}":>14}\n{f"Savings Account Balance:":<}{f"${self.savings_bal:>,.2f}":>15}')
        print()


# <<< Testing Program >>>
new_account = BankAccount('John Doe', 1000.00, 2000.00)
new_account.print_account_statement()
print(new_account.withdraw_checking(input('How much would you like to withdraw from checking: ')))
print(new_account.withdraw_savings(input('How much would you like to withdraw from savings: ')))
print(new_account.transfer_to_savings(input('How much would you like to transfer to savings: ')))
new_account.print_account_statement()



#David Sybrandy
#Assignment 8.1

class BankAccount:
    """A parent class representing Bank Account."""

    def __init__(self, accountNum, balance):
        self.accountNumber = accountNum
        self.balance = float(balance)
        print("Account has been created")
        print("The account number is " + str(self.accountNumber))
        print("The balance is $" + str(self.balance))

    def withdrawl(self):
        userWithdrawl = input("\nHow much would you like to withdrawl? ")
        self.balance = self.balance - float(userWithdrawl)
        self.getBalance()

    def deposit(self):
        userDeposit = input("\nHow much would you like to deposit? $")
        self.balance = self.balance + float(userDeposit)
        self.getBalance()

    def getBalance(self):
        print("\nCurrent account balance is: $" + str(self.balance))

class CheckingAccount(BankAccount):
    """A child class, checking account, to parent class BankAccount."""

    def __init__(self, accountNum, balance, fee, minBal):
        BankAccount.__init__(self, accountNum, balance)
        self.accountFees = fee
        self.minimumBalance = minBal
        print("\nThe account fee is $" + str(self.accountFees))
        print("The minimum balance is $" + str(self.minimumBalance))

    def deductFees(self):
        print("\nDeducting fee...")
        self.balance = self.balance - self.accountFees
        print("Balance after fee is $" + str(self.balance))

    def checkingMinimumBalance(self):
        print("\nChecking if account balance meets minimum balance...")

        if float(self.balance) < self.minimumBalance:
            print("\nAccount balance is too low")
            print("You must deposit $" + str(self.minimumBalance - self.balance) + " to meet the minimum account balance")
            self.deposit()
            self.checkingMinimumBalance()
        else:
            print("Account balance meets minimum balance requirements")

class SavingsAccount(BankAccount):
    """A child class, savings account, to parent class BankAccount."""
    def __init__(self, accountNum, balance, interestRate):
        BankAccount.__init__(self, accountNum, balance)
        self.interestRate = interestRate
        print("The annual ") #create a print for annual interest rate

    def addInterest(self):
        print("Adding interest...")
        self.balance = self.balance * self.interestRate
        print("Savings balance after interest added is $" + str(self.balance))

#main program
print("\nWelcome to CIS245 Federal Credit Union")

try:
    flag1 = 0
    while flag1 == 0:
        print("\n***Main Menu***")
        print("Open Checking Account, press 1")
        print("Open Savings Account, Press 2")
        print("Exit program, press 3")
        loop1 = input("")

        if loop1 == '1':
            flag2 = 0
            while flag2 == 0:
                flag2 = 1
                print("\nWould you like to open a Checking Account? Press 1")
                loop2 = input("")

                if loop2 == '1':
                    print("\n***Checking Account Setup***")
                    print("\n- Minimum Balance is $50.00")
                    print("- Account Fee is $5.00")
                    checkingAccountNumber = input("\nEnter an Account Number: ")
                    checkingAccountBalance = input("Enter Account Balance: $")
                    print("\nPlease wait while account is created...\n")
                    my_checkingAccount = CheckingAccount(checkingAccountNumber, checkingAccountBalance, 5.0, 50.0)
                    my_checkingAccount.deductFees()
                    my_checkingAccount.checkingMinimumBalance()

                    flag3 = 0
                    while flag3 == 0:
                        print("\n***New Account Menu***")
                        print("\nWhat would you like to do?")
                        print("- Check your balance, press 1")
                        print("- Make a deposit, press 3")
                        print("- Make a withdrawl, press 4")
                        print("- Go to Main Menu, press 5")
                        loop3 = input("")

                        if loop3 == '1':
                            my_checkingAccount.getBalance()
                        elif loop3 == '3':
                            my_checkingAccount.deposit()
                        elif loop3 == '4':
                            my_checkingAccount.withdrawl()
                        elif loop3 == '5':
                            print("Exiting to Main Menu...")
                            flag3 = 1
                        else:
                            print("Command not recognized")

                else:
                    print("Command not recognized")
                    flag2 = 0

        elif loop1 == '2':
            flag4 = 0
            while flag4 == 0:
                flag4 = 1
                print("\nWould you like to open a Savings Account? Press 1")
                loop2 = input("")

                if loop2 == '1':
                    print("\n***Savings Account Setup")
                    print("\n- Annual Interest Rate is 2%")
                    savingsAccountNumber = input("\nEnter an Account Number: ")
                    savingsAccountBalance = input("Enter the deposit amount: $")
                    print("Please wait while account is created...")
                    my_savingsAccount = SavingsAccount(savingsAccountNumber, savingsAccountBalance, 1.02)
                    my_savingsAccount.addInterest()

        elif loop1 == '3':
            print("Exiting Program...")
            flag1 = 1

        else:
            Print("Command not recognized")
except:
    print("broken")

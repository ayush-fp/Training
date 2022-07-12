from account import Account
from bank import Bank

class Customer:
    customerId = -1
    allCustomer = []
    def __init__(self, firstNAme, lastName, username):
        self.firstNAme = firstNAme
        self.Lastname = lastName
        self.totalBalance = 0
        self.username = username
        self.customerId = Customer.customerId
        self.accounts = []

    @staticmethod
    def findCustomer(username):
        for u in Customer.allCustomer:
            if u.username == username:
                return True, u
        return False, None


    @staticmethod
    def createNewCustomer(firstName, lastName, username):
        isCustomerExist, customer = Customer.findCustomer(username)
        if isCustomerExist:
            return False, "Username already exists"
        Customer.customerId += 1
        newCustomer = Customer(firstName, lastName, username)
        Customer.allCustomer.append(newCustomer)
        #return True, "Customer Created"
        return Customer(firstName, lastName, username)
    
    def deposit(self, amount, bankAbbreviation):
        isAccountExists, account = self.findAccount(bankAbbreviation)
        if not isAccountExists:
            return False, "Account Does not Exist"
        account.balance += amount
        self.__updateTotalBalance()
        self.displayBalance(bankAbbreviation)
        return True, "Amount Deposited"
    
    def withdraw(self, amount, bankAbbreviation):
        isAccountExists, account = self.findAccount(bankAbbreviation)
        if not isAccountExists:
            return False, "Account Does not Exist"
        #check balance is sufficient
        if not account.isSufficientBalance(amount):
            return False, "Insufficient Balance"
        account. balance -= amount
        self.__updateTotalBalance()
        self.displayBalance(bankAbbreviation)
        return True, "Amount Withdrawn"

    def transferAmount(self, creditCustomerUsername, creditbankAbbreviation, debitbankAbbreviation, amount):
    
        iscreditCustomerExists, creditCustomer = Customer.findCustomer(creditCustomerUsername)
        if not iscreditCustomerExists:
            return False, "creditCustomer Does not exist"
        
        isAmountWithdrawn, message = self.withdraw(amount, debitbankAbbreviation)
        if not isAmountWithdrawn:
            return False, "Transfer incomplete, low balance"
        
        isAmountCredited, message = creditCustomer.deposit(amount, creditbankAbbreviation)
        if not isAmountCredited:
            self.deposit(amount, debitbankAbbreviation)
            return False, "Transfer incomplete, reditCustomer bank account Not found"
        
        return True, "Amount Transferred"
    
    def selfTransfer(self, creditbankAbbreviation, amount, debitbankAbbreviation):
        #self.transferAmount(self.username, creditbankAbbreviation, debitbankAbbreviation, amount)
        isAmountWithdrawn, message = self.withdraw(amount, debitbankAbbreviation)
        if not isAmountWithdrawn:
            return False, "Transfer incomplete, low balance"
        
        isAmountCredited, message = self.deposit(amount, creditbankAbbreviation)
        if not isAmountCredited:
            self.deposit(amount, debitbankAbbreviation)
            return False, "Transfer incomplete, reditCustomer bank account Not found"
        

        return True, "Amount Transferred"


    def findAccount(self, bankAbbreviation):
        if (len(self.accounts) == 0):
            return False, "No accounts found"
        for a in self.accounts:
            if a.isAccountExist(bankAbbreviation):
                return True, a
        return False, None

    def __updateTotalBalance(self):
        self.totalBalance = 0
        for a in self.accounts:
            self.totalBalance += a.balance
    
    def displayTotalBalance(self):
        print(self.firstNAme, " Total Balance is ", self.totalBalance)
    
    def displayBalance(self, bankAbbreviation):
        for a in self.accounts:
            if a.bank.bankAbbreviation == bankAbbreviation:
                print(self.username, a.bank.bankAbbreviation, a.balance)
                return True, "Account Balance displayed"
        return False, "Wrong bankAbbreviation given"

    def createNewAccount(self, bankAbbreviation):
        #check for multiple accounts of a customer in same bank
        isAccountExist, account = self.findAccount(bankAbbreviation)
        if isAccountExist:
            return False, "Your Account already exist"
        isAccountCreated, account = Account.createNewAccount(bankAbbreviation)
        if not isAccountCreated:
            return False, "Account not created, Retry"
        self.accounts.append(account)
        self.__updateTotalBalance()
        #Update customer details in customer list after creating accounts
        for customer in Customer.allCustomer:
            if self.username == customer.username:
                customer.accounts = self.accounts
                customer.totalBalance = self.totalBalance
        return True, "Account Created"

if __name__ == "__main__":
    #Creating Bank
    Bank.createNewBank("State Bank of India", "sbi")
    Bank.createNewBank("Axis Bank", "axis")
    Bank.createNewBank("Union Bank of India", "ubi")

    #Creating Customers
    Tim = Customer.createNewCustomer("Tim", "Cook", "timcook")
    Ram = Customer.createNewCustomer("Ram", "Kumar", "ramkumar")

    #Creating accounts for customers
    Tim.createNewAccount("sbi")
    Tim.createNewAccount("axis")
    Ram.createNewAccount("sbi")
    Ram.createNewAccount("ubi")

    #Check Balance of all accounts of a customer
    Tim.displayTotalBalance()
    Ram.displayTotalBalance()
    print("\n")

    #Check individual account balance of a customer
    Tim.displayBalance("sbi")
    Ram.displayBalance("ubi")
    print("\n")

    #Check for a customer to deposit amount to own account
    Tim.deposit(200, "sbi")
    Ram.deposit(300, "ubi")
    print("\n")

    #Check for a customer to withdraw amount from own account
    Tim.withdraw(200, "sbi")
    Ram.withdraw(200, "ubi")
    print("\n")

    #Check for self transfer
    Tim.selfTransfer("axis", 500, "sbi")
    Tim.displayTotalBalance()
    print("\n")
    
    #Check for transfer to another customer
    Ram.displayBalance("sbi")
    Ram.displayBalance("ubi")
    Ram.displayTotalBalance()
    Tim.transferAmount("ramkumar", "ubi", "axis", 500)
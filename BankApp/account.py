from bank import Bank

class Account:
    accountID = -1
    def __init__(self, bank, balance):
        self.bank = bank
        self.balance = balance
        self.accountID = Account.accountID

    def isAccountExist(self, bankAbbreviation):
        return self.bank.bankAbbreviation == bankAbbreviation
    def displayBalance(self):
        print(self.bank.bankAbbreviation, " balance is: ", self.balance)
    def isSufficientBalance(self, amount):
        return self.balance >= amount

    @staticmethod
    def createNewAccount(bankAbbreviation):
        isBankExist, bankObject = Bank.findBank(bankAbbreviation)
        if not isBankExist:
            return False, "Bank does not exists"
        Account.accountID += 1
        newAccount = Account(bankObject, 1000)
        return True, newAccount
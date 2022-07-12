class Bank:
    bankId = -1
    allBanks = []
    def __init__(self, fullNAme, bankAbbreviation):
        self.fullName = fullNAme
        self.bankAbbreviation = bankAbbreviation
        Bank.bankId +=1
        self.bankID = Bank.bankId


    @staticmethod
    def findBank(bankAbbreviation):
        for i in Bank.allBanks:
            if i.bankAbbreviation == bankAbbreviation:
                return True, i
        return False, None
    
    @staticmethod
    def createNewBank(fullName, bankAbbreviation):
        isBankExist, bankObject = Bank.findBank(bankAbbreviation)
        if isBankExist:
            return False, "Bank bankAbbreviation already exists"
        if bankObject != None:
            if bankObject.fullName == fullName:
                return False, "Bank Full name already exists"
        newBank = Bank(fullName, bankAbbreviation)
        Bank.allBanks.append(newBank)
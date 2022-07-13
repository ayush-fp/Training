class ContactDetails:
    Contact_Detail_ID = -1
    def __init__(self, Type, Email):
        self.Type = Type
        self.Email = Email
        ContactDetails.Contact_Detail_ID += 1

    
    @staticmethod
    def createContactDetails(Type, Email):
        return ContactDetails(Type, Email)
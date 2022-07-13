from contactDetails import ContactDetails

class Contact:
    ContactID = -1
    def __init__(self, F_name, L_name, Full_name, isActive):
        self.F_name = F_name
        self.L_name = L_name
        self.Full_name = Full_name
        self.isActive = isActive
        self.Contact_Details = []
        Contact.ContactID += 1
        self.ContactID = Contact.ContactID
    
    @staticmethod
    def createContact(F_name, L_name, isActive):
        """factory function to create a contact"""
        Full_name = F_name+L_name
        return Contact(F_name, L_name, Full_name, isActive)

    def createContactDetails(self, Type, Email):
        if self.isActive == True:
            contactDetails = ContactDetails.createContactDetails(Type, Email)
            self.Contact_Details.append(contactDetails)
    
    def readContactDetail(self, Type):
        for cd in self.Contact_Details:
            if cd.Type == Type:
                return cd


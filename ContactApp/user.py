from contact import Contact
from contactDetails import ContactDetails

class User:
    userID = -1
    usersAll = []
    def __init__(self, F_name, L_name, username, isAdmin, isActive):
        self.F_name = F_name
        self.L_name = L_name
        self.username = username
        self.isAdmin = isAdmin
        self.isActive = isActive
        User.userID += 1
        self.userID = User.userID
        self.Contacts = []
    
    @staticmethod
    def createAdmin(F_name, L_name):
        username = F_name+L_name
        admin =  User(F_name, L_name, username, True, True)
        User.usersAll.append(admin)
        return admin

    def createNewUser(self, F_name, L_name, isActive):
        """factory function to create a normal user"""
        if self.isAdmin == False:
            return "User not created, Not an admin"
        isAdmin = False
        username = F_name+L_name
        NewUser =  User(F_name, L_name, username, isAdmin, isActive)
        User.usersAll.append(NewUser)
        return NewUser
    
    def createContact(self, F_name, L_name, isActive):
        if self.isActive == True:
            contact = Contact.createContact(F_name, L_name, isActive)
            self.Contacts.append(contact)
    
    def createContactDetails(self, ContactFullName, Type, Email):
        if self.isActive == True:
            for c in self.Contacts:
                if c.Full_name == ContactFullName:
                    c.createContactDetails(Type, Email)

    def deleteUser(self, username):
        if self.isAdmin == True:
            for u in User.usersAll:
                if u.username == username:
                    u.isActive = False
                    print("User Deleted")
    
    def readContact(self, Full_name, Type):
        if self.isActive == True:
            for c in self.Contacts:
                if c.isActive == True:
                    if(c.Full_name == Full_name):
                        cd = c.readContactDetail(Type)
                        print(c.F_name, " ", c.L_name, " ", cd.Email)
                else:
                    print("No such contact present")
    
    def deleteContact(self, Full_name):
        if self.isActive == True:
            for c in self.Contacts:
                if(c.Full_name == Full_name):
                    c.isActive = False

if __name__ == "__main__":
    
    Admin = User.createAdmin("Ram", "Kumar")
    Harry = Admin.createNewUser("Harry", "Potter", True)
    Harry.createContact("Tom", "Cruise", True)
    Harry.createContactDetails("TomCruise", "work", "tom@hollywood.com")
    Harry.createContactDetails("TomCruise", "home", "tom@gmail.com")
    Harry.readContact("TomCruise", "home")
    Harry.readContact("TomCruise", "work")
    Harry.deleteContact("TomCruise")
    Harry.readContact("TomCruise", "home")
    Admin.deleteUser("HarryPotter")
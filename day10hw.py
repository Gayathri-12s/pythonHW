from abc import ABC , abstractmethod

class User(ABC):
    def __init__(self, name, account_year):
        self.name = name
        self.account_year = account_year
        
    def account_age(self):
        return 2025 - self.account_year
    
    @abstractmethod
    def get_role(self):
        pass
class Admin(User):
    def get_role(self):
        return "Admin"
    
    def __str__(self):
        return f"Admin User:{self.name}, account created in {self.account_year}"
    
class Guest(User):
    def get_role(self):
        return "Guest"
    
    def __str__(self):
        return f"Guest User:{self.name}, account created in {self.account_year}"
    
    
Admin_user = Admin("Ravi", 2020)
Guest_user = Guest('Anjali', 2023)

print("role:", Admin_user.get_role())
print("account_age:", Admin_user.account_age(), "years")
print(Admin_user.__str__())


print("role:", Guest_user.get_role())
print("account_age:", Guest_user.account_age(), "years")
print(Guest_user.__str__())
class Account:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        
    def __add__(self, other):
        return self._balance + other._balance

class SavingsAccount(Account):
    def calculate_interest(self):
        # Account.__init__(name, balance)
        return self._balance*0.05 
    
class CurrentAccount(Account):
    def calculate_interest(self):
        return self._balance*0.02
    
savings = SavingsAccount("ravi", 10000)
current = CurrentAccount("anjali", 15000)

print("savings-account:", savings._name)
print("savings-account:", savings._balance)
print(savings.calculate_interest())
print("current-account:", current._name)
print("current-account:", current._balance)
print(current.calculate_interest())

total_balance = savings + current

print("Total balance of Ravi and Anjali:", total_balance)

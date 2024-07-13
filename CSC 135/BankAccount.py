class BankAccount:

    def __init__(self, name):
        self._name = name
        self._balance = 0.00
    
    def deposit(self, amount):
        if amount > 0.00:
            self._balance = self._balance + amount
            
    def withdraw(self, amount):
        if amount > 0.00 and (amount <= self._balance):
            self._balance = self._balance - amount
        
    @property
    def name(self):
        return self._name
    
    @property
    def balance(self):
        return self._balance
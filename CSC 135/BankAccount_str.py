class BankAccount:

    def __init__(self, name = 'John', balance = 0.00):
        self._name = name
        self._balance = balance
        
    def __str__(self):
    #txt = "For only {price:.2f} dollars!"
        txt = self._name + ", ${price:.2f}"
        return (txt.format(price = self._balance))
            
    @property
    def name(self):
        print('name getter called')
        return self._name
    
    @property
    def balance(self):
        print('balance getter called')
        return self._balance
        
    def deposit(self, amount):
        if amount > 0.00:
            self._balance = self._balance + amount
            return self._balance
        else:
            return self._balance
       
    def withdraw(self, amount):
        if amount > 0.00 and (amount <= self._balance):
            self._balance = self._balance - amount
            return self._balance
        else:
            return self._balance
    
yana = BankAccount('Mariana', 3.50)

#print(yana.name)
#print(yana.balance)
str(yana)
#print(yana.__str__())
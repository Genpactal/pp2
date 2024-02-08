class Account:
    def __init__(self, owner, balance):
        self.owner = owner 
        self.balance = balance
    
    def deposit(self, add):
        self.balance = self.balance + add
        print(f'{self.balance}')

    def withdraw(self, take):
        if (take > self.balance):
            print(f'Nah, you cant, bro')
        else:
            self.balance = self.balance - take

    def show(self):
        print(f'{self.balance}')

name = input("Who are you, warrior?")
shekels = int(input())
res = Account(name, shekels)

poo = int(input())
res.deposit(poo)
res.show()

boo = int(input())
res.withdraw(boo)
res.show()
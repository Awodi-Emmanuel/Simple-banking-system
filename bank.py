from user import User

class Bank(User):
    def __init__(self, name, age, gender):
       return super().__init__(name, age, gender)
   
    def deposit(self, amount):
        print("Your account has been credit with: ")
        self.balance = self.balance + amount
        print("Balance: ", self.balance)
        
        
# emmy = Bank('emmy', 30, 'm')
# emmy.deposit(10.0)
        
    def withdraw(self, amount):
        print("You account has been debited")
        print("")
        if self.balance < amount:
            print("You've  insuffieient fund")
        else: 
            self.balance = self.balance - amount
            print(self.balance)
            

emmy = Bank('emmy', 25, 'm')
emmy.withdraw(20.0)
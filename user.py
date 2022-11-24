# Hold the details about the account
class User():
    def __init__(self, name, age, gender):
        self.name = name, 
        self.age = age,
        self.gender = gender
        self.balance = 0.0
        
    def show_user(self):
        print("Personal details")
        print("")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        
emmy = User("emmy", 30, "M")
emmy.show_user()
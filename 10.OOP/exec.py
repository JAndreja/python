# class Comment():
#     def __init__(self,username,text,likes=0):
#         self.username = username
#         self.text = text
#         self.likes = likes

# c=Comment("dave123","lol you're so silly", 3)
# print(c.username)
# print(c.text)
# print(c.likes)

# ***********************************************

# class BankAccount:
#     def __init__(self,owner):
#         self.owner = owner
#         self.balance = 0.0
    
#     def getBalance(self):
#         return self.balance
    
#     def deposit(self,num):
#         self.balance = self.balance +num
#         return self.balance
        
#     def withdraw(self,num):
#         self.balance = self.balance-num
#         return self.balance
        
# acct = BankAccount("Andreja")

# print(acct.owner)
# print(acct.balance)
# print(acct.deposit(10))
# print(acct.withdraw(3))
# print(acct.balance)

# ***********************************************


class Pet:
    
    allowed = ['cat', 'dog' , 'fish', 'rat']
    
    def __init__(self,pet_name,species):
        if species not in Pet.allowed:
          raise ValueError(f"You can't have a {species} pet!")
        self.name = pet_name
        self.species = species
    

cat = Pet("Blue","cat")
dog = Pet("Molly","dog")
#tiger = Pet("Tony","tiger")

print(cat.name)
print(dog.species)
#print(tiger.name)

# ***********************************************

# class Chicken:
#     total_eggs = 0
#     def __init__(self,species,name):
#         self.species = species
#         self.name = name
#         self.eggs = 0
        
#     def lay_egg(self):
#         self.eggs += 1
#         Chicken.total_eggs += 1
#         return self.eggs       
        
    
    
# c1 = Chicken("Patridge Silkie", "Alice")
# c2 = Chicken("Speckled Sussex", "Amelia")

# print(Chicken.total_eggs)
# print(c1.lay_egg())
# print(Chicken.total_eggs)
# print(c2.lay_egg())
# print(c2.lay_egg())
# print(c2.lay_egg())
# print(Chicken.total_eggs)


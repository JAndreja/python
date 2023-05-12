
#class User:
#    pass
#user1 = User()

class User:
    def __init__(self, first,last,age):
            self.name = first
            self.lastname = last
            self.age = age
user1 = User('Andreja','Jovanovski',47)
user2 = User('Radica', 'Jovanovski',41)
print(user1.name)
print(user2.name)
print(f"Hello {user1.name} {user1.lastname}.You are {user1.age} year old")
print(f"Hello {user2.name} {user2.lastname}.You are {user2.age} year old")

################################################################
class Comment():
      def __init__(self, username, text, likes=0):
            self.user = username
            self.txt= text
            self.like = likes

c = Comment("davey123", "lol you're so silly", 3) 
print(c.user)
print(c.txt)
print(c.like)
another_comment = Comment("rosa77", "soooo cute!!!") 
print(another_comment.user)
print(another_comment.txt)
print(another_comment.like)

#print(dir(another_comment))

#######################################################
class Person:
      def __init__(self, first, last,age):
            self.name = first
            self.lname = last
            self.age = age
      
      def full_name(self):
            return f"My first name is {self.name} and my surname is {self.lname}"
      def initial(self):
            return f"{self.name[0]}.{self.lname[0]}"      
      def likes(self, thing):
            return f"{self.name} likes {thing}"

      

user3 = Person("Andreja", "Jovanovski", 47)
user4 = Person("Radica", "Jovanovski", 41)

print(user3.full_name())
print(user4.full_name())
print(user3.initial())
print(user4.initial())
print(user3.likes("Sladoled"))
print(user4.likes('banani'))

#########################################################################


class BankAccount:
      def __init__(self, owner , balance =0):
            self.owner = owner
            self.balance = balance

      def getBalance(self):
            return self.balance

      def deposite(self,num):
            self.balance += num
            return self.balance
      
      def withdraw(self,num):
            self.balance -=num
            return self.balance

      

owner1 = BankAccount("Andreja")
#print(owner1.owner)
#print(owner1.balance)
#print(owner1.deposite(10))
#print(owner1.withdraw(3))

print(owner1.owner)
print(owner1.balance)
print(owner1.deposite(10))
print(owner1.withdraw(3))
print(owner1.getBalance())

#####################################################################


class ChatUser:
    active_users =0      # Class Attributes
    
    def __init__(self,first,last,age):
        self.name= first    
        self.surname = last
        self.age = age
        ChatUser.active_users += 1

    def logut(self):
          ChatUser.active_users -= 1
          return f"{self.name} logged out"
    

print(f"Starting user: {ChatUser.active_users}")
user5 = ChatUser("Kaja","Jovanovski",12)
user6 = ChatUser("Mirko","Stankovski",59)
print(f"New User status: {ChatUser.active_users}")
print(user6.logut())
print(f"New User status: {ChatUser.active_users}")


#########################################################

class Pet:
      allowed = ['cat', 'dog', 'fish', 'rat']
      def __init__(self, name, species):
            if species not in Pet.allowed:
                  raise ValueError(f"You cant have a {species} pet")
            self.name =  name
            self.species = species

cat = Pet("Blue", "cat")
print(cat.name)
#lion = Pet("Red", "lion")
#print(lion.name)
print(cat.allowed)

#########################################################

class Chicken:
      total_eggs = 0
      def __init__(self,name,species):
            self.name = name
            self.species = name
            self.eggs = 0 

      def lay_egg(self):
            self.eggs +=1
            Chicken.total_eggs += 1
            return self.eggs


c1 = Chicken(name="Alice", species="Partridge Silkie")
c2 = Chicken(name="Amelia", species="Speckled Sussex")

print(Chicken.total_eggs)
print(c1.lay_egg())
print(c2.lay_egg())
print(c2.lay_egg())
print(Chicken.total_eggs)
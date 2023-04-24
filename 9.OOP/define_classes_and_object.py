# Object oriented programming is a method of programming that attempts to model some process or thing in the world as a class or object.

# class - a blueprint for objects. Classes can contain methods (functions) and attributes (similar to keys in a dict).

# instance - objects that are constructed from a class blueprint that contain their class's methods and properties

# With object oriented programming, the goal is to encapsulate your code into logical, hierarchical groupings using classes so that you can reason about your code at a higher level.

#class
class User:
    def __init__(self,first,last,age):
        self.name= first    # Instance Attributes 
        self.surname = last
        self.age = age

#instance(object)
user1 = User("Andreja", "Jovanovski",46)
user2 = User("Radica", "Jovanovski", 40)
print(f"Name: {user1.name}")
print(user1.name , user1.surname)
print(user2.age)

print("#-----------------------------------------------")      
# ******************
#Underscores

    #_name  - private list attribute
    #__name - name mangling.Double Pre Underscores tells the Python interpreter to rewrite the attribute name of subclasses to avoid naming conflicts
    #__name__  - dunder methods.

class Person:
    def __init__(self):
        self.name="Tony"
        self._secret = "hi"
        self.__msg = "I like banana"  

p = Person()
print(p.name)
print(p._secret)
#print(dir(p))
#print(p.__msg)    # ke javi greska
print(p._Person__msg)

print("#-----------------------------------------------")
# *****************************
# Instance Attributes and Methods

class User:
    def __init__(self,first,last,age):
        self.name= first    # Instance Attributes 
        self.surname = last
        self.age = age
    
    def full_name(self):  # Instance Methods
        return f"My fist name is {self.name} and my surname is {self.surname}"
    
    def initials(self):
        return f"{self.name[0]}.{self.surname[0]}"

    def likes(self, thing):
       return f"{self.name} likes {thing}"
        
    def senior(self):
        return self.age >= 65
    
    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th , {self.name}"
        
user3=User("Andreja","Jovanovski",46)
user4=User("Mirko","Petrovski",67)


print(user3.full_name())
print(user4.full_name())

print(user3.initials())
print(user4.initials())

print(user3.likes("Ice Cream"))
print(user3.likes("Banana"))

print(user3.senior())
print(user4.senior())

print(user3.birthday())
print(user4.birthday())

print("#-----------------------------------------------")
# *********************************
# Class Attributes

class User:
    active_users =0      # Class Attributes
    
    def __init__(self,first,last,age):
        self.name= first    # Instance Attributes 
        self.surname = last
        self.age = age
        User.active_users += 1 
    
    def logout(self):
        User.active_users -= 1
        return f"{self.name} logged out"
    
    def full_name(self):  # Instance Methods
        return f"My fist name is {self.name} and my surname is {self.surname}"
    
    def initials(self):
        return f"{self.name[0]}.{self.surname[0]}"

    def likes(self, thing):
       return f"{self.name} likes {thing}"
        
    def senior(self):
        return self.age >= 65
    
    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th , {self.name}"

user5=User("Kaja","Jovanovski",11)
user6=User("Slavko","Janevski",54)

print(User.active_users)
print(user6.logout())
print(User.active_users)

print("#-----------------------------------------------")

# *********************************
# Class Methods

class User:
    active_users =0      # Class Attributes
    
    def __init__(self,first,last,age):
        self.name= first    # Instance Attributes 
        self.surname = last
        self.age = age
        User.active_users += 1 
    
    @classmethod
    def display_active_user(cls):
        return f"There are currently {cls.active_users} active users"
    
    @classmethod
    def from_string(cls, data_string):
        name,surname,age = data_string.split(",")
        return cls(name,surname,int(age))
    
    def full_name(self):  # Instance Methods
        return f"My fist name is {self.name} and my surname is {self.surname}"
    
    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th , {self.name}"
    
user7 = User("Mladen", "Ristovski",56)
user8 = User("Viktor", "Mladenovski",34)


print(User.display_active_user())
user9 = User("Nenad", "Ristovski",56)
user10 = User("Stojan", "Mladenovski",34)
print(User.display_active_user())

andreja=User.from_string("Andreja,Jovanovski,12")
print(andreja.name)
print(andreja.full_name())
print(andreja.birthday())
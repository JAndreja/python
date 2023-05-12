
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
# There is a lambda for each value in the iterable.
# Returns filter object which can be converted into other iterables
# The object contains only the values that return true to the lambda



nums =[1,2,3,4]
evens_map = list(map(lambda x: x%2 == 0 ,nums ))
evens_filter = list(filter(lambda x: x%2 == 0 , nums))
print(evens_map)
print(evens_filter)


print("-------------------------------------------------------------------------")
users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

# extracting inactive users using filter
print("# Extracting inactive users using filter")
print()
inactive_users = list(filter(lambda u: u['tweets'] == [] ,users))
print(inactive_users)
inactive_users1 = list(filter(lambda u: len(u['tweets']) == 0 ,users))
print(inactive_users1)
inactive_users3 = list(filter(lambda u: not u['tweets'] ,users))
print(inactive_users3)
print()

# extracting usernames of inactive users using map and filter
print("# Extracting usernames of inactive users using map and filter")
print()
user_n=list(map( lambda user: user['username'], 
            filter(lambda u : not u['tweets'],users)))
print(user_n)
print()

# extracting inactive users using list comprehension
print("# Extracting inactive users using list comprehension")
print()
inactive_list_user=[user for user in users if not user['tweets']  ]
print(inactive_list_user)
print()

# extracting usernames of inactive users using list comprehension
print("# extracting usernames of inactive users using list comprehension")
print()
inactive_username = [ username['username'] for username in users if not username['tweets'] ] 
print(inactive_username)
print()
print("-------------------------------------------------------------------------")

# combine map and filter
names = [ "Andreja", "Radica", "Kaja"]
filter_name = list(filter(lambda name: len(name) < 7, names ))
print(filter_name)
s_name= list(map( lambda name: f"Hello {name}, your name is shorter than 5 character" , filter(lambda value: len(value) < 5 , names)))
print(s_name)


#list comprehension
len_names = [f"Hello {name}, your name is shorter than 5 character" for name in names if len(name)<5]
print(len_names)


# ************************************************************************************************** #
      # EXERCISE
def remove_negatives(num_list):
      return list(filter(lambda num: num >= 0 , num_list ))
      


print(remove_negatives([-1,3,4,-99]))
print(remove_negatives([-7,0,1,2,3,4,5]))

# ************************************************************************************************** #





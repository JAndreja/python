nums = [2,4,6,8]
doubles = list(map( lambda x:x*2 , nums))
print(doubles)


people = ["Andreja", "Radica", "Kaja", "Maza"]

upper_peopole = map(lambda name: name.upper(), people)
upper_peopole = list(upper_peopole)
print(upper_peopole)

names = [
    {'first':'Andreja', 'last': 'Jovanovski'}, 
    {'first':'Radica', 'last': 'Jovanovski', }, 
    {'first':'Kaja', 'last': 'Jovanovski', }
]

firts_name = map( lambda name: name['first'], names)
firts_name=list(firts_name)
print(firts_name)


nums1 = [2,4,6,8]
def double(x):
    return x*x

doubles1 = list(map(double, nums1 ))
print(doubles1)

nums = [1,2,3,4,5,6,7,8]
even_num = list(map(lambda n : n%2 ==0 , nums))
print(even_num)
even_num_filter = list(filter(lambda n : n%2 ==0 , nums))
print(even_num_filter)


users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

inactive_users = list(filter(lambda u: u['tweets'] == [] ,users))
print(inactive_users)
inactive_users1 = list(filter(lambda u: len(u['tweets']) == 0 ,users))
print(inactive_users1)
inactive_users3 = list(filter(lambda u: not u['tweets'] ,users))
print(inactive_users3)

print('###########################################################################################')

list1=all([1,2,3,4,5])
list2=all([0,1,2,3,4])

print(list1)
print(list2)

people = ["Andreja", "Angel", "aneta", "Andrijana"]
without_all=[name[0].upper() == 'A' for name in people]
print(without_all)
with_all=all([name[0].upper() == 'A' for name in people])
print(with_all)

print('###########################################################################################')

midterm = [80,91,78]
finals = [98,89,53]
students = [ 'dan', 'ang', 'kate']

#finals_grade = (zip(midterm,finals))
finals_grade =[max(pair) for pair in zip(midterm,finals)]
print(list(finals_grade))
finals_grade ={ pair[0] :max(pair[1:]) for pair in zip(students,midterm,finals)}
print(finals_grade)
# A standard function that accepts at least two arguments, a function and an "iterable"
# iterable - something that can be iterated over (lists, strings, dictionaries, sets, tuples)
# runs the lambda for each value in the iterable and returns a map object which can be converted into another data structure

nums = [2,4,6,8,10]

doubles =(map(lambda x: x*2 , nums))
print(type(doubles))
print(list(doubles))

people = ["Andreja", "Radica", "Kaja", "Maza"]

upper_people = map(lambda name: name.upper(), people )
upper_people= list(upper_people)
print(upper_people)

names = [
    {'first':'Andreja', 'last': 'Jovanovski'}, 
    {'first':'Radica', 'last': 'Jovanovski', }, 
    {'first':'Kaja', 'last': 'Jovanovski', }
]

first_name = map( lambda x:x['first'], names)
last_name = map( lambda x:x['last'], names)

first_name=list(first_name)
last_name=list(last_name)
print(first_name)
print(last_name)

def dec_lis(num_list):
    return list(map( lambda n: n-1, num_list))

print(dec_lis([1,2,3]))
print(dec_lis([10,20,30]))

# standardna funckija bez map
new_dec =[]
def dec(num_list):
    for i in num_list:
        new_dec.append(i-1)
    print(new_dec)
    
#dec([2,3,4])
dec([50,60,70])
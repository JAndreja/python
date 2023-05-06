"""
def sum_all_num(n1,n2,n3):
    return n1+n2+n3
print(sum_all_num(2,2,2))

def sum_all_num2(*nums):
    print(nums)
sum_all_num2(2,2,2,4)


def sum_all_num3(*nums):
    total =0
    for num in nums:
        total += num
    return total
print(sum_all_num3(2,2,2,4))


def fav_color(**name_color):
    print(name_color)
fav_color( Andreja="green", Janko = "red", Mitra = "orange")

def fav_color2(**name_color):
    for name in name_color.keys():
        print(name)
fav_color2( Andreja="green", Janko = "red", Mitra = "orange")

def fav_color3(**name_color):
    for name , color in name_color.items():
        print(f"{name} favorite color is {color}")
fav_color3( Andreja="green", Janko = "red", Mitra = "orange")

def greeting(**names):
   if "Andreja" in names and  names["Andreja"] == "special":
       return f"You are special Andreja"
   elif "Kaja" in names:
       return f"{names['Kaja']} Kaja"
   return "Not sure who this is ...."

print(greeting(Andreja = "Zdravo"))
print(greeting(Kaja = "Pozdrav"))
print(greeting(Andreja = "special"))
print(greeting(Kaja = "Pozdrav",Andreja = "special"))

"""

def sum_all_num4(*nums):
    total =0
    for num in nums:
        total += num
    print(total)
sum_all_num4(2,2,2,4)

list_num = [2,2,2,4]
sum_all_num4(*list_num)


names = { "first": "Andreja", "second": "Jovanovski"}
def display_names(first,second):
    return f"{first} say hello to {second}"
print(display_names(**names))



def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = f"{kwargs.get('message', 'The resulti is ')}{float(operation_value)}"
    else:
        final = f"{kwargs.get('message', 'The resulti is ')}{int(operation_value)}"
    return final
print(calculate(make_float=False, operation='add', message='You just added ', first=2, second=4))
print(calculate(make_float=True, operation='divide', first=3.5, second=5))
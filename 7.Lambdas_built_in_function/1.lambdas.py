# normal function

def square(num):
    return num*num
print(square(9))

# lambda
# lambda parameters : body of function


square2=lambda num: num * num
print(square2(5))

addnum=lambda x,y: x+y
print(addnum(3,4))

square3 = (lambda n : n*n)(5)
print(square3)

addnum2=(lambda x,y: x+y)(3,4)
print(addnum2)

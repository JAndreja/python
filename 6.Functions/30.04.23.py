
#######################################################################################################
"""
def sum(a,b):
    return a+b  

def mult(c,d):   
    return c*d   

def sub(a,b):
    return a-b

def sum_of_all(a,b,c,d):
    result = sum(a,b) + mult(c,d)
    return result
print(sum_of_all(2,8,2,5))

def sum_of_all_2(a,b):
    return sum(a,b) +mult(a,b)
print(sum_of_all_2(2,8))

def sum_of_all_3(a,b):  
    return a + b
print(sum_of_all_3(sum(2,8),mult(2,5)))

def sum_of_all_4(fn1 = sum(2,4) , fn2= mult(3,4)):
    return fn1 + fn2
print(sum_of_all_4())

def sum_of_all_5( a,b,c,d ,fn1 = sum , fn2= mult ):
    return fn1(a,b) + fn2(c,d)
print(sum_of_all_5(5,5,5,5))

def sum_of_all_6( a,b ,fn):
     return fn(a,b)
print(sum_of_all_6(5,4,sub))
"""
#####################################################################################

def marks_avg(marks):
    avg = sum(marks)/len(marks)
    return avg
    
def compute_grade(average_marks):
    if average_marks >= 80:
        return "Your grade is: A"
    elif average_marks >= 60:
        return "Your grade is: B"
    elif average_marks >= 50:
        return "Your grade is: C"
    else:
        return "Your grade is: F"

marks = [ 80,85,85,75,95]

avg_marks= marks_avg(marks)
print(f"Average marks is : {avg_marks}")

grade = compute_grade(avg_marks)
print(f"The grade is : {grade}")

##############################################################################################

def marks_avg1(marks):
    avg = sum(marks)/len(marks) 
    return avg
    
def compute_grade1( marks, avg = marks_avg1):
        avg_marks = avg(marks)
        print(f"Average marks is : {avg_marks}")
        if avg_marks >= 80:
            return "Your grade is: A"
        elif avg_marks >= 60:
            return "Your grade is: B"
        elif avg_marks >= 50:
            return "Your grade is: C"
        else:
            return "Your grade is: F"
          
marks = [ 40,50,30,40,68]
print(compute_grade1(marks))

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
    
def compute_grade1( marks, fn_mark_avg = marks_avg1):
        avg_marks = fn_mark_avg(marks)
        print(f"Average marks is : {avg_marks}")
        if avg_marks >= 80:
            return "Your grade is: A"
        elif avg_marks >= 60:
            return "Your grade is: B"
        elif avg_marks >= 50:
            return "Your grade is: C"
        else:
            return "Your grade is: F"
          
marks = [ 80,60,70,89,68]
print(compute_grade1(marks))

#########################################################################################

marks2 = [ 40,40,40,40,40]
def marks_avg2(m):
    avg = sum(m)/len(m) 
    return avg
    
def compute_grade2(fn_mark_avg = marks_avg2(marks2)):
        print(f"Average marks is : {fn_mark_avg}")
        if fn_mark_avg >= 80:
            return "Your grade is: A"
        elif fn_mark_avg >= 60:
            return "Your grade is: B"
        elif fn_mark_avg >= 50:
            return "Your grade is: C"
        else:
            return "Your grade is: F"
          
print(compute_grade2())

#########################################################################################

user_input = input("Enter numbers separated by commas: ")

grades = user_input.split(",")
grades = [ int(grade) for grade in grades]


def marks_avg3(m):
    avg = sum(m)/len(m) 
    return avg
    
def compute_grade3(fn_mark_avg = marks_avg3(grades)):
        print(f"Average marks is : {fn_mark_avg}")
        if fn_mark_avg >= 80:
            return "Your grade is: A"
        elif fn_mark_avg >= 60:
            return "Your grade is: B"
        elif fn_mark_avg >= 50:
            return "Your grade is: C"
        else:
            return "Your grade is: F"
          
print(compute_grade3())

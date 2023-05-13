#number = float(input("Please enter a number: "))

#if number > 0:
#    print(f"The {number} is positive")
#elif number < 0:
#    print(f"The {number} is negative")
#else:
#    print(f"The number is 0")


number = int(input("Pleaase enter the number:"))

for num in range(1,11):
    product = number * num
    print(f"{number} x {num} = {product}")
numbers = input("Enter numbers:")
print(numbers)
print(type(numbers))

num_list = numbers.split(",")
print(num_list)
print(type(num_list))

new_num_list = []
for num in num_list:
    num =int(num)
    new_num_list.append(num)
print(new_num_list)

def sum_nums(nums):
    return sum(nums)
print(sum_nums(new_num_list))
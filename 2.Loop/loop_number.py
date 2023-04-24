# for num in range(1,21):
#     if num % 2 == 0 and num != 4:
#         print(f"{num} is even")
#     elif num % 2 != 0 and num !=13:
#             print(f"{num} is odd") 
#     else:
#         print(f"{num} is unlucky")


for num in range(1,21):
    if num % 2 == 0 and num != 4:
        state="even"
    elif num % 2 != 0 and num !=13:
        state="odd" 
    else:
        state="unlucky"
    print(f"{num} is {state}")
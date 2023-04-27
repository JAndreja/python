nested_list = [ [1,2,3], [4,5,6], [7,8,9] ]

print(nested_list[0][1])
print(nested_list[1][1])
print(nested_list[2][1])

print("--------------------------")
for i in nested_list:
    print(i)
    for val in i:
       print(val)
print("--------------------------")
i=0
while i < len(nested_list):
     print(f"Index {i}: {nested_list[i]}")
     i +=1
print("--------------------------")
i=0
while i < len(nested_list):
     print(f"Index {i}: {nested_list[i]}")
     sub_list=nested_list[i]
     j=0
     while j < len(sub_list):
         print(f"Sub_index {j}: {sub_list[j]}")
         j += 1
     i +=1
print("=====================================")

 # nested list comprehension
print("** Nested list comprehension **" )
nested_num=[[1,3,5],[2,4,6],[7,9,11],[8,10,12]]
[[print(val) for val in i] for i in nested_num]
print("--------------------------")
board = [[num for num in range(1,5)] for val in range(1,4)]
print(board)
print("--------------------------")
print([["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)])
print("--------------------------")
answer=[[num for num in range(0,3)] for val in range(0,3)]
print(answer)
print("--------------------------")
answer=[[num for num in range(0,10)] for val in range(0,10)]
print(answer)
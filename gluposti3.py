list1=[2,3,5,6]
list2=[7,1,4,8]

new_list =[]
for i in range(len(list1)):
    new_list.append([list1[i]])
    for k in list2:
       new_list[i].append(k)
       list2.remove(k)
       break
print(new_list)
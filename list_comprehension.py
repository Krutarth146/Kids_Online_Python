list1 = [10,20,30,40,44,21,31,34]


for i in list1:
    if i % 2 != 0:
        print(i)

list2 = [i for i in list1]
list2 = [i for i in list1 if i % 2 != 0]
print(list2)   # [21, 31]

list3 = [10,90,34,32,21]

for i in list3:
    print(i,i**3)


cube = [i**3 for i in list3]
print(cube)   # [1000, 729000, 39304, 32768, 9261]

square = [i**2 for i in list3]
print(square)   # [100, 8100, 1156, 1024, 441]


square_pair = [(i,i**2) for i in list3]
print(square_pair)   # [(10, 100), (90, 8100), (34, 1156), (32, 1024), (21, 441)]
  

list5 = [[10,20,30], [50,90,89], [34,32,78]]

# [10,20,30,50,90....]

for sublist in list5:
    for ele in sublist:
        print(ele)

list9 = [ele for sublist in list5 for ele in sublist] 
print(list9)  # [10, 20, 30, 50, 90, 89, 34, 32, 78]


list7 = [list5[row][col] for row in range(len(list5)) for col in range(len(list5[row]))]
print(list7)   # [10, 20, 30, 50, 90, 89, 34, 32, 78]


# [(10,10), (10,20), (10,30)....]
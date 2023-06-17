list1 = [10,20,30,0,50,90]

print(list1)
print(type(list1))  # <class 'list'>
print(len(list1))  # 6
print(max(list1))  # 90
print(min(list1))  # 10
print(sum(list1) / len(list1))  # 40.0

print(all(list1))  # False
print(any(list1))  # False

list1.append(900)
list1.append("str1")
print(list1)  # [10, 20, 30, 0, 50, 90, 900, 'str1']

list1.extend([800])
print(list1)  # [10, 20, 30, 0, 50, 90, 900, 'str1', 800]

list1.extend("Rishita")
print(list1)   # [10, 20, 30, 0, 50, 90, 900, 'str1', 800, 'R', 'i', 's', 'h', 'i', 't', 'a']


del list1[3:12]

l3 = [10,20,30,40]
list1.append(l3)
print(list1)   # [10, 20, 30, 'h', 'i', 't', 'a', [10, 20, 30, 40]]

# list1.extend(l3)
# print(list1)   # [10, 20, 30, 'h', 'i', 't', 'a', 10, 20, 30, 40]


list1.insert(4, 90000)
print(list1)   # [10, 20, 30, 'h', 90000, 'i', 't', 'a', [10, 20, 30, 40]]

list1.insert(-1, 800)
print(list1)   # [10, 20, 30, 'h', 90000, 'i', 't', 'a', 800, [10, 20, 30, 40]]

list1[-1] = 678
print(list1)   # [10, 20, 30, 'h', 90000, 'i', 't', 'a', 800, 678]

list1.remove(800)
print(list1)   # [10, 20, 30, 'h', 90000, 'i', 't', 'a', 678]

list1.pop()
print(list1)   # [10, 20, 30, 'h', 90000, 'i', 't', 'a']

list1.pop(2)
print(list1)   # [10, 20, 'h', 90000, 'i', 't', 'a']

l3 += [10,20,30]
print(l3)

l3.sort()
print(l3)   # [10, 10, 20, 20, 30, 30, 40]

# l3.reverse()
# print(l3)   # [40, 30, 30, 20, 20, 10, 10]

l3.sort(reverse=True)
print(l3)   # [40, 30, 30, 20, 20, 10, 10]


print(l3)   # [40, 30, 30, 20, 20, 10, 10]
print(l3.count(20))  # 2
print(l3.index(20))  # 3

# l3.clear()
# print(l3)  # []

l4 = l3.copy()   # Shallow Copy
print(l4)   # Xerox

l6 = l3  # Digilocker  # Deep Copy
print(l6)

l3.append(9089)
print(l3)   # [40, 30, 30, 20, 20, 10, 10, 9089]
print(l4)   # [40, 30, 30, 20, 20, 10, 10]
print(l6)   # [40, 30, 30, 20, 20, 10, 10, 9089]

l3.append(5000)
print(l3)   # [40, 30, 30, 20, 20, 10, 10, 9089, 5000]
print(l6)   # [40, 30, 30, 20, 20, 10, 10, 9089, 5000]




for i in l6:
    print(i)


# for j in range(9):
for j in range(len(l6)):
    # print(j,end=' ')  # 0 1 2 3 4 5 6 7 8
    print(l6[j],end=' ')  # 40 30 30 20 20 10 10 9089 5000

l3 = [[10,20,30], [90,89,32], [23,89]]

for i in l3:   # i= [10, 20, 30]
    for f in i:
        if f % 3 == 0:
            print(f)  # 90
# # Dictionary ----> key-value Pairs  (Ordered (No Index), Don't Allow Duplicates, Mutable)

dict1 = {"Name" : "Krutarth", 'Roll' : 90, 'list1' : [10,20,30,40], 'address' : {'city' : 'Ahmedabad', 'pincode' : [140,230,380]}}

# print(dict1)
# print(dict1['address'])   # {'city': 'Ahmedabad', 'pincode': [140, 230, 380]}
# print(dict1['address']['pincode'])   # [140, 230, 380]
# print(dict1['address']['pincode'][2])   # 380
# print(dict1['address']['pincode'][-1])   # 380


for key in dict1.keys():
    print(key,end=' ')   # keys Name Roll list1 address

print()
print()

for val in dict1.values():
    print(val,end=' ')   # values  Krutarth 90 [10, 20, 30, 40] {'city': 'Ahmedabad', 'pincode': [140, 230, 380]}

print()
print()

for data in dict1.items():
    print(data,end=' ')   # values  ('Name', 'Krutarth') ('Roll', 90) ('list1', [10, 20, 30, 40]) ('address', {'city': 'Ahmedabad', 'pincode': [140, 230, 380]})
print()
print()

for key, val in dict1.items():
    # print(key,end=' ')   # values  ('Name', 'Krutarth') ('Roll', 90) ('list1', [10, 20, 30, 40]) ('address', {'city': 'Ahmedabad', 'pincode': [140, 230, 380]})
    print()
    print()
    if val == 90:
        print(key)
        break


# --------------------------------------------

# from bidict import bidict

# dict1 = {"Name" : "Krutarth", 'Roll' : 90, 'address' : "Shahpur"}
# dict2 = bidict({'Name' : "Manoj"})
# dict3 = bidict(dict1)

# print(dict2,dict3)

# dict2 = dict2.inverse

# print(dict2['Manoj'])   # Name

print(dict1)  # {'Name': 'Krutarth', 'Roll': 90, 'list1': [10, 20, 30, 40], 'address': {'city': 'Ahmedabad', 'pincode': [140, 230, 380]}}
print(dict1.get('Name'))   # Krutarth
print(dict1.get('Name1'))   # None
print(dict1['Name'])   # Krutarth
# print(dict1['Name1'])   # Error


dict1.update({'class' : 7})

print(dict1)

# dict1['std'] = 10
# print(dict1)

print()
print()
dict4 = dict1.copy()  # Shallow Copy
dict5 = dict1  # Deep Copy
dict6 = dict(dict1)  # Shallow Copy

dict5.update({2 : 8})  # 

print(dict4)
print(dict5)
print(dict6)
print(dict1)


dict1.setdefault("Model", 'Alto')
dict1.setdefault("Roll", 3334)
print(dict1)


list1 = [10,20,30,40]
d1 = dict.fromkeys("Aman", 0)
d1 = dict.fromkeys(list1, 0)

print(d1)  # {10: 0, 20: 0, 30: 0, 40: 0}


poped_val = dict1.pop("Name")

print(poped_val)   # Krutarth
print(dict1)   # {'Roll': 90, 'list1': [10, 20, 30, 40], 'address': {'city': 'Ahmedabad', 'pincode': [140, 230, 380]}, 'class': 7, 2: 8, 'Model': 'Alto'}

pop_val1 = dict1.popitem()
print(pop_val1)   # ('Model', 'Alto')
print(dict1)


# --------------------------------------------

str1 = "MISSISSIPI"

ans = {"M" : 1, "I" : 4, "S" : 4, "P" : 1}


dict1 = {}
c =0 

for char in set(str1):
    dict1[char] = str1.count(char)
    c+=1
print(dict1)
print(c) 

dict2 = {}

for i in str1:
    if i not in dict2:
        dict2[i] = 1
    else:
        dict2[i] += 1

print(dict2)


# list1 = [10,90,23,45,67]
# sc = {10 : (100, 1000), .....}
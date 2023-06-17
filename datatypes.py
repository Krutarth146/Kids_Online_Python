list1 = [10, 90.89, 6+89j, True, [1,89], "Nilay"]
print(type(list1))   # <class 'list'>

tup1 = (90, 89.67, False, (12,3))
print(tup1)   # (90, 89.67, False, (12, 3))
print(type(tup1))  # <class 'tuple'>    

str1 = 'D'
str2 = "Krutarth"
print(type(str2))   # <class 'str'>

dict1 = {}
print(type(dict1))  # <class 'dict'>

set1 = set()
print(type(set1))  # <class 'set'>


dict2 = {"Name" : "Nilay", 'Marks' : 45.90, "Address" : "Ahm"}
print(dict2)   # {'Name': 'Nilay', 'Marks': 45.9, 'Address': 'Ahm'}

set2 = {90,89, 67.90, 90}
print(type(set2))  # <class 'set'>
print(set2)  # {89, 90, 67.9}  -> Unique Elements


# Opearators -> 
# Arithmetic -> + - * / // ** % 
# Assignment -> = += -= *= /= //= %= <<= >>= != &= ^=  (Assignment o/p priority Low)

print(~34)   # -35 (Negation)

a = 90
a+=2      # a = a + 2

a*=10    # 920
a//=3     # 306
print(a)   # 306



# i = 1   # Intialization
# while(i<=100)   # Condition
# {
#     printf("%d ",i);  # statements
#     i += 1
# }


# _ = 1
# while _ <= 100:
#     print(_,end=' ')
#     _+=1

# _ = 100
# while _ >= 1:
#     if _ % 5 == 0:
#         print(_,end=' ')
#     _-=1


_ = 99
while _ >= 1:
    if _ % 2 != 0:
        print(_,end=' ')
    _-=2


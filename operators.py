# 23 + 56  -> 23 and 56 is Operand , + is Operator

# 1. Arithmetic O/p  +  -  *  /  //  %  **

print(2**(3**2))  # 512

# 2. Assignment O/p  = += -= *= /= //= %= |= <<= >>= &= ^=


x = 90

x+=1   # x = x + 1 -> 90 + 1  -> x = 91

print(x)

# 3. Membership O/p  in , not in

# list1 = [10, 90, 89, 67, 45]
# need = int(input())

# flag = 0
# for j in list1:
#     if j == need:
#         print(f"{need} is available in the list")
#         flag = 0
#         break
#     else:
#         flag = 1

# if flag == 1:
#     print(f"{need} is Not avalibale")


# if need in list1:
#     print(f"{need} is available in the list")
# else:
#     print(f"{need} is Not avalibale")
  

# 4. Identity O/p     is ,  is not

# x = 90
# y = 90

# if x is y:
#     print("x and y is Equal")  # x and y is Equal

list2 = [45, 90, 89, 78]
list3 = [45, 90, 89, 78]

# if list2 is list3:
#     print("list2 and list3 is Equal")  # x and y is Equal

# print(id(list2))  # 2058807618112
# print(id(list3))  # 2058807554752

# list4 = list2

# if list4 is list2:
#     print("list2 and list4 is Equal")  # list2 and list4 is Equal

list5 = list2.copy()
if list5 is list2:
    print("list2 and list5 is Equal")  # list2 and list4 is Equal
else:
    print("Fail")

print(id(list2))  # 2058807618112
print(id(list5))  # 2058807554752

# 5. Comparison O/p  == < > <= >= !=

# 6. Bitwise O/p  ->     &  !  ^  <<  >>
 

# 7. Logical O/p  ->    and  or  not
num = 40

if num % 5 == 0 and num % 7 == 0 or num % 10 == 0:
    print("Pass")
else:
    print("Fail")


# AND Table  (A * B)

# i/p  i/p  o/p
#  0    0    0
#  0    1    0
#  1    0    0
#  1    1    1



# OR Table  (A + B)

# i/p  i/p  o/p
#  0    0    0
#  0    1    1
#  1    0    1
#  1    1    1


# XOR Table (same - 0)

# i/p  i/p  o/p
#  0    0    0
#  0    1    1
#  1    0    1
#  1    1    0


# Decimal to Binary

# 113 , 9089, 78323, 1187

# Binary to Decimal

# 1101010  11111   1010101

# Deciaml to  HexaDecimal

# 5690   2344

# RIght shift and Left Shift

254 << 2
9900 >> 4

# Datatype -> int , float, str, Bool, complex
# collections - list, tuple, dictionary, set

# Python is Dynamic Programming

x = 0
print(type(x))  # <class 'int'>

y = None
print(type(y))  # <class 'NoneType'>

# Typecasting -> Implicit Typecasting , Explicit Typecasting

x = 90    # int
y = 80.56  # float
print(x+y)  # 170.56   # Implicit Typecasting


_Nilay = True   # -> 1
gid = 34

print(_Nilay + gid)   # 35 # Implicit Typecasting


v = 90
print(float(v))  # 90.0

q = 90.90
print(int(q))   # 90


# import math
from math import ceil, floor

print(ceil(90.01))   # 91
print(floor(90.90))   # 90

# u = "Kru"
# print(int(u))   # Generates Error

f = '30'
print(int(f))   # 30

f = "31"
print(int(f))   # 31

h = "34.89"
print(int(float(h)))   # 34


num1 = 0

if num1 > 0:
    print("Positive")
elif num1 == 0:
    print("Zero")
else:
    print("Negative")

# TAke 3 variables from user and compare it then print Max Number
# Take age as input and check whether he is eligible for voting or not???
# Take one number as input and check whether this num is divisible by 5 and 7 or not???
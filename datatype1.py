# datatype -> int, float, complex, bool

# int x = 90;
# Python is Dynamic Lang.
# AutoDefine

x = 80
print(x)  # 80
print(type(x))   # <class 'int'>

y = 30.98
print(y)
print(type(y))  # <class 'float'>

z = True
print(z)  # True
print(type(z))  # <class 'bool'>

x = 'R'
print(type(x))  # <class 'str'>

f = "RRR"
print(type(f))  # <class 'str'>

w = 90+8j   # -> 90 is Real Part, 8j is Imaginary Part
print(type(w))  # <class 'complex'>

f = 90j
print(w+f)  # 90 + 98j


g = [12, 90.89, True, [23,34], "String"]
print(g)  # [12, 90.89, True, [23, 34], 'String']

print(type(g))  # <class 'list'>

h = (13,45.90, True)
print(type(h)) # <class 'tuple'>

w = {'Name' : "Rishita", 'Age' : 15}
print(type(w))  # <class 'dict'>
print(w)  # {'Name': 'Rishita', 'Age': 15}

f = set()
print(type(f))  # <class 'set'>

f = {12,45,32,67.90}
print(type(f))  # <class 'set'>
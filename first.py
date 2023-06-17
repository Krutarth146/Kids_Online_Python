# printf("Hello World");
# cout<<"Hello World";


# from __future__ import print_function  -> in python 2

# Python version - 3
print("Hello World1",end=' Nilay ')   # \r -> return carriage
print('Hello World2')   # Hello World2


# print("Nilay", 'Gidwani', sep=' ')   # defalut sep = ' '
print("Nilay", 'Gidwani', sep='_ROyal_')   # defalut sep = ' '

# Single Line Comment

'''
Multi
Line
Comment
'''

print('''
priyank Modi
    Hello My name is Priyank Modi
    I lives in Surat
    I am 70 years old.
''')


# priyank Modi
#     Hello My name is Priyank Modi
#     I lives in Surat
#     I am 70 years old.

# printf("Enter your Id: ");
# scanf("%d",&id);

x = 90
print(x)
print(type(x))  # <class 'int'>

_dhiraj_sir = 56
print(_dhiraj_sir)  # 56

Royal = 80.78
print(type(Royal))  # <class 'float'>

h = False
print(type(h))  # <class 'bool'>

w = 's'
print(type(w))   # <class 'str'>

q = "Nilay"
print(type(q))  # <class 'str'>

r = 90 + 8j
print(type(r))  # <class 'complex'> 90 is real Part, 8j is Imaginary Part.

k = 56
print(r+k)    # (146+8j)

t = 78j
print(r+t)  # (90+86j)


x = 90
y = 89
print(x+y)


# raw_input() # py2
eng = input("Enter your eng Marks1: ")  # py3   # default str
maths = input("Enter your maths Marks1: ")

print(int(eng) + int(maths))  # 60 Explicit Type conversion  # 60
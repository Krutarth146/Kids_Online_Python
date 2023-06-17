# i = 0
# while i<=100:
#     print(i)
#     i+=1


# for j in range(10):   # 0 to 9  -> By default 0 is start Point
#     print(j,end=' ')
# print()
# for j in range(1,11):   # 0 to 9
#     print(j,end=' ')


# for _ in range(25,101):
#     if _ % 2 != 0:
#         print(_)

# for _ in range(25,101,1):   # (start , end (n-1) , Step (n-1))
#     # if _ % 2 != 0:
#     print(_)

# for _ in range(25,101,2):   # (start , end (n-1) , Step (n-1))
#     # if _ % 2 != 0:
#     print(_)

for _ in range(101,25,-3):   # (start , end (n-1) , Step (n-1))
    # if _ % 2 != 0:
    print(_)

# Table
# 5 * 1 = 5
# Power of any Number
# Factorial

# Fibonacci Series

# 0 1 1 2 3 5 ......

step = int(input("Enter Total No. of steps: "))

n1 = 0
n2 = 1
print(n1,n2,end=' ')
for i in range(step-2):
    n3 = n1 + n2  # 3
    print(n3,end=' ')   # 0 1 1 2 3
    n1 = n2   # n1 = 1
    n2 = n3   # n2 = 2
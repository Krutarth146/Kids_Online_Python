l1 = [10,20,30,40,50]

for i in l1:
    print(i,end=' ')  # 10 20 30 40 50

for j in range(0,len(l1)):
    print(l1[j])

l1= [[10,20,30], 
     [40,50,60], 
     [70,80,90]]

for sublist in l1:
    print(sublist)

# [10, 20, 30]
# [40, 50, 60]
# [70, 80, 90]

l1= [[10,20,30], 
     [40,51,60], 
     [71,80,90]]
sum = 0

for sublist in l1:
    for element in sublist:
        if element % 2 != 0:
            print(element)
            sum += element

print(sum)  # 122

l1= [[10,20,30], 
     [40,51,60], 
     [71,80,90]]

for row in range(len(l1)):
    if row % 2 == 0:
        for col in range(len(l1[row])):
            print(l1[row][col],end=' ') 
    else:
        for col in range(len(l1[row])-1,-1,-1):
            print(l1[row][col],end=' ')

    print()

# 10 20 30
# 40 51 60
# 71 80 90
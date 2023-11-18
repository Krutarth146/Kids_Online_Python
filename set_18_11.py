set1 = {10, 23.23, True, "Str1", (10,20,10), 10, 10}   # Unordered (No Indexing), Doulicates Not Allowed, Unchangeble (But we can add or remove elements)

print(set1)   # {True, 'Str1', (10, 20, 10), 23.23, 10}


set2 = set()

print(type(set2))   # <class 'set'>


set1 = {10,20,30,40}
set2 = {40,50,60}

print(id(set1))

set1.update({12,204})   # {20, 40, 10, 204, 12, 30}
print(id(set1))

print(set1)


set1.remove(40)
print(set1)   # {20, 10, 204, 12, 30}


print(set1.pop())   # 20
print(set1)   # {10, 204, 12, 30}


set1.add(400)
print(set1)



# ------------------------------------
set1 = {10,20,30,40}
set2 = {40,50,60}

print(set1.difference(set2))   # {10,20,30}


# set1.difference_update(set2)
# print(set1)  # {10,20,30}

# print(set1.intersection(set2))   # {40}


# set1.intersection_update(set2)

# print(set1)   # {40}

# set1.discard(40)

# print(set1)   # set()

# print(set1.symmetric_difference(set2))  # {10, 50, 20, 60, 30}

set1 = {10,20,30,40}
set2 = {90,50,60,10,20,30,40}

# print(set1.isdisjoint(set2))   #  True
print(set1.issubset(set2))  # True
print(set2.issuperset(set1))   # True


S = "the big dwarf only jumps"

s1 = set(S)
print(s1)


f = "The quick brown fox jumps over the lazy dog"
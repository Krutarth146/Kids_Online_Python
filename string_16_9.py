str1 = 'Manoj is Good Boy123.'



str2 = "Ståle"
print(str2.encode())
print(str2.encode(encoding="ASCII",errors='backslashreplace'))
print(str2.encode(encoding="ASCII",errors='namereplace'))
print(str2.encode(encoding="ASCII",errors='replace'))
print(str2.encode(encoding="ASCII",errors='ignore'))
print(str2.encode(encoding="ASCII",errors='xmlcharrefreplace'))


print(str2.endswith('e'))   # True
print(str2.startswith('St'))   # True

str3 = 'Rishita\tBasera'
print(str3)
print(str3.expandtabs(16))
print(str3.expandtabs(32))


name = 'Rishita'
rs = 9000
print('{} has {} Rs. only.'.format(name, rs))
print('{} has {} Rs. only.'.format("Aman", 333))
print('{1} has {0} Rs. only.'.format("Aman", 333))
print('{name} has {rs} Rs. only.'.format(name = "Aman", rs = 333))


print('%s is Good'%'Rishita')
print('%.2f is Good'%344.90)

dict1 = {'Name' : 'Aman', 'Rs' : 800}
print('{Name} has {Rs} Rs. only.'.format_map(dict1))

name = 'Rishita'
# print(name.find('z'))  # -1
# print(name.index('z'))  # Error


for k in range(len(name)):
    if name[k] == 'i':
        print(k, name[k])


print(str3.rfind('i'))  # 4

str3 = "Rishita is good_girl"
print(str3.isalnum())
print(str3.isalpha())
print(str3.isnumeric())
print(str3.isdigit())
print(str3.isdecimal())
print(str3.isascii())
print(str3.isprintable())
print(str3.isidentifier())
print(str3.isspace())
print(str3.title())   # Rishita Is Good_Girl
print(str3.istitle())  # False


str2 = 'Royal_is Best Institute Ever123.'

# print(''.join(str2))
# print(' '.join(str2))
# print('_'.join(str2))
# print(str3.join(str2))
# print(str2.join(str3))


list1 = str2.split()  # space
# list1 = str2.split('_')
list1 = str2.split('R')
print(list1)   # ['', 'oyal_is Best Institute Ever123.']
print(str2.partition(' '))   # ('Royal_is', ' ', 'Best Institute Ever123.')
print(str2.partition('e'))   # ('Royal_is B', 'e', 'st Institute Ever123.')
print(str2.rpartition('e'))   # ('Royal_is Best Institute Ev', 'e', 'r123.')

list1 = str2.split()   
print(list1)  # ['Royal_is', 'Best', 'Institute', 'Ever123.']

list1[1] = 'Very Best'

print(' '.join(list1))   # Royal_is Very Best Institute Ever123.
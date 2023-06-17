dict1 = {"Name" : "Krutarth", 'ROll' : 900}

print(dict1.keys())

dict1['ROll'] = 5000
print(dict1)   # {'Name': 'Krutarth', 'ROll': 5000}

# ----------------------------------------

records = {
    '1001' : {'pName' : "kellogs", 'qn' : 901, 'price' : 50},
    '1002' : {'pName' : "5-star", 'qn' : 250, 'price' : 20},
    '1003' : {'pName' : "Parle G", 'qn' : 400, 'price' : 5},
    '1004' : {'pName' : "Oats", 'qn' : 68, 'price' : 30}
}

print(type(records))  # <class 'dict'>

print(records['1003']['qn'])   # 400

print("---------------------Menu----------------------")

for i in records:
    print(records[i]['pName'],"||",records[i]['qn'],'||',records[i]['price'])


user_need = input("Enter Product Id: ")
quantity = int(input("Enter QUantity: "))

if quantity <= 0:
    print("Pls ENter Valid Quantity")
    exit()

total_bill = 0
if quantity <= records[user_need]['qn']:
    records[user_need]['qn'] -= quantity
    total_bill = quantity * records[user_need]['price']
    print("Total Bill Amount is",total_bill)
    print("Thank You Visit Again!")
else:
    print(f"We have only {records[user_need]['qn']} quantities.")
    res = input("if u need these then Press Y or y: ")
    if res.lower() == "y":
        records[user_need][quantity] = 0
        total_bill = records[user_need]['qn'] * records[user_need]['price']
        print("Total Bill Amount is",total_bill)
        print("Thank You Visit Again!")
    else:
        print("Thank You Visit Again!")
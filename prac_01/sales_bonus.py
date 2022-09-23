"""1. Sales Bonus

get sales
while sales >= 0
    if sales < 1000
        bonus = sales * 0.1
        print bonus
        get sales
    else if sales >= 1000
        bonus = sales * 0.15
        print bonus
        get sales
print Invalid message
"""
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print(bonus)
    sales = float(input("Enter sales: $"))
print("Invalid")

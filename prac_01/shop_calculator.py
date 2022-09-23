""" Shop Calculator

total = 0
get number_of_items
while number_of_items < 0
    print Invalid message
    get number_of_items
for each number_of_items
     get price_of_item
    total += price_of_item
if total > 100
    discount = total * 0.1
    total -= discount
print total of number_of_items

"""
total = 0
number_of_items = int(input("Number_of_items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number_of_items: "))
for i in range(1, number_of_items + 1):
    price_of_item = float(input("Price of item: "))
    total += price_of_item
if total > 100:
    discount = total * 0.1
    total -= discount
print(f"Total price for {number_of_items} items is ${total:.2f}")



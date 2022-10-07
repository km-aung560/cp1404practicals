""" Basic List Operations """

MAXIMUM_NUMBERS = 5
numbers = [5, 20, 1, 2, 3]
# for i in range(MAXIMUM_NUMBERS):
#     number = int(input("Number: "))
#     numbers.append(number)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[MAXIMUM_NUMBERS - 1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

""" Woefully inadequate security checker """

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Username: ")
if username in usernames:
    print("Access Granted")
else:
    print("Access Denied")






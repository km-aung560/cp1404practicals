""" Files Questions """

# Question 1
name = input("Name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# Question 2
in_file = open("name.txt", "r")
for line in in_file:
    print(line)
in_file.close()

# Question 3
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

# Question 4
total = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)



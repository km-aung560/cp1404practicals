# number_of_stars = int(input("Number of stars: "))
# for i in range(1, number_of_stars + 1):
#     print("*" * i)
# print()

# x = 10
# while x > 4:
#     print(x, end=" ")
#     x = x - 2

# for i in range(1, 10, 4):
#     print(i, i * 2, end=" ")

# x = 5
# for i in range(x):
#     x = x + i
#     print(x, end=" ")

"""
0, 1, 2, 3, 4

1. 5 + 0 = 5
2. 5 + 1 = 6
3. 5 + 


"""
# girls = 0
# boys = 0
# children = girls + boys
# girls = 15
# boys = 12
# print(girls, boys, children)

nums1 = [1, -5, 2, 0, 4, 2, -3]
nums2 = [1, -5, 2, 4, 4, 2, 7]
result = 0
j = 0
while j < len(nums1):
    if nums1[j] != nums2[j]:
        result = result + 1
    j = j + 1
print(j)

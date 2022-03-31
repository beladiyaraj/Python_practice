# Tuple

# <------------------------Github Link------------------------>
# https://github.com/rajbeladiya4/PIP-Practical-2.git

# a. Write a Python program to create a tuple with different data types.
tuple1 = ('Raj', 3, 3.03, {'a': '100', 'b': '200'}, {1, 2, 3, 4})
j = 0
for i in tuple1:
    print(type(tuple1[j]))
    j = j+1

# b. Write a Python program to create a tuple with numbers and print one item.
'''num = 0
tuple1 = ()
while True:
    i = input("Enter text Number(Press enter to exit): ")
    if not i:
        break
    tuple1 = tuple1+(i,)
print(tuple1)'''

# c. Write a Python program to add an item in a tuple.
'''tuple1 = (1, 2, 3, 4, 5, 6, 7)
tuple1 = tuple1+(8,)
print(tuple1)'''

# d. Write a Python program to convert a tuple to a string
'''str1 = ''
tuple1 = ('R', 'A', 'J')
for item in tuple1:
    str1 = str1+item
print(str1)'''

# Write a Python program to find the length of a tuple.
'''i = 0
tuple1 = ('a', 'b', 'c', 3.33)
for item in tuple1:
    i = i+1
print("Nuber of Elements in tuple is:", i)'''

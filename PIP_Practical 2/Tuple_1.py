# a. Write a Python program to create a tuple with different data types.
tuple1 = ('Raj', 3, 3.03, {'a': '100', 'b': '200'}, {1, 2, 3, 4})
j = 0
for i in tuple1:
    print(type(tuple1[j]))
    j = j+1

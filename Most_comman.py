# (E) Write a Python program to find the most common elements and their counts from list, tuple, dictionary.

# **** For List *****
List = [1, 2, 3, 2, 1, 3]
counter = 0
num = List[0]
for i in List:
    curr_frequency = List.count(i)
    if (curr_frequency > counter):
        counter = curr_frequency
        num = i

print("For List:", List)
print("     Most common elements is : ", num)
print("     Most repeted number is: ", counter)

# **** For Tuple *****
tuple = (1, 2, 4, 5, 6, 6, 3, 6, 8, 3, 6)
L = list(tuple)
count = 0
num1 = L[0]
for i in L:
    curr_frequency = L.count(i)
    if(curr_frequency > count):
        count = curr_frequency
        num1 = i
print("For Tuple-", tuple)
print("     Number which is repeted most: ", num1)
print("     Most repeted number is: ", count)


# **** For Dictionary *****
dic = {
    1: '100',
    2: '200',
    3: '200',
    4: '400',
    5: '400',
    6: '500'
}
value = dic.values()
l1 = list(value)
count = 0
name = list(l1[0])
for i in l1:
    curr_frequency = l1.count(i)
    if(curr_frequency > count):
        count = curr_frequency
        name = i
print("For Dictionary-", dic)
print("     Name which is repeted most: ", name)
print("     Most repeted name is: ", count)

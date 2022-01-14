# Dictionary

# a. Write a Python script to check whether a given key already exists in a dictionary.
def checkKey(dict1, key):

    if key in dict1.keys():
        print("key", key, "is Present and the value is:", dict1[key], ".")
    else:
        print("key", key, "is not Present.")


dict1 = {'a': 100, 'b': 200, 'c': 300}

key = 'a'
checkKey(dict1, key)

key = 'w'
checkKey(dict1, key)

# b. Write a Python script to merge two Python dictionaries.
'''dict1 = {
    'a': 100,
    'b': 200
}

dict2 = {
    'c': 300,
    'd': 400
}

print(dict1 | dict2)'''

# c. Write a Python program to sum all the items in a dictionary.
'''k = 0

dict1 = {
    'a': 100,
    'b': 200,
    'c': 300,
    'd': 400
}

for i in dict1:
    k = k+1

print(k)'''

# d. Write a Python script to add a key to a dictionary.
# Sample Dictionary: {0: 10, 1: 20}
# Expected Result: {0: 10, 1: 20, 2: 30}
'''dict1 = {
    0: 10,
    1: 20
}
dict1[2] = 30
print(dict1)'''

# e. Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary:
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# Expected Result: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

# dict4= dict(dict1.items()+dict2.items()+dict3.items())
dict4 = dict(dict1)
dict4.update(dict2)
dict4.update(dict3)

print(dict4)'''

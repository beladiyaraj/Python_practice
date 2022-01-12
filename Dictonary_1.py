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

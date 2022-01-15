# Set

# a. Write a Python program to add member(s) in a set and clear a set
newset = set()
while True:
    i = input("Enter anything(Press enter to exit): ")
    if not i:
        break
    newset.add(i)
print(newset)

# b. Write a Python program to remove an item from a set if it is present in the set.
'''set = {1, 2, 3, 4}
print("Original set is:", set)
set.discard(1)
print("After discarding 1 new set is:", set)
set.discard(6)
print("After discarding 2 new set is:", set)'''

# c. Write a Python program to create an intersection, Union, difference of sets.
'''set1 = {'a', 'b', 'c', 'd', 'e'}
set2 = {'b', 'c'}

# union
print("Union of Set1 and Set2 is:", set1 | set2)

# intersection
print("Intersection of Set1 and Set2 is:", set1 & set2)

# difference
print("Difference of Set1 and Set2 is:", set1 - set2)'''

# d. Write a Python program to find maximum and the minimum value in a set.
'''set = {1, 2, 3, 4}
maxval = max(set)
minval = min(set)
print("Maximum value in set is:", maxval)
print("Minimum value in set is:", minval)'''

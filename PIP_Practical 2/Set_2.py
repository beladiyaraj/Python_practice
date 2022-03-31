# b. Write a Python program to remove an item from a set if it is present in the set.

set = {1, 2, 3, 4}
print("Original set is:", set)
set.discard(1)
print("After discarding 1 new set is:", set)
set.discard(6)
print("After discarding 2 new set is:", set)

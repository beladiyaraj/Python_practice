# a. Write a Python program to add member(s) in a set and clear a set
newset = set()
while True:
    i = input("Enter anything(Press enter to exit): ")
    if not i:
        break
    newset.add(i)
print(newset)
num = 0
tuple1 = ()
while True:
    i = input("Enter text Number(Press enter to exit): ")
    if not i:
        break
    tuple1 = tuple1+(i,)
print(tuple1)

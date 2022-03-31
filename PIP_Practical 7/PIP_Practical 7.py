# Aim
#
# Lapindrome is defined as a string which when split in the middle, gives two halves having the same
# characters and same frequency of each character. If there are odd number of characters in the string,
# we ignore the middle character and check for lapindrome. For example gaga is a lapindrome, since the two
# halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few
# examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves contain the same charact-
# ers but their frequencies do not match. Your task is simple. Given a string, you need to tell if it is a
# lapindrome.

# 20CE003_RAJ BELADIYA
# https://github.com/rajbeladiya4/PIP-Practical.git

num = int(input())
lap = []
list1 = []
list2 = []
for i in range(num):
    string = input()
    lap.append(string)
    length = len(string)
    if length % 2 == 0:
        list1.append(string[0:int((length/2))])
        list2.append(string[int(length/2):int(length)])
    else:
        list1.append(string[0:int((length / 2))])
        list2.append(string[int(length / 2)+1:int(length)])

for i in range(num):
    list1[i] = sorted(list1[i])
    list2[i] = sorted(list2[i])
    if list1[i] == list2[i]:
        print('YES')
    else:
        print('NO')

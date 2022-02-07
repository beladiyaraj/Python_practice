# You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.
# 20CE003_RAJ BELADIYA
# https://github.com/rajbeladiya4/PIP-Practical.git

no = int(input())
str_arr = []
for i in range(no):
    item = input()
    str_arr.append(item)
set1 = set(str_arr)
print(len(set1))

str_arr2 = []
str_arr3 = []
for i in str_arr:
    if i in str_arr2:
        pass
    else:
        str_arr2.append(i)
        str_arr3.append(str_arr.count(i))

for j in str_arr3:
    print(j, end=' ')

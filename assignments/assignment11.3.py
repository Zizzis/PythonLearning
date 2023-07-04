import re
hand = open('regex_sum_1832040.txt')
numlist = list()
for line in hand:
    nums = re.findall ('[0-9]+', line)
    for num in nums:
        szam = int(num)
        numlist.append(szam)
sum = 0
for szam in numlist:
    sum = sum + szam
print(sum)

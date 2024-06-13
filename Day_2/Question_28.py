# 28. find the frequnecy of word

name = input('Enter the string: ')
# dct = {}
# dct = name
#
# # count = 0
# # for i in dct:
# #     count += 1
# for i in dct:
#     count = dct.count(i)
#     output =  str(count).s

from collections import Counter

print(Counter(name))

freq = {}
for word in freq:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1


# find the common char in two string

name1 = 'the world is bad and good as well as'
name2 = 'this string has alot of letters'

result = list(set(name1)&set(name2))
for i in result:
    print(i, end=' ')

print(result)
# for _ in name1:
#     for i in name2:
#         if _ == i and _ in i:
#             print(_,end='')
#             break
#
# print(set(name))
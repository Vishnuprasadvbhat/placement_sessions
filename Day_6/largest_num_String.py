# return the numbers in the string
# s = 'abcc123xys'

# n  = ''
#
# for i in s:
#     if i.isdigit():
#         n= n+i
# print(int(n))

# string contains many numbers return largest number

s= 'a30b40bn345'
lst = []
numbers= ''
for i in s:
    if i.isdigit():
        numbers = numbers + i
    else :
        lst.append(i)
        numbers= ''
print(numbers)
print(lst)
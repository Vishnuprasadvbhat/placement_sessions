#print the longest string in the list

# string_ = ['apple', 'elephant', 'hanuman', 'mango']
# lenght = 0

# for i in string_:
#     str=len(i)
#     if str>lenght:
#         lenght = str
#         string = i
# print(string)

#print the string highest count of spcl characters
strings = ['!@#$$ant','************aple', ')(**&&^^123']
spcl_char = 0
length = 0

    #find spcl Char in string
for i in strings:
    spcl = 0
    if not i.isalnum() and not  i.isspace():
     spcl = spcl + 1

if spcl >spcl_char:
    spcl_char =spcl
    str = i

print(str)





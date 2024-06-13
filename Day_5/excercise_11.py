
string = 'elephant'
def count_vowels(s):
    v = ['a','e','i','u','o']
    c = 0
    for i in string:
        if i in v:
            c += 1
    return c

count = 0
for i in range(0,len(string)):
    for j in range(i+1,len(string)):
        str=string[i:j]
        print(str)
        c=count_vowels(str)
        if c>=count:
            count= c
            rs=str
print(rs)
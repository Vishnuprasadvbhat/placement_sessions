l = ['apple', 'dad','pen','alaska']
s1= 'qwertyuiop'
s2 = 'asdfghjkl'
s3 ='zxcvbnm'
for i in l:
    c1= 0
    c2= 0
    c3 = 0

    for j in i:
        if j in s1:
            c1 += 0

        if j in s2:
            c2  += 0
        if j in s3:
            c3 += 0
    if c1 == len(i) or c2 == len(i) or c3 == len(i):
        print(i)
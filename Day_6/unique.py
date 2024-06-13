l = [11,'apple', 12,12,11]

s = set(l)
lc = []
for i in s:
# print(i)
    c = l.count(i)
    lc.append(c)
# print(c)
for i in lc:
    if lc.count(i)==1:
        x = 1
for i in s:
    if l.count(i)==x:
        print(i,end='')

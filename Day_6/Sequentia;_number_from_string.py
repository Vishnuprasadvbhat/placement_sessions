s = "1a2b4c3"
hash = set()
lst = []
for i in s:
    if i.isdigit():
        lst.append(i)

print(lst)
lst = sorted(lst)
print(lst)
for i in lst:
    hash.add(i)
print(hash)
numbers = ''.join(hash)
print(numbers)
b = True


for i in numbers:
    x = i%10
    x= x//10
    while x:
        y = x%10
        if x-y==1:
            x=y
        else:
            b =False
if b:
    print(x)
else:
    print(False)



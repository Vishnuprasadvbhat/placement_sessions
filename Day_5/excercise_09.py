#1. Check for the type
#2. Check for the min

lst = [25.8,'abc', '31', 40,18,19,'egg',48,39,'xyz',37,'apple',29.58, 2,11]
numbers= []
for i in lst:
    if type(i) == int:
        numbers.append(i)

print(numbers)

prime = []
for i in numbers:
    c = 0
    for j in range(2,i//2):
        if i%j==0:
            c += 1
    if c ==0:
        prime.append(i)
print(prime)
z= []
max = max(prime)
min =min(prime)
for i in range(min,max//2):
    if max%i==0 and i in prime:
        z.append(i)

print(z)











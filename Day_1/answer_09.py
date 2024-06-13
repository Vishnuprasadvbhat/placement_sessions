# Write a function that takes list of numbers returns its average.

numbers = map(int,input('Enter the numbers: ').split())
num = []
count = 0
for i in numbers:
    num.append(i)
    count +=1

print(num)
# print(round(sum(num)/count)

output = sum(num)/count
print(output)
output1 = sum(num)//count # floor division
print(output1)
import math
print(math.floor(output))


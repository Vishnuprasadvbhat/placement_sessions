# Q. Program to count the number of even numbers in given list

numbers = [1,2,3,4,5,6]
even = []
for i in numbers:
    if i%2==0:
        even.append(i)

print(even)
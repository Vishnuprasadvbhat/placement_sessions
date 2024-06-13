num =int(input('Enter The number: '))

first = 0
second = 1
for i in range(num+1):
    print(first)
    first,second = second, first + second

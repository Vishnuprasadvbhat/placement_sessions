#Check whether given number is odd or even

numbers = int(input('Enter the number:'))
if numbers & 1: #returns 0 or 1 it will return 0 when it is even
    print(False)


#
# num = [i for i in range(0,numbers%2)]
# print(num)
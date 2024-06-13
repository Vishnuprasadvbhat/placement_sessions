# 10. write a program ot calculate the factorial of given number.
"""10. write a program ot calculate the factorial of given number.
10. write a program ot calculate the factorial of given number.
10. write a program ot calculate the factorial of given number. """

def factorial(num):
    if num ==0:
        return 0
    elif num ==1:
        return 1
    else:
        return print(factorial(num*num-1))

num =int(input('Enter the number: '))
factorial(num)
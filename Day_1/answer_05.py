for i in range (1,101):
    if i%3==0 and i%5==0:
        print('Fizz Buzz: ',i)
    if i%3 == 0:
        print('Fizz: ', i)
    if i%5==0:
        print('Buzz: ', i)
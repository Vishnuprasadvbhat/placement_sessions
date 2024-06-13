#if the height of the boy is lesser than 3

age,height = map(int,input('Enter your Age and Height: ').split())

if height < 3:
    print('Cannot Read')
else:
    if age > 18:
        print('Pay 500')
    elif  age < 12:
        print('Pay 150')
    elif age>12 and age<18:
        print("Pay 250")
    else:
        print('Pay 350')

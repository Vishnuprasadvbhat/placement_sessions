#Check whether the given number is sequential digit number

number = int(input('Enter the number: '))
x = number%10
number= number//10
b =True
while number:
    y= number%10
    if x-y==1:
        x=y
    else:
        b= False
        break
    number=number//10

if b:
    print(True)
else:
    print(False)
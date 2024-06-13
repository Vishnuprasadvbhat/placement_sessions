
# password = input("Enter your password")

password = 'AaEGDFSERT1'

digit = 0
# spl_character = ['!','@','#','$','%','^','&','*','(',')','_']

len = len(password)
upper_count = 0
lower_count = 0
if len < 8:
    for i in password:
        if i.islower():
            lower_count +=1

        if i.isupper():
            upper_count +=1

        if i.isdigit():
            digit += 1
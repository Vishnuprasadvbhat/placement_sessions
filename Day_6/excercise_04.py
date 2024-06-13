password = 'jkjkj'
print(password[0])

if password[0].isdigit():
    print('digit not allaowed')

spc = ['_','.']
for i in password:
    if i in spc:
        continue
    if i.startswith(0):




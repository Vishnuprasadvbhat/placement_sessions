import re

string = 'hello world1234'

result = re.findall('[0-9]',string)
if result == None:
    print('yes')
else:
    print(result)
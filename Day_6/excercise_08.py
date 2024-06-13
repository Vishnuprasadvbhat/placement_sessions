string = 'abc123xyz@gmail.com'

user_id = string[:-10:]

print(user_id)
def check_user_id(user_id):
    spcl = ['_', '.']
    s = 0
    while (user_id[0]!=spcl):
        for i in user_id:
            if i.upper():
                s += 1
            if
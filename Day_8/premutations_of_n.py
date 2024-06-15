def FindPerm(res,string):
    if len(string) == 0:
        print(res)
        return
    for char in range(len(string)):
        rember_char = char
        remaining_char = string[:char]+ string[char+1:]
        FindPerm(res+rember_char,remaining_char)


str= "DOG"
FindPerm('',str)
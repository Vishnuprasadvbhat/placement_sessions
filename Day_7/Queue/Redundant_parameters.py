# string = '(a+b) + (a+b)'
# valid = [')']
# valid_count = 0
# list = []
# for i in string:
#     if i == ')':
#         valid_count += 1
#         list.append(i)
#     if i =='(':
#         valid_count -= 1
#
# if valid_count > 1:
#     print('Invlaid ')
# else:
#     print("Valid")


def FindValid(expression):
    stack = []
    for i in expression:
        if i != '(':
            countChar = 0
            PreviousChar = stack.pop()
            while(PreviousChar!='('):
                countChar += 1
                PreviousChar = stack.pop()
            if countChar <= 1:
                return True
            else:
                stack.append(i)
        else:
            return False

print(FindValid("((a+b))"))

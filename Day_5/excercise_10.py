string = 'This cat is not a dog this dog not a cat but a dog so it is a dog not a cat'
count_cat = 0
count_dog = 0
for i in string.split():
    print(i, end=' \n')
    if i == 'cat':
        count_cat += 1
    if i == 'dog':
        count_dog += 1


print(count_dog)
print(count_cat)
if count_dog == count_cat:
    print(True)
else:
    print(False)
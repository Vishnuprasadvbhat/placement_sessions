# Count of words in the sentences
name = 'This is a sentence'

name.split()

count = 0

for i in name.split():
    if i in name:
        count += 1

        print( i, end= ' ')
print(count)

# love calculator

# names = map(str,input('Please enter your name and your girlfriends name:  ').split())
names='Abhishek Abdul'
count1 = 0
count2 = 0

word1 = 'true'
word2 = 'love'

for i in names:
    if i in word1:
        count1 += 1

for i in names:
    if i in word2:
        count2 += 1


c1 =max(str(count1))
c2 = max(str(count2))

print(f' {c1+c2}%')




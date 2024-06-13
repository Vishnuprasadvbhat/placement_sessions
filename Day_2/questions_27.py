# program for Create pyramid patterns
n = 5
for i in range(1, n+1):
    for j in range(n-i):
        print(' ')
    for k in range(1,2*i):
        print('*',end='')
import random

p1 = int(input("enter 1: "))
p2 = int(input("enter 2: "))

while(p1):
    die_score = random.randint(1,6)
    # print(die_score)
    score = 0
    # count = 0
    score = score + die_score
    if score == 2:
        score= score + 14
    if score == 48:
        score = score - 40
    if score == 50:
        print(score)
        break
# find the most frequently

sent = "fail again and try fail again and try"

sent = sent.split()
count = 0
dict ={}
for i in sent:
    if i in  sent:
     dict[i] = 1
     count += 1
    if i in  sent:
        dict[i] +=1
        count += 1
print(dict)

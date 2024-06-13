# Write a program to print armstrong number from user given range
import math
start=0
end = 1200
# count = []
while (start<=end):
    length = len(str(start))
    # print(length)
    for i in str(start):
        object = math.pow(int(i),int(length))
    object= round(object)
    if object == start:
        print(object)
    start += 1
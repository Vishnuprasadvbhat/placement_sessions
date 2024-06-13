# # Program to find most frequent
# # element in a list
#
# def most_frequent(List):
#     counter = 0
#     num = List[0]
#
#     for i in List:
#         curr_frequency = List.count(i)
#         if (curr_frequency > counter):
#             counter = curr_frequency
#             num = i
#
#     return num
#
#
# List = [2, 1, 2, 2, 1, 3]
# print(most_frequent(List))


l = []
s= set()
lc = []
for i in s:
    c= l.count(i)
    lc.append(c)
sc = set(lc)


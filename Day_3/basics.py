#List operations 

# my_list = [1,2,22,2,2,3,4]
# print(my_list.count(2))

#duplicates in the list 
numbers= [1,2,3,4,4,5,7,5,6]

for i in range(len(numbers)):
  for j in range (i+1, len(numbers)):
    if numbers[i] == numbers[j]:
      print(numbers[i], 'is a Duplicate ')
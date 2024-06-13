# # 1.area of triangle
# # length = int(input('Enter The length: '))
# # height = int(input())
# # breadth = int(input())
# # area= length + height + breadth
# # print(area)
#
# # 2. Solve Quadratic
#
#
#
# # 3.Generate random number
# import random
# random = random.randint(1,10)
# print(random)
#
# #prgram to check even or odd
#
# n = int(input())
# if n%2==0:
#     print('even')
# else:
#     print('Odd')
#
#prgm to check if a Number is positive or Negative
# numbers = int(input())
# if numbers == 0:
#     print(0)
# elif numbers >=1:
#     print('Positive')
# else:
#     print('Negative')
#
# # prgm to get Factorial of a number:
#
# def fac(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return n*fac(n-1)
# print(fac(6))

#prgm to get armstrong number

# integer = int(input('Enter '))
# parts= [int(i) for i in str(integer)]
# count = 0
# for _ in parts:
#     count += _**3
# if count==integer:
#     print('yes')
# else:
#     print('No')

# sum of N-numbers
# def n_sum(num):
#     return print((num*(num+1))//2)
#
# n_sum(10)

#prgm to lcm

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(x,y):
    lcm1 =abs(x*y)//gcd(x,y)
    return lcm1


lcm(12,24)
gcd(48,60)


#prgm to find LCM
# a = [[2,3,4,5]]
# b = [[2,3,4,5]]
#
# print(a)


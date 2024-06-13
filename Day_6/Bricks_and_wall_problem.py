#Check whether with the given number of large and small bricks can we construct a wall of given length

large_b = 3
small_b =5
wall =28

req_large_bricks = wall//5
req_small_bricks = wall//3
print(req_small_bricks)
print(req_large_bricks)
x = min(large_b,req_large_bricks)

wall_using_large_bricks = x * 5

remaining_length = wall - wall_using_large_bricks

if remaining_length <= req_small_bricks:
    print('Possible')
else:
    print('Not possible')

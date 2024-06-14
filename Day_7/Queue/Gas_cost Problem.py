gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
totalGas= 0
currGas = 0
start = 0

for i in range(5):
    totalGas += gas[i] - cost[i]
    currGas += gas[i]-cost[i]
    if currGas<0:
        start = i+1
        currGas = 0
print(start if currGas>0 else -1)
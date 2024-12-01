leftList = []
rightList = []

with open("Day1/Input.txt", 'r') as file:
    for line in file.readlines():
        (leftNum, rightNum) = line.strip().split('   ')
        leftList.append(int(leftNum))
        rightList.append(int(rightNum))

sortedLeft = sorted(leftList)
sortedRight = sorted(rightList)

sumDiff = 0
for leftNum, rightNum in zip(sortedLeft, sortedRight):
    sumDiff += abs(leftNum - rightNum)
    
print(f'Puzzle 1 : {sumDiff}')

sumSim = 0
for leftNum in leftList:
    numSim = 0
    for rightNum in rightList:
        if leftNum == rightNum:
            numSim += 1
    sumSim += numSim * leftNum
    
print(f'Puzzle 1 : {sumSim}')
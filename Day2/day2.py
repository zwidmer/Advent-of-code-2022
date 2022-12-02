# 1 Rock, 2 paper, 3 scissors
# A         B       C
# X         Y       Z
import re

file1 = open('input2.txt', 'r')
text = file1.read()
text = re.sub(r'A|X', '1', text)
text = re.sub(r'B|Y', '2', text)
text = re.sub(r'C|Z', '3', text)

Lines = text.split('\n')
myTotalPoints = 0
for line in Lines:
    line.strip()
    if(line==''):
        continue
    opponent = int(line[:1])
    myChoice = int(line[-1:])
    if(opponent == myChoice):
        myTotalPoints= myTotalPoints + 3 + myChoice
        continue
    if(opponent > myChoice):
        if(opponent == 3 and myChoice == 1):
            myTotalPoints = myTotalPoints + myChoice + 6
            continue
        else:
            myTotalPoints = myTotalPoints + myChoice
            continue
    if(opponent < myChoice):
        if(opponent == 1 and myChoice== 3):
            myTotalPoints = myTotalPoints + myChoice
            continue
        else:
            myTotalPoints = myTotalPoints + myChoice + 6
            continue

print('result 1: ', myTotalPoints)

# second part  3=win 2=draw 1=lose
# 1 Rock, 2 paper, 3 scissors
myTotalPoints = 0

def getMyChoice(opp, res):
    if result == 3:
        if opp <3:
            return opp+1
        else:
            return 1
    if result ==2:
        return opp
    if result == 1:
        if opp > 1:
            return opp-1
        else:
            return 3


for line in Lines:
    line.strip()
    if(line==''):
        continue
    opponent = int(line[:1])
    result = int(line[-1:])
    myChoice = getMyChoice(opponent, result)
    if(opponent == myChoice):
        myTotalPoints= myTotalPoints + 3 + myChoice
        continue
    if(opponent > myChoice):
        if(opponent == 3 and myChoice == 1):
            myTotalPoints = myTotalPoints + myChoice + 6
            continue
        else:
            myTotalPoints = myTotalPoints + myChoice
            continue
    if(opponent < myChoice):
        if(opponent == 1 and myChoice== 3):
            myTotalPoints = myTotalPoints + myChoice
            continue
        else:
            myTotalPoints = myTotalPoints + myChoice + 6
            continue

print('result 2: ', myTotalPoints)

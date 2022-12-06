import numpy as np
file = open('input6.txt', 'r')
text = file.read()

def findIndex(text):
    for x in np.arange(0, len(text)-4,1, dtype=int):
        a = text[x:x+4]
        if len(set(a))== 4:
            return x+4
result = findIndex(text)
print(result)

def findIndex2(text):
    for x in np.arange(0, len(text)-15,1, dtype=int):
        a = text[x:x+15]
        if len(set(a))== 14:
            return x+15
result_p2 = findIndex2(text)
print(result_p2)

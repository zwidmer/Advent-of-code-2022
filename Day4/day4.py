import numpy as np
file = open('input4.txt', 'r')
Lines = file.readlines()

count = 0
for line in Lines:
    first, second = line.split(',')
    min_first, max_first = [int(x) for x in first.strip().split('-')]
    min_second, max_second = [int(x) for x in  second.strip().split('-')]
    if (min_first<=min_second and max_first>=max_second) or (min_first>=min_second and max_first<=max_second):
        count += 1

print(count)

#part2
count2=0
for line in Lines:
    first, second = line.split(',')
    min_first, max_first = [int(x) for x in first.strip().split('-')]
    min_second, max_second = [int(x) for x in  second.strip().split('-')]
    if (min_first<=min_second<=max_first or min_first<=max_second<=max_first) or (min_second<=min_first<=max_second or min_second<=max_first<=max_second):
        count2+= 1

print(count2)
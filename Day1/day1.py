#https://adventofcode.com/2022/day/1

import numpy as numpy

file1 = open('input.txt', 'r')
Lines = file1.readlines()
Elves = numpy.arange(0,len(Lines),1)
count =0
sum = 0
for line in Lines:

    if line =='\n':
        Elves[count] =sum
        count += 1
        sum=0
    else:
        part = line.strip()
        sum = sum + int(part)

print(Elves.max())

sorted = numpy.sort(Elves)
print(sorted)
top = sorted[-1]
second = sorted[-2]
third = sorted[-3]

total = top +second+third

print(total)


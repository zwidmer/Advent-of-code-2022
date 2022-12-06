import numpy as np
file = open('input5.txt', 'r')
text = file.read()
stacks, orders = text.split('\n\n')
Lines = stacks.split('\n')
Lines = Lines[0:-1]
number_of_stacks = Lines[-1].strip()[-1]

stacks = [ [] for _ in range(9) ]
def addToStacks(stack, content):
    content = content.strip()
    if(content != ''):
        stacks[stack].extend(content)

for line in Lines:
    stack = 0
    for i in np.arange(0,len(line)+1,4,  dtype=int):
        if line[i + 2:]:
            addToStacks(stack, line[i+1:i + 2])
        stack +=1
for stack in stacks: stack.reverse()

#move 2 from 1 to 7
for order in orders.split('\n'):
    order.strip()
    number, direction = order.split('from')
    number= int(number.strip().split(" ")[-1])
    from_pos, to_pos = direction.split('to')
    from_pos = int(from_pos.strip())
    to_pos = int(to_pos.split(' ')[-1])
    stack_to_move = np.empty(number, dtype=str)
    print( stacks[from_pos-1], number)
    for x in range(number):
            elem = stacks[from_pos-1].pop()
            index = number - x -1
            stack_to_move[index] = elem
    stacks[to_pos-1].extend(stack_to_move)
    print(stack_to_move, stacks[to_pos-1])
result = ''
for stack in stacks:
    result += (stack[-1])
print(result)


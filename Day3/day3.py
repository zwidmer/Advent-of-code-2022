import numpy as np
file = open('input3.txt', 'r')
Lines = file.readlines()

alphabet = 'a 	b 	c 	d 	e 	f 	g 	h 	i 	j 	k 	l 	m 	n 	o 	p 	q 	r 	s 	t 	u 	v 	w 	x 	y 	z  A 	B 	C 	D 	E 	F 	G 	H 	I 	J 	K 	L 	M 	N 	O 	P 	Q 	R 	S 	T 	U 	V 	W 	X 	Y 	Z'.strip().split()
numbers = np.arange(1,53,1)
alphabet_map = dict(zip(alphabet, numbers))

#part 1
sum =0
for line in Lines:
    line = line.strip()
    size = int(len(line)/2)
    first = line[0:size]
    second = line[size:]
    com_str = ''.join(set(first).intersection(second))
    sum += alphabet_map.get(com_str)

print(sum)


#part2
sum2=0
for x in np.arange(0,len(Lines)-1, 3, dtype=int):
    first_line =Lines[x].strip()
    second_line = Lines[x+1].strip()
    third_line = Lines[x+2].strip()
    com_str2 = ''.join(set(first_line).intersection(second_line).intersection(third_line))
    sum2 += alphabet_map.get(com_str2)
print(sum2)

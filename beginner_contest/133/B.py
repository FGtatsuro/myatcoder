_input = [i for i in open(0).read().split('\n') if i]
n, d = [int(i) for i in _input[0].split()]
x_list = [[int(i) for i in x.split()]for x in _input[1:]]
x_list2 = x_list[:]

import math

count = 0
for x1 in x_list:
    for x2 in x_list2:
        dist = math.sqrt(sum((x1[i]-x2[i])**2 for i in range(d)))
        if int(dist) == 0:
            continue
        if dist.is_integer():
            count += 1

print(count//2)

n = int(input())
v = [[int(i) for i in input().split()] for _ in range(n)]

max_length_square = 0
for i in range(n):
    for j in range(n):
        max_length_square = max((v[i][0] - v[j][0]) ** 2 + (v[i][1] - v[j][1]) ** 2, max_length_square)

import math
print(math.sqrt(max_length_square))

_input = [i for i in open(0).read().split('\n') if i]
l, r = [int(i) for i in _input[0].split()]
i_start = l
j_start = l + 1
i_end = min(r-1, i_start+(2019-1))
j_end = min(r, j_start+(2019-1))

min_val = 2018
for i in range(i_start, i_end+1):
    for j in range(j_start, j_end+1):
        if i >= j:
            continue
        min_val = min(min_val, (i * j) % 2019)
print(min_val)

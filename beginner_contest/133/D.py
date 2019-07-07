_input = [i for i in open(0).read().split('\n') if i]
n = int(_input[0])
a_list = [int(i) for i in _input[1].split()]
a_double_list = [i * 2 for i in a_list]

switch = 1
total = 0
for i in range(n):
    if (switch % 2) == 1:
        total += a_double_list[i]
    else:
        total -= a_double_list[i]
    switch += 1
b1 = total // 2

ans = [b1]
for i in range(n-1):
    b = a_double_list[i] - ans[i]
    ans.append(b)
print(' '.join(str(i) for i in ans))

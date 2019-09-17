n, k, q = [int(i) for i in input().split()]
a = [0] + [int(input()) for _ in range(q)]
score = [0] + [0] * n

for i in range(1, q + 1):
    score[a[i]] += 1
for i in range(1, n + 1):
    if score[i] - q + k > 0:
        print('Yes')
    else:
        print('No')

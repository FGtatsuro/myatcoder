n = int(input())
d = [int(i) for i in input().split()]
total = 0

for i in range(n):
    for j in range(n):
        if i >= j:
            continue
        total += d[i] * d[j]
print(total)

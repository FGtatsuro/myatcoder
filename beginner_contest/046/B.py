n, k = [int(i) for i in input().split()]

if n == 1:
    print(k)
else:
    total = 1
    for i in range(n):
        if i == 0:
            total *= k
        else:
            total *= k - 1
    print(total)

n = int(input())
h = [int(i) for i in input().split()]

if n == 1:
    print(0)
else:
    max_count = 0
    current = 0
    for i in range(n - 1):
        if h[i] < h[i+1]:
            max_count = max(max_count, current)
            current = 0
        else:
            current += 1
    max_count = max(max_count, current)
    print(max_count)

n, k = [int(i) for i in input().split()]
h = [int(i) for i in input().split()]

print(len([i for i in h if i >= k]))

n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]

prev = -100
total = 0
for i in a:
    total += b[i - 1]
    if prev == i - 1:
        total += c[i - 2]
    prev = i
print(total)

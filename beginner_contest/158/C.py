import sys
input = sys.stdin.readline

a, b = [int(i) for i in input().split()]

start = int(((a * 100)/8) + 0.5)
if a % 2 == 0:
    candidate1 = list(range(start, start + 13))
else:
    candidate1 = list(range(start, start + 12))
start = (b * 10)
candidate2 = list(range(start, start + 10))

ans = -1
for i in candidate2:
    if i in candidate1:
        ans = i
        break
print(ans)

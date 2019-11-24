import sys
sys.setrecursionlimit(10 ** 6)

a, b, x = [int(i) for i in input().split()]

MAX = 10 ** 9
ans = 0

def solver(start, current, end):
    global ans
    result = a * current + b * len(str(current))
    if result <= x:
        ans = max(current, ans)
        if current + 1 == end:
            return
        solver(current, (current + end) // 2, end)
    else:
        if start + 1 == current:
            return
        solver(start, (start + current) // 2, current)

if (a * MAX + b * 10) <= x:
    print(MAX)
    sys.exit(0)

if (a * 1 + b * 1) > x:
    print(0)
    sys.exit(0)
else:
    ans = 1

solver(1, MAX // 2, MAX)
print(ans)

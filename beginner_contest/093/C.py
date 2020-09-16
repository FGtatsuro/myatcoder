import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a, b, c = sorted(map(int, input().split()))

ans = 0
while not (a % 2 == b % 2 == c % 2):
    if a % 2 == b % 2:
        a += 1
        b += 1
    elif a % 2 == c % 2:
        a += 1
        c += 1
    elif b % 2 == c % 2:
        b += 1
        c += 1
    ans += 1

print(ans + (c - a) // 2 + (c - b) // 2)

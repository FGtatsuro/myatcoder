import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
a = [-1] + list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

left_gcd = [0] + [0] * n + [-1]
right_gcd = [-1] + [0] * n + [0]

for i in range(n):
    left_gcd[i + 1] = gcd(left_gcd[i], a[i + 1])
    right_gcd[n - i] = gcd(right_gcd[n - i + 1], a[n - i])

ans = 1
for i in range(1, n+1):
    ans = max(ans, gcd(left_gcd[i-1], right_gcd[i+1]))
print(ans)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a, b, c, d = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return (a // gcd(a, b)) * b

# 両端の余りをあわせて、商が1増える可能性がある
#ans = b - a + 1
#
#ans -= (b - a) // c
#if a % c == 0:
#    ans -= 1
#
#ans -= (b - a) // d
#if a % d == 0:
#    ans -= 1
#
#_lcm = lcm(c, d)
#ans += (b - a) // _lcm
#if a % _lcm == 0:
#    ans += 1
#print(ans)

def solve(n):
    ans = n
    ans -= n // c
    ans -= n // d
    ans += n // lcm(c, d)
    return ans

print(solve(b) - solve(a - 1))

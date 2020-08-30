import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def is_prime(n):
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True

x = int(input())

while True:
    if is_prime(x):
        print(x)
        sys.exit(0)
    else:
        x += 1

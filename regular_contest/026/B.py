import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())

divisor = set()
target = n
i = 1
while i ** 2 <= target:
    if target % i != 0:
        i += 1
        continue

    divisor.add(i)
    divisor.add(target // i)

    i += 1
divisor.remove(n)

s = sum(divisor)
if s == n:
    print('Perfect')
elif s < n:
    print('Deficient')
else:
    print('Abundant')

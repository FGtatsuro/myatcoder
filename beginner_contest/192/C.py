import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())

def g1(num):
    return int(''.join(sorted(str(num), reverse=True)))

def g2(num):
    return int(''.join(sorted(str(num))))

ai = N
for i in range(1, K + 1):
    ai_1 = g1(ai) - g2(ai)
    if ai_1 == ai:
        print(ai)
        sys.exit(0)
    else:
        ai = ai_1
print(ai)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
str_n = str(n)

if n < 10:
    print(n)
    sys.exit(0)

ans = 0
while True:
    if n // 10 == 0:
        break
    ans += 9
    n //= 10

# 最上位から1桁下が全て9の場合、繰り下がりが不要
if set(str_n[1:]) == {'9'}:
    ans += n
else:
    ans += (n - 1)

print(ans)

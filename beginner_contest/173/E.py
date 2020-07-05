import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, k = map(int, input().split())
a = list(map(int, input().split()))
MOD = 10 ** 9 + 7

plus_zero = []
minus = []

for i in a:
    if i >= 0:
        plus_zero.append(i)
    if i < 0:
        minus.append(-i)

from collections import deque

plus_zero = deque(sorted(plus_zero, reverse=True))
minus = deque(sorted(minus, reverse=True))
absolute = deque(sorted(a, key=abs, reverse=True))

ans_lst = []
# 境界条件: k == n
if k == n:
    ans_lst.extend(a)
# 負
elif len(plus_zero) == 0 and (k % 2) != 0:
    for _ in range(k):
        ans_lst.append(-minus.pop())
# 正 or 0
else:
    minus_num = 0
    for _ in range(k):
        v = absolute.popleft()
        if v < 0:
            minus_num += 1
        ans_lst.append(v)
    if minus_num % 2 != 0:
        abs_min_plus_zero, abs_min_minus = None, None
        abs_max_plus_zero, abs_max_minus = None, None
        for i in ans_lst:
            if i >= 0:
                if abs_min_plus_zero is None:
                    abs_min_plus_zero = i
                else:
                    abs_min_plus_zero = min(i, abs_min_plus_zero)
            else:
                if abs_min_minus is None:
                    abs_min_minus = i
                else:
                    abs_min_minus = max(abs_min_minus, i)
        for i in absolute:
            if i >= 0:
                if abs_max_plus_zero is None:
                    abs_max_plus_zero = i
                else:
                    abs_max_plus_zero = max(i, abs_max_plus_zero)
            else:
                if abs_max_minus is None:
                    abs_max_minus = i
                else:
                    abs_max_minus = min(abs_max_minus, i)
        case1, case2 = False, False
        if abs_min_plus_zero is not None and abs_max_minus is not None:
            case1 = True
        if abs_min_minus is not None and abs_max_plus_zero is not None:
            case2 = True
        if case1 and case2:
            if abs_max_minus * abs_min_minus <= abs_max_plus_zero * abs_min_plus_zero:
                ans_lst.remove(abs_min_minus)
                ans_lst.append(abs_max_plus_zero)
            else:
                ans_lst.remove(abs_min_plus_zero)
                ans_lst.append(abs_max_minus)
        elif case1:
            ans_lst.remove(abs_min_plus_zero)
            ans_lst.append(abs_max_minus)
        elif case2:
            ans_lst.remove(abs_min_minus)
            ans_lst.append(abs_max_plus_zero)
        
# functools.reduceはTLEをくらう場合があるので気をつける
ans = 1
for i in ans_lst:
    ans = (ans * i) % MOD
print(ans)


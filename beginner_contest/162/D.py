import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
s = input().strip()

if ('R' not in s) or ('G' not in s) or ('B' not in s):
    print(0)
    sys.exit(0)

from collections import deque

index_cache = {'R': deque(), 'G': deque(), 'B': deque()}
for i, v in enumerate(s):
    index_cache[v].append(i)

ans = 0
for i, v in enumerate(s):
    index_cache[v].popleft()

    v2, v3 = set('RGB') - set(v)
    if len(index_cache[v2]) == 0 or len(index_cache[v3]) == 0:
        break

    i2, i3 = index_cache[v2][0], index_cache[v3][0]
    ans += len(index_cache[v2]) * len(index_cache[v3])

    if i2 < i3:
        for i4 in index_cache[v2]:
            if i4 + (i4 - i) < n and s[i4 + (i4 - i)] == v3:
                ans -= 1
            if (i + i4) % 2 == 0 and s[(i + i4) // 2] == v3:
                ans -= 1
    else:
        for i5 in index_cache[v3]:
            if i5 + (i5 - i) < n and s[i5 + (i5 - i)] == v2:
                ans -= 1
            if (i + i5) % 2 == 0 and s[(i + i5) // 2] == v2:
                ans -= 1

print(ans)

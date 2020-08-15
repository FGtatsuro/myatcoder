import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, k = map(int, input().split())
p = [0] + list(map(int, input().split()))
c = [0] + list(map(int, input().split()))

from collections import deque

def bfs(queue, cycle_index, cycle_num):
    cycle = []
    score = 0
    while queue:
        current = queue.popleft()
        cycle_index[current] = cycle_num
        cycle.append(current)
        score += c[current]

        if p[current] not in cycle_index:
            queue.append(p[current])
    return cycle, score

cycle_index = {}
cycle_num = 0
cycles = []
for i in range(1, n + 1):
    if i in cycle_index:
        continue
    queue = deque([i])
    cycle, score = bfs(queue, cycle_index, cycle_num)
    cycles.append((cycle, score))
    cycle_num += 1

ans = None
for i in range(1, n + 1):
    cycle, score = cycles[cycle_index[i]]
    tmp_ans = 0
    
    cum = [0]
    current = i
    for j in range(1, len(cycle)):
        current = p[current]
        cum.append(cum[-1] + c[current])

    if score > 0:
        q = (k // len(cycle))
        r = k % len(cycle)
        # 一周しない方がいいケースがある
        # FYI: https://atcoder.jp/contests/abc175/submissions/15968040
        if r == 0:
            tmp_ans = max((score * q), (score * (q - 1)) + max(cum[1:]))
        else:
            tmp_ans = (score * q) + max(cum[1:r+1])
    else:
        r = min(k, len(cycle))
        tmp_ans = max(cum[1:r+1])

    if ans is None:
        ans = tmp_ans
    else:
        ans = max(ans, tmp_ans)
print(ans)

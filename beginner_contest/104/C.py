d, g = [int(i) for i in input().split()]
p = [0] + [[int(i) for i in input().split()] for _ in range(d)]

def recursive(d, g):
    if d == 0:
        return 10 ** 9
    n = min(g // (100 * d), p[d][0])
    t = 100 * d * n
    # Full
    if n == p[d][0]:
        t += p[d][1]
    # Partial
    if t < g:
        n += recursive(d-1, g-t)
    return min(n, recursive(d-1, g))

def bit(d, g):
    ans = 10 ** 9
    for i in range(2 ** d):
        b = '-' + format(i, '0{}b'.format(d))
        last_zero_index = 0
        tmp_ans = 0
        total_score = 0
        for j in range(1, d+1):
            if b[j] == '1':
                total_score += p[j][0] * (100 * (j))
                total_score += p[j][1]
                tmp_ans += p[j][0]
            else:
                last_zero_index = j
        if total_score < g:
            diff = g - total_score
            q = diff // (100 * last_zero_index)
            r = diff % (100 * last_zero_index)
            if r != 0:
                q += 1
            if q > p[last_zero_index][0]:
                continue
            else:
                tmp_ans += q
        ans = min(ans, tmp_ans)
    return ans

solve = recursive
#solve = bit
print(solve(d, g))

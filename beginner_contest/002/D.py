n, m = [int(i) for i in input().split()]
relations = {tuple(int(i) for i in input().split()) for _ in range(m)}

import itertools

def solve(n, m, relations):
    if m == 0:
        return 1
    ans = 0
    for i in range(2 ** n):
        bit = '-' + format(i, '0{}b'.format(n))
        flag_index = [i for i in range(1, n+1) if bit[i] == '1']
        if len(flag_index) <= 1:
            continue
        combinations = set(itertools.combinations(flag_index, 2))
        if combinations.issubset(relations):
            ans = max(ans, len(flag_index))
    return ans

print(solve(n, m, relations))

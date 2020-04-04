import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

k = int(input())

ans = list(range(1, 10))
d = 10
prev = ['0'] + list(map(str, ans))
while len(ans) <= k:
    _next = []
    for v in prev:
        if v[0] == '0':
            _next.append('0' + v)
            _next.append('1' + v)
            ans.append(int('1' + v))
            continue
        if v[0] == '1':
            _next.append('0' + v)
            _next.append('1' + v)
            ans.append(int('1' + v))
            _next.append('2' + v)
            ans.append(int('2' + v))
            continue
        if v[0] == '9':
            _next.append('8' + v)
            ans.append(int('8' + v))
            _next.append('9' + v)
            ans.append(int('9' + v))
            continue
        i = int(v[0])
        s1 = str(i - 1)
        s2 = str(i)
        s3 = str(i + 1)
        _next.append(s1 + v)
        ans.append(int(s1 + v))
        _next.append(s2 + v)
        ans.append(int(s2 + v))
        _next.append(s3 + v)
        ans.append(int(s3 + v))
    prev = _next

print(sorted(ans)[k-1])

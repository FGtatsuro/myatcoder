import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))

route = [1]
index = k
hit = set([1])
for i in range(n+1):
    _next = a[route[-1]]
    if _next in hit:
        route.append(_next)
        index -= (i+1)
        break
    route.append(_next)
    hit.add(_next)

if index <= 0:
    print(route[k])
else:
    route = route[route.index(route[-1]):-1]
    print(route[index % len(route)])

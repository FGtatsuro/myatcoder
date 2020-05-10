import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, q = map(int, input().split())
query = [0] * q
for i in range(q):
    query[i] = list(map(int, input().split()))

parent = [0] * n
for i in range(n):
    parent[i] = i

def root(n):
    if parent[n] == n:
        return n
    else:
        # 経路圧縮なし
        #return root(parent[n])
        # 経路圧縮あり 
        parent[n] = root(parent[n])
        return parent[n]

def unite(n1, n2):
    p1 = root(n1)
    p2 = root(n2)
    if p1 == p2:
        return

    parent[p2] = p1

for q in query:
    p, a, b = q
    if p == 0:
        unite(a, b)
    if p == 1:
        if root(a) == root(b):
            print('Yes')
        else:
            print('No')

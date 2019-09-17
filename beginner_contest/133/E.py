import sys
sys.setrecursionlimit(4100000)

_input = [i for i in open(0).read().split('\n') if i]
n, k = [int(i) for i in _input[0].split()]
edge = tuple([tuple([int(p) for p in i.split()]) for i in _input[1:n]])

factorial = [0] * (k + 1)
inverse = [0] * (k + 1)
MOD = 1000000007

# Ref: http://keita-matsushita.hatenablog.com/entry/2016/12/05/175024
def mod_pow1(n, k, mod):
    a = 1
    while k:
        if (k & 1) == 1:
            a = (a * n) % mod
        n = (n * n) % mod
        k >>= 1
    return a

# Ref: https://www.smartbowwow.com/2018/10/mod1097.html
def mod_pow2(n, k, mod):
    if k == 0:
        return 1
    if k % 2 == 0:
        a = mod_pow2(n, k // 2, mod)
        return (a * a) % mod
    else:
        return (n * mod_pow2(n, k - 1, mod)) % mod

#mod_pow = mod_pow1
# It's better to use built-in function for speed.
mod_pow = pow

def mod_factorial_inverse(k, mod):
    factorial[0] = 1
    inverse[0] = 1

    # Ref: http://keita-matsushita.hatenablog.com/entry/2016/12/05/184011
    for i in range(1, k + 1):
        factorial[i] = ((i * factorial[i - 1]) % mod) # factrial[i]
        inverse[i] = mod_pow(factorial[i], mod - 2, mod) # inverse[i]
 
total = 1

if not edge:
    print(k)
else:
    all_edge = tuple([[] for _ in range(n + 1)])
    for e in edge:
        all_edge[e[0]].append(e[1])
        all_edge[e[1]].append(e[0])
    all_edge = [set(v) for v in all_edge]

    if [v for v in all_edge if len(v) >= k]:
        print(0)
    else:
        mod_factorial_inverse(k, MOD)

        root = edge[0]
        total = (factorial[k] * inverse[k - len(all_edge[root[0]]) - 1]) % MOD

        def dfs(current, from_):
            global total
            child = all_edge[current]
            if len(child) - 1 > 0:
                total = (total * factorial[k - 2] * inverse[k - 2 - (len(child) - 1)]) % MOD
            for c in child:
                if c != from_:
                    dfs(c, current)
        for c in all_edge[root[0]]:
            dfs(c, root[0])
        print(total)

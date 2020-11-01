import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = input().strip()

if len(s) == 1:
    if s == '8':
        print('Yes')
    else:
        print('No')
elif len(s) == 2:
    if int(s) % 8 == 0:
        print('Yes')
    elif int(s[1] + s[0]) % 8 == 0:
        print('Yes')
    else:
        print('No')
else:
    from collections import Counter
    c = Counter(s)
    mul = 0
    while mul < 1000:
        c2 = Counter(format(mul, '03'))
        ok = True
        for k in c2:
            if (k not in c) or (c[k] < c2[k]):
                ok = False
                break
        if ok:
            print('Yes')
            sys.exit(0)
        else:
            mul += 8
    print('No')

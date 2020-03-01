import sys
input = sys.stdin.readline

a1 = [int(i) for i in input().split()]
a2 = [int(i) for i in input().split()]
a3 = [int(i) for i in input().split()]

n = int(input())

b = [0] * n
for i in range(n):
    b[i] = int(input())

for v in b:
    try:
        i = a1.index(v)
        a1[i] = 0
        continue
    except:
        pass
    try:
        i = a2.index(v)
        a2[i] = 0
        continue
    except:
        pass
    try:
        i = a3.index(v)
        a3[i] = 0
        continue
    except:
        pass

def cond():
    if a1[0] == 0 and a1[1] == 0 and a1[2] == 0:
        return True
    if a2[0] == 0 and a2[1] == 0 and a2[2] == 0:
        return True
    if a3[0] == 0 and a3[1] == 0 and a3[2] == 0:
        return True
    if a1[0] == 0 and a2[0] == 0 and a3[0] == 0:
        return True
    if a1[1] == 0 and a2[1] == 0 and a3[1] == 0:
        return True
    if a1[2] == 0 and a2[2] == 0 and a3[2] == 0:
        return True
    if a1[0] == 0 and a2[1] == 0 and a3[2] == 0:
        return True
    if a1[2] == 0 and a2[1] == 0 and a3[0] == 0:
        return True
    return False

if cond():
    print('Yes')
else:
    print('No')

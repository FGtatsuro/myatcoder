import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

S1 = list(input().strip())
S2 = list(input().strip())
S3 = list(input().strip())

import string

# 3番目の条件より高々10個のアルファベットしか存在しえない
chars = set(S1 + S2 + S3)
if len(chars) > 10:
    print('UNSOLVABLE')
    sys.exit(0)

# 各文字を順列の何番目と対応させるか
char_map = dict()
for i, v in enumerate(chars):
    char_map[v] = i

for i, v in enumerate(S1):
    S1[i] = char_map[v]
for i, v in enumerate(S2):
    S2[i] = char_map[v]
for i, v in enumerate(S3):
    S3[i] = char_map[v]

import itertools
for perm in itertools.permutations(range(10), len(chars)):
    # 先頭の数字が0では駄目
    if perm[S1[0]] == 0 or perm[S2[0]] == 0 or perm[S3[0]] == 0:
        continue
    N1 = 0
    N2 = 0
    N3 = 0
    # 下位から処理する
    for i, v in enumerate(reversed(S1)):
        N1 += perm[v] * (10 ** i)
    for i, v in enumerate(reversed(S2)):
        N2 += perm[v] * (10 ** i)
    for i, v in enumerate(reversed(S3)):
        N3 += perm[v] * (10 ** i)
    if N1 + N2 == N3:
        print(N1)
        print(N2)
        print(N3)
        sys.exit(0)
print('UNSOLVABLE')

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

K = int(input())
S = input().strip()
T = input().strip()

from collections import Counter
remains = [0] + [K] * 9
sc = Counter(S[:-1])
sc = {int(k):sc[k] for k in sc}
tc = Counter(T[:-1])
tc = {int(k):tc[k] for k in tc}
s_card = [0] + [0] * 9
t_card = [0] + [0] * 9
for card, count in sc.items():
    remains[card] -= count
    s_card[card] += count
for card, count in tc.items():
    remains[card] -= count
    t_card[card] += count

# 配り方の場合の数は余ったカードの枚数から算出できる
case = (9 * K - 8) * (9 * K - 9)
win = 0
# i: 高橋君の#
# j: 青木君の#
for i in range(1, 10):
    for j in range(1, 10):
        # カードが残っていない
        # 同じカードを引くケース
        if i == j and remains[i] < 1:
            continue
        # 違うカードを引くケース
        if remains[i] == 0 or remains[j] == 0:
            continue

        s_card[i] += 1
        t_card[j] += 1

        s_score = 0
        t_score = 0
        for k in range(1, 10):
            s_score += k * (10 ** s_card[k])
            t_score += k * (10 ** t_card[k])

        # 同じ組み合わせでも複数配り方がある
        if s_score > t_score:
            if i == j:
                win += remains[i] * (remains[i] - 1)
            else:
                win += remains[i] * remains[j]

        s_card[i] -= 1
        t_card[j] -= 1

print(win / case)

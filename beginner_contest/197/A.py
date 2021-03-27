import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

S = input().strip()

print(S[1:]+S[0])

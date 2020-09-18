import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = input().strip()

if len(s) == 2:
    print(0)
    sys.exit(0)

for i in range(1, len(s) // 2 + 1):
    split_index = (len(s) - i * 2) // 2
    if s[:split_index] == s[split_index:len(s) - i * 2]:
        print(len(s) - i * 2)
        sys.exit(0)

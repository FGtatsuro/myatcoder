import sys
input = sys.stdin.readline
s = input().strip()

count = 0
check = len(s) //  2

for i in range(check):
    if s[i] != s[-i-1]:
        count += 1

print(count)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

s = input().strip()
print(len(s[s.find('A'):s.rfind('Z')+1]))

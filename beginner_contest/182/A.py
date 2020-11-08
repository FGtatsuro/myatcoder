import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a, b = map(int, input().split())

print(2 * a + 100 - b)

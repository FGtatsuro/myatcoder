import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

x = int(input())

a = x // 500
b = (x - (500 * a)) // 5
print(1000 * a + 5 * b)

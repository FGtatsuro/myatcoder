import sys
input = sys.stdin.readline

a, b = [int(i) for i in input().split()]

str_a = str(a) * b
str_b = str(b) * a
print(min(str_a, str_b))

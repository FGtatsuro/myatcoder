n = int(input())
s = input()

west = [0] * (n + 2)
east = [0] * (n + 2)

for i,v in enumerate(s):
    west[i + 1] = west[i]
    if v == 'W':
        west[i + 1] += 1

for i,v in enumerate(reversed(s)):
    east[n - i] = east[n + 1 - i]
    if v == 'E':
        east[n - i] += 1

min_count = None
for i in range(n):
    if min_count is None:
        min_count = west[i] + east[i + 2]
    else:
        min_count = min(min_count, west[i] + east[i + 2])

print(min_count)

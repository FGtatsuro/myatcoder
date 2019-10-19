n = int(input())
s = input()

out = '0'

for i in s:
    if out[-1] != i:
        out += i

print(len(out) - 1)

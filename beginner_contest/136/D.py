s = input()
reverse_s = s[::-1]

num = [0] * len(s)

for i in range(len(s)):
    if s[i] == 'R':
        nearest = s.index('L', i)
        if (nearest - i) % 2 == 0:
            num[nearest] += 1
        else:
            num[nearest - 1] += 1
    else:
        reverse_i = len(s) - (i + 1)
        reverse_nearest = reverse_s.index('R', reverse_i)
        nearest = len(s) - (reverse_nearest + 1)
        if (i - nearest) % 2 == 0:
            num[nearest] += 1
        else:
            num[nearest + 1] += 1
print(*num)

n, s = int(input()), input()

d = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print(''.join([d[(d.index(i) + n) % 26] for i in s]))

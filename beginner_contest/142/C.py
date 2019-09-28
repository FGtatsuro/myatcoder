n = int(input())
a = [int(i) for i in input().split()]

a_with_index = []
for i, v in enumerate(a):
    a_with_index.append((v, str(i + 1)))

print(' '.join(v[1] for v in sorted(a_with_index)))

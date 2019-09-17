n = int(input())
MOD = 10 ** 9 + 7
factrial = [0] * (n + 1)

factrial[1] = 1

for i in range(2, n + 1):
    factrial[i] = (factrial[i - 1] * i) % MOD
print(factrial[n])

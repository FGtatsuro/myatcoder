_input = [i for i in open(0).read().split('\n') if i]
n, a, b = [int(i) for i in _input[0].split()]
print(sum(i for i in range(1, n+1) if a <= sum(int(s) for s in str(i)) <= b))

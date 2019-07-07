_input = [i for i in open(0).read().split('\n') if i]
n, a, b = [int(i) for i in _input[0].split()]
print(min(n * a, b))

_input = [i for i in open(0).read().split('\n') if i]
n = _input[0]
a = sorted([int(i) for i in _input[1].split()], reverse=True)
print(sum(a[0:None:2]) - sum(a[1:None:2]))

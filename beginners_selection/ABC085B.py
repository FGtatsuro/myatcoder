_input = [i for i in open(0).read().split('\n') if i]
n = _input[0]
d = _input[1:]
print(len(set(d)))

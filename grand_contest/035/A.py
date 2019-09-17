_input = [i for i in open(0).read().split('\n') if i]
n = int(_input[0])
a = [int(i) for i in _input[1].split()]

import functools
if functools.reduce(lambda a, b: a^b, a) == 0:
    print('Yes')
else:
    print('No')

_input = [i for i in open(0).read().split('\n') if i]
s = _input[0]

import re
if re.search(r'^(dream|dreamer|erase|eraser)+$', s):
    print('YES')
else:
    print('NO')

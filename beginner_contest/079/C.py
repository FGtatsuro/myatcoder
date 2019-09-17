a, b, c, d = input()

import sys
ops = '+-'
for op1 in ops:
    for op2 in ops:
        for op3 in ops:
            s = '{}{}{}{}{}{}{}'.format(a, op1, b, op2, c, op3, d)
            if eval(s) == 7:
                print('{}=7'.format(s))
                sys.exit(0)

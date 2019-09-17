s = input()

import sys

for i in range(len(s)):
    if (i + 1) % 2 == 1 and s[i] not in 'RUD':
        print('No')
        sys.exit(0)
    if (i + 1) % 2 == 0 and s[i] not in 'LUD':
        print('No')
        sys.exit(0)
print('Yes')

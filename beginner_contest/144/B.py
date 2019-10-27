n = int(input())

import sys

if n <= 9:
    print('Yes')
    sys.exit(0)

for i in range(2, 10):
    if (n % i == 0) and (n // i <= 9):
        print('Yes')
        sys.exit(0)
print('No')

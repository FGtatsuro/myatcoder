a, b = [int(i) for i in input().split()]

import sys
if b == 1:
    print(0)
    sys.exit(0)

count = a
if count >= b:
    print(1)
else:
    ans = 2
    while True:
        count += (a - 1)
        if count >= b:
            print(ans)
            break
        ans += 1

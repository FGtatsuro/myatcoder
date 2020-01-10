import sys
input = sys.stdin.readline

n, s = int(input()), input()

import re

m = re.findall(r'ABC', s)
print(len(m))

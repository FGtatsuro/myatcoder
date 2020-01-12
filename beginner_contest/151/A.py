import sys
input = sys.stdin.readline

import string
lst = string.ascii_lowercase 

print(lst[lst.find(input().strip()) + 1])

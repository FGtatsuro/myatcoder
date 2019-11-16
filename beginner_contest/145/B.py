n = int(input())
s = input()

def cond():
    if n % 2 == 1:
        return False
    else:
        return s[:n//2] == s[n//2:]

if cond():
    print('Yes')
else:
    print('No')

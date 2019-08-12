a, b, c, d = [int(i) for i in input().split()]

def calc():
    if a <= c:
        if b < c:
            return 0
        if b >= d:
            return (d - c)
        return b - c
    else:
        if d < a:
            return 0
        if d >= b:
            return b - a
        return d - a
        
print(calc())

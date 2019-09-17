s = int(input())
if s <= 10 ** 9:
    print(0, 0, s, 0, s, 1)
else:
    a = s // (10 ** 9)
    b = s % (10 ** 9)
    if b == 0:
        print(0, 0, 10 ** 9, 1, 0, a)
    else:
        print(0, 0, 10 ** 9, 1, 10 ** 9 - b, a + 1)

_input = [i for i in open(0).read().split('\n') if i]
n = int(_input[0])
points = [[int(i) for i in i.split()] for i in _input[1:n+1]]

def has_route(t, x, y):
    if t < (x + y):
        return False
    else:
        return (t - (x + y)) % 2 == 0

reached = True
for t, x, y in points:
    if not has_route(t, x, y):
        reached = False
        break

if reached:
    print('Yes')
else:
    print('No')

_input = [i for i in open(0).read().split('\n') if i]
n = int(_input[0])
points = [[int(i) for i in i.split()] for i in _input[1:n+1]]

def has_route(current_point, next_point):
    t1, x1, y1 = current_point
    t2, x2, y2 = next_point
    t_diff = t2 - t1
    x_diff = x2 - x1
    y_diff = y2 - y1
    if t_diff < (x_diff + y_diff):
        return False
    else:
        return (t_diff - (x_diff + y_diff)) % 2 == 0

reached = True
points.insert(0, [0, 0, 0])
for i in range(len(points) - 1):
    if not has_route(points[i], points[i+1]):
        reached = False
        break

if reached:
    print('Yes')
else:
    print('No')

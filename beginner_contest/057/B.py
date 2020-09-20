import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())

students = [0] * n
for i in range(n):
    a, b = map(int, input().split())
    students[i] = (a + b, a - b)
checkpoints = [0] * m
for i in range(m):
    c, d = map(int, input().split())
    checkpoints[i] = (c + d, c - d)

for a_p_b, a_m_b in students:
    current_distance = 10 ** 10
    current_point = None
    for i, c_d in enumerate(checkpoints):
        c_p_d, c_m_d = c_d
        if max(abs(a_p_b - c_p_d), abs(a_m_b - c_m_d)) < current_distance:
            current_point = i + 1
            current_distance = max(abs(a_p_b - c_p_d), abs(a_m_b - c_m_d))
    print(current_point)
        

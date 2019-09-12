import functools
import heapq
from collections import deque

def build_graph_normal():
    for e in edges:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

def build_graph_maxheap():
    for e in edges:
        # Pythonのheapqはminheapのみなので、maxheapにするためには値を工夫する必要がある
        heapq.heappush(graph[e[0]], e[1] * -1)
        heapq.heappush(graph[e[1]], e[0] * -1)

def build_graph_minheap():
    for e in edges:
        heapq.heappush(graph[e[0]], e[1])
        heapq.heappush(graph[e[1]], e[0])

def build_graph_heap(weight=1):
    for e in edges:
        heapq.heappush(graph[e[0]], e[1] * weight)
        heapq.heappush(graph[e[1]], e[0] * weight)

def neighbor_select_normal(neighbors):
    yield from neighbors

def neighbor_select_maxheap(neighbors):
    for _ in range(len(neighbors)):
        # maxheapにするための-1を戻す
        yield heapq.heappop(neighbors) * -1

def neighbor_select_minheap(neighbors):
    for _ in range(len(neighbors)):
        yield heapq.heappop(neighbors)

def neighbor_select_heap(neighbors, weight=1):
    for _ in range(len(neighbors)):
        yield heapq.heappop(neighbors) * weight

def depth_first_pop(todo):
    # LIFO
    return todo.pop()

def dfs_iterative(graph, start, seen):
    todo = deque()
    # 発見する=seen[i]=True & todoに追加
    seen[start] = True
    todo.append(start)

    while todo:
        # 訪れる=取り出す(pop)
        current = pop(todo)
        print(current)
        for neighbor in neighbor_select(graph[current]):
            if seen[neighbor]:
                continue
            seen[neighbor] = True
            todo.append(neighbor)

# 行きがけ順/帰りがけ順/タイムスタンプ
# FYI: https://qiita.com/drken/items/4a7869c5e304883f539b#3-4-dfs-%E3%81%AE%E6%8E%A2%E7%B4%A2%E9%A0%86%E5%BA%8F%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6%E3%81%AE%E8%A9%B3%E7%B4%B0
first_order = []
last_order = []
time_stamp_arrive = []
time_stamp_leave = []
first = 0
last = 0
time = 0
def dfs_recursive(graph, current, seen):
    global first_order, first
    global last_order, last
    global time_stamp_arrive, time_stamp_leave, time

    # 発見する=訪れる=seen[current]=True
    seen[current] = True
    first_order[current] = first
    first += 1
    time_stamp_arrive[current] = time
    time += 1

    for neighbor in neighbor_select(graph[current]):
        if seen[neighbor]:
            continue
        dfs_recursive(graph, neighbor, seen)

    last_order[current] = last
    last += 1
    time_stamp_leave[current] = time
    time += 1

if __name__ == '__main__':
    n, m = [int(i) for i in input().split()]
    edges = [tuple([int(i) for i in input().split()]) for _ in range(m)]
    graph = [[] for _ in range(n)]
    seen = [False] * n
    first_order = [0] * n
    last_order = [0] * n
    time_stamp_arrive = [0] * n
    time_stamp_leave = [0] * n

    #pop = depth_first_pop
    ## build_graph = build_graph_maxheap
    #build_graph = functools.partial(build_graph_heap, weight=-1)
    ## neighbor_select = neighbor_select_maxheap
    #neighbor_select = functools.partial(neighbor_select_heap, weight=-1)
    #dfs = dfs_iterative

    # build_graph = build_graph_minheap
    build_graph = functools.partial(build_graph_heap)
    # neighbor_select = neighbor_select_minheap
    neighbor_select = functools.partial(neighbor_select_heap)
    dfs = dfs_recursive

    build_graph()
    dfs(graph, 0, seen)

    print('First Order: {}'.format(first_order))
    print('Last Order: {}'.format(last_order))
    print('TimeStamp Arrive: {}'.format(time_stamp_arrive))
    print('TimeStamp Leave: {}'.format(time_stamp_leave))

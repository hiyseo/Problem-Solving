## 진짜 마지막 - 처음부터 ##
# 트리 구하기 -> 시작 노드에서 가장 멀리 떨어진 노드 구하기
# 가장 멀리 떨어진 노드에서 다시 가장 멀리 떨어진 노드 구하기

from collections import deque

def bfs(start: int) -> tuple:
    visited = [False for _ in range(V+1)]
    dq = deque()
    for node, dist in graph[start]:
        dq.append((node, dist))
    visited[start] = True
    max_node, max_dist = 0, float('-inf')

    while dq:
        node, dist = dq.popleft()
        visited[node] = True
        if max_dist < dist:
            max_dist = dist
            max_node = node
        for n_node, n_dist in graph[node]:
            if not visited[n_node]:
                n_dist = n_dist+dist
                dq.append((n_node, n_dist))
    return max_node, max_dist

# def bfs(start: int) -> tuple:
#     visited = [False for _ in range(V+1)]
#     dq = deque()
#     dq.append((start, 0))
#     visited[start] = True
#     max_node, max_dist = start, 0

#     while dq:
#         print(f"max_dist: {max_dist}")
#         print(f"max_")
#         node, dist = dq.popleft()
#         if dist > max_dist:
#             max_dist = dist
#             max_node = node
#         for n_node, n_dist in graph[node]:
#             if not visited[n_node]:
#                 visited[n_node] = True
#                 dq.append((n_node, dist + n_dist))

    # return max_node, max_dist

V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    lst = list(map(int, input().split()))
    target = lst[0]
    idx = 1
    while lst[idx]!=-1:
        node, dist = lst[idx], lst[idx+1]
        graph[target].append((node, dist))
        idx+=2

node, _ = bfs(1)
node, dist = bfs(node)
print(dist)

### 테스트 케이스 1 ###
# 예제 입력 1
# 5
# 1 3 2 -1
# 2 4 4 -1
# 3 1 2 4 3 -1
# 4 2 4 3 3 5 6 -1
# 5 4 6 -1

# 예제 출력 1 
# 11
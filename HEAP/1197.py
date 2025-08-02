### 수도코드 ###
# 우선, 방향이 없는 그래프이므로 undirected_graph에 간선 정보 담음
# visited = [각 노드의 방문 정보]
# 첫 노드와 연결된 노드 중에서 간선 cost가 가장 작은 노드 선택 후
# total_cost += cost && visited[노드] = True

import heapq

V, E = map(int, input().split()) # V: 노드 수, E: 간선 개수
# print(f"V: {V}, E: {E}")
undirected_graph = [[] for _ in range(V+1)]
visited = [False for _ in range(V+1)]
for _ in range(E):
    u, v, cost = map(int, input().split())
    # print(f"u: {u}, v: {v}, cost: {cost}")
    undirected_graph[u].append((v, cost))
    undirected_graph[v].append((u, cost))
# print(f"undirected_graph: {undirected_graph}")

# hq -> heapq((cost, vertex))
hq = [(0, 1)] # hq 초기화
total_cost = 0

while hq:
    cost, v = heapq.heappop(hq)
    if visited[v]: continue
    visited[v] = True
    total_cost += cost
    for next_v, next_cost in undirected_graph[v]:
        heapq.heappush(hq, (next_cost, next_v))

print(total_cost)

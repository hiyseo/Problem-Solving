

# 우선순위 큐를 활용한 다익스트라 알고리즘
# 우선수위 큐란, 우선순위가 가장 높은 데이터를 가장 먼저 삭제(추출)
import heapq

INF = float('inf')
V, E = map(int, input().split())
path = [[] for _ in range(V)]
S = int(input()) - 1

for _ in range(E):
    u, v, w = map(int, input().split())
    path[u-1].append((v-1, w))

def dijkstra(start):
    cost = [INF for _ in range(V)]
    cost[start] = 0
    pq = [(0, start)]
    while pq:
        curr_cost, node = heapq.heappop(pq)
        for neighbor, weight in path[node]:
            new_cost = curr_cost + weight
            if new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))
    return cost

cost = dijkstra(S)
for num in cost:
    print(num if num!= INF else "INF")
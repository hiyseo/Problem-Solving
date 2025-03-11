INF = float('inf')
N = int(input())
M = int(input())
route = [[] for _ in range(N+1)]
cost = [INF for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for i in range(M):
    a, b, c = map(int, input().split())
    route[a].append((b, c))

start, dest = map(int, input().split())

cur_node = start
cost[start] = 0
for _ in range(N):
    visited[cur_node] = True
    for j in range(len(route[cur_node])):
        b, c = route[cur_node][j][0], route[cur_node][j][1]
        cost[b] = min(cost[b], cost[cur_node]+c)
    min_val = INF
    min_index = -1
    for index in range(len(cost)):
        if not visited[index] and cost[index] < min_val:
            min_val = cost[index]
            min_index = index
    cur_node = min_index
    
print(cost[dest])
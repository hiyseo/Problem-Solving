### 수도코드 ###
# graph 정보 (어떤 노드에서 어떤 노드가 들어오는지)
# indegree 정보 (어떤 노드로 몇 개의 노드가 들어오는지)
# indegree가 0일 때, queue에 push
# queue에서 popleft된 노드가 가리키는 모든 노드의 indegree 1 감소

from collections import deque

queue = deque()
res = []

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = {}
for i in range(1, N+1):
    indegree[i] = 0

for _ in range(M):
    lst = list(map(int, input().split()))
    n, lst = lst[0], lst[1:]
    # print(f"n: {n}, lst: {lst}")
    for i in range(n-1):
        curr, next = lst[i], lst[i+1]
        graph[curr].append(next)
        indegree[next] += 1

# print(f"graph: {graph}")
# print(f"indegree: {indegree}")

for key, value in indegree.items():
    if value == 0:
        queue.append(key)

while queue:
    node = queue.popleft()
    res.append(node)
    for i in graph[node]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)

if len(res) == N:
    for n in res:
        print(n)
else:
    print(0)
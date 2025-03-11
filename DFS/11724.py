N, M = map(int, input().split())
# print(f"N: {N}, M: {M}")

def find_connected(node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            find_connected(neighbor)

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

# 입력받기
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 연결 요소 개수 찾기
count = 0
for i in range(1, len(graph)):
    if not visited[i]:
        find_connected(i)
        count+=1

print(count)
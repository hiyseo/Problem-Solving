N = int(input())
graph = []
for _ in range(N):
    lst = list(map(int, input().split()))
    graph.append(lst)

def print_graph(graph):
    for i in range(N):
        for j in range(N):
            if j==N-1: print(graph[i][j])
            else: print(graph[i][j], end=' ')

for k in range(N): # 경유지
    for i in range(N): # 출발지
        for j in range(N): # 도착지
            if graph[i][k]==1 and graph[k][j]==1:
                graph[i][j]=1

# print("="*(N*2))
print_graph(graph)
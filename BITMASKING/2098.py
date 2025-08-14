N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1]*(1<<N) for _ in range(N)]

start = 0
INF = float('inf')

def tsp(curr, visited) -> int:
    '''
    현재 도시 curr에 있고, visited 상태일 때, 남은 모든 도시를 방문하고 출발 도시로 돌아가는 최소 비용
    '''
    if visited == (1<<N)-1:
        if W[curr][start] != 0:
            return W[curr][start]
        else:
            return INF
        
    if dp[curr][visited] != -1:
        return dp[curr][visited]
    
    min_cost = INF
    for nxt in range(N):
        if not visited & (1<<nxt) and W[curr][nxt] != 0:
            cost = W[curr][nxt] + tsp(nxt, visited | (1<<nxt))
            min_cost = min(min_cost, cost)

    dp[curr][visited] = min_cost
    return min_cost

answer = tsp(start, 1<<start)
print(answer)
import sys
sys.setrecursionlimit(10**9)

M, N = map(int, input().split())
MAP = []
TOTAL = [[-1 for _ in range(N)] for _ in range(M)]
for i in range(M):
    lst = list(map(int, input().split()))
    MAP.append(lst)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# (x, y)에서 출발하여 갈 수 있는 경로의 수
def dfs(x, y):
    if x==M-1 and y==N-1:
        return 1
    if TOTAL[x][y]!=-1:
        return TOTAL[x][y]
    TOTAL[x][y]=0
    # 상하좌우 가능한 경우 검색(더 작은 경우)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<M and 0<=ny<N:
            if MAP[x][y] > MAP[nx][ny]:
                # 현재 위치에 다음 위치의 가능한 경로의 수를 더함 - Dynamic Programming
                TOTAL[x][y] += dfs(nx, ny)
    return TOTAL[x][y]

print(dfs(0, 0))
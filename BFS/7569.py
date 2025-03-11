from collections import deque
import sys

def bfs():
    directions = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
    days = 0

    while queue:
        z, y, x, day = queue.popleft()
        days = max(days, day)
        for dz, dy, dx in directions:
            nz, ny, nx = z+dz, y+dy, x+dx
            if 0<=nz<H and 0<=ny<N and 0<=nx<M and storage[nz][ny][nx]==0:
                storage[nz][ny][nx]=1
                queue.append((nz, ny, nx, day+1))
    return days

M, N, H = map(int, sys.stdin.readline().split())
storage = []
queue = deque()
for h in range(H):
    layer = []
    for n in range(N):
        row = list(map(int, sys.stdin.readline().split()))
        layer.append(row)
        for m in range(M):
            if row[m] == 1:
                queue.append((h, n, m, 0))
    storage.append(layer)

result = bfs()

for h in range(H):
    for n in range(N):
        for m in range(M):
            if storage[h][n][m] == 0:
                print(-1)
                sys.exit()

print(result)
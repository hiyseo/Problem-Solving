from collections import deque

n, m = map(int, input().split())
start_x, start_y = -1, -1
MAP = []
VISITED = [[False for _ in range(m)] for _ in range(n)]
ANSWER = [[-1 for _ in range(m)] for _ in range(n)]
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(len(lst)):
        if lst[j] == 2: 
            start_x, start_y = i, j
        elif lst[j] == 0:
            ANSWER[i][j]=0
    MAP.append(lst)

def print_map(lst):
    for i in range(len(lst)):
        size = len(lst[i])
        for j in range(size):
            if j == size-1:
                print(lst[i][j])
            else: print(lst[i][j], end=' ')

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
queue = deque()
queue.append((start_x, start_y, 0))
while len(queue)>0:
    items = []
    cx, cy, dist = queue.popleft()
    ANSWER[cx][cy] = dist
    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if not VISITED[nx][ny] and MAP[nx][ny]==1:
                items.append((nx, ny, dist+1))
                VISITED[nx][ny] = True

    for item in items:
        queue.append(item)

print_map(ANSWER)
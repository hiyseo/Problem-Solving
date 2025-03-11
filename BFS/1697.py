from collections import deque

N, M = map(int, input().split())
VISITED = [False for _ in range(10**6)]
dx = [-1, 1, 2]
time = 0

queue = deque()
queue.append((N, 0))
while len(queue)>0:
    items = []
    cx, time = queue.popleft()
    if cx == M: break
    for i in range(3):
        if i==2:
            nx = cx*dx[i]
        else: nx = cx+dx[i]
        if 0<=nx<=100000 and not VISITED[nx]:
            items.append((nx, time+1))
            VISITED[nx] = True
    for item in items:
        queue.append(item)

print(time)
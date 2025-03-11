from collections import deque
N = int(input())
painting = []
visited = [[False for _ in range(N)] for _ in range(N)]
blind_visited = [[False for _ in range(N)] for _ in range(N)]
count = 0
blind_count = 0

for _ in range(N):
    painting.append(list(input()))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y, color):
    # print(f"x: {x}, y: {y}, color: {color}")
    queue = deque()
    queue.append((x, y))
    # print(queue)
    visited[x][y] == True
    while queue:
        curr = queue.popleft()
        cx, cy = curr[0], curr[1]
        # print(f"cx: {cx}, cy: {cy}")
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                # print(f"nx: {nx}, ny: {ny}")
                next_color = painting[nx][ny]
                if next_color == color: 
                    queue.append((nx, ny, next_color))
                    visited[nx][ny] = True

def blind_bfs(x, y, color):
    # print(f"x: {x}, y: {y}, color: {color}")
    blind_queue = deque()
    blind_queue.append((x, y))
    # print(queue)
    blind_visited[x][y] == True
    while blind_queue:
        curr = blind_queue.popleft()
        cx, cy = curr[0], curr[1]
        # print(f"cx: {cx}, cy: {cy}")
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<=nx<N and 0<=ny<N and not blind_visited[nx][ny]:
                # print(f"nx: {nx}, ny: {ny}")
                next_color = painting[nx][ny]
                if color in "RG" and next_color in "RG": 
                    blind_queue.append((nx, ny, next_color))
                    blind_visited[nx][ny] = True
                else:
                    if color == next_color: 
                        blind_queue.append((nx, ny, next_color))
                        blind_visited[nx][ny] = True


for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, painting[i][j])
            count+=1
        if not blind_visited[i][j]:
            blind_bfs(i, j, painting[i][j])
            blind_count+=1

print(count, blind_count)


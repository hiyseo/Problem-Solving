N, M = map(int, input().split())
tetromino = []
visited = [[False for _ in range(M)] for _ in range(N)]
for _ in range(N):
    tetromino.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
max_total = 0

def search(x, y, length, total):
    # print(f"x: {x}, y: {y}, length: {length}, value: {tetromino[x][y]}, total: {total}")
    global max_total
    visited[x][y] = True

    if length == 0:
        max_total = max(total, max_total)
        # print(f"max_total: {max_total}")
    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and length > 0:
            search(nx, ny, length-1, total+tetromino[nx][ny])
    
    visited[x][y] = False

def special_shape(x, y):
    global max_total
    shapes = [
        [(0, 1), (0, -1), (1, 0)], # ㅜ
        [(0, 1), (0, -1), (-1, 0)], # ㅗ
        [(1, 0), (-1, 0), (0, 1)], # ㅏ
        [(1, 0), (-1, 0), (0, -1)] # ㅓ
    ]
    
    for shape in shapes:
        total = tetromino[x][y]
        for dx, dy in shape:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M:
                # print(f"tetronomino[{x+dx}][{y+dy}]: {tetromino[x+dx][y+dy]}")
                total += tetromino[nx][ny]
        # print(f"special shape > x: {x}, y: {y}, value: {tetromino[x][y]}, total: {total}")
        max_total = max(max_total, total)
        # print(f"max_total: {max_total}")


for i in range(N):
    for j in range(M):
        # print(f"start searching tetromino[{i}][{j}], value: {tetromino[i][j]}")
        search(i, j, 3, tetromino[i][j])
        special_shape(i, j)
        
print(max_total)

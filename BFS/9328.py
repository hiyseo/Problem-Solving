from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    h, w = map(int, input().split())
    grid = [list(input().strip()) for _ in range(h)]
    keys_input = input().strip()
    keys = set(keys_input.lower()) - {'0'}

    visited = [[False]*w for _ in range(h)]
    q = deque()
    doors = [deque() for _ in range(26)]  # 각 문(A~Z)에 막혀있는 좌표 저장

    # 🔹 가장자리에서 BFS 시작 가능한 지점 수집
    def try_add(x, y):
        """현재 좌표가 탐색 가능한 경우 queue에 추가"""
        if visited[x][y] or grid[x][y] == '*':
            return
        cell = grid[x][y]
        visited[x][y] = True

        if 'A' <= cell <= 'Z':
            key_idx = ord(cell) - 65
            if chr(ord('a') + key_idx) in keys:
                grid[x][y] = '.'
                q.append((x, y))
            else:
                doors[key_idx].append((x, y))
        elif 'a' <= cell <= 'z':
            keys.add(cell)
            grid[x][y] = '.'
            q.append((x, y))
        else:
            q.append((x, y))

    for i in range(h):
        try_add(i, 0)
        try_add(i, w-1)
    for j in range(w):
        try_add(0, j)
        try_add(h-1, j)

    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    documents = 0

    while q:
        x, y = q.popleft()
        cell = grid[x][y]

        if cell == '$':
            documents += 1
            grid[x][y] = '.'

        # 네 방향 탐색
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if not (0 <= nx < h and 0 <= ny < w):
                continue
            if visited[nx][ny]:
                continue
            cell2 = grid[nx][ny]

            if cell2 == '*':  # 벽
                continue

            visited[nx][ny] = True

            if 'A' <= cell2 <= 'Z':
                key_idx = ord(cell2) - 65
                if chr(ord('a') + key_idx) in keys:
                    grid[nx][ny] = '.'
                    q.append((nx, ny))
                else:
                    doors[key_idx].append((nx, ny))

            elif 'a' <= cell2 <= 'z':
                # 새로운 키 획득
                if cell2 not in keys:
                    keys.add(cell2)
                    # 🔹 열 수 있게 된 문을 모두 큐에 추가
                    door_idx = ord(cell2) - 97
                    while doors[door_idx]:
                        dx2, dy2 = doors[door_idx].popleft()
                        grid[dx2][dy2] = '.'
                        q.append((dx2, dy2))
                grid[nx][ny] = '.'
                q.append((nx, ny))

            else:
                q.append((nx, ny))

    print(documents)
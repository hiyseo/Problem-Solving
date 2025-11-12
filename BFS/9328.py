# # 가장자리에서 드나들 수 있는 지점 찾는 함수
# # 대문자 알파벳을 만나면, 만약 열쇠가 있다면 그대로, 없다면 candidates에 [(x, y), 'B'] 형태로 저장
# # 다음 이동할 수 있는 지점을 큐에 넣기
# # 아니면, key찾으면 해당 key에 해당하는 door 전부 '.'으로 바꾸기

# # 큐에서 BFS로 탐색, 처음에 키를 가지고 있으면 해당 문을 모두 '.'으로 바꿈

# h_alphs = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# l_alphs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# from collections import deque

# t = int(input())

# for _ in range(t):
#     keys = set()
#     doors = {} # 딕셔너리 doors['X'] = [(x, y), .. ]
#     queue = deque() # ((x, y), '.') or ((x, y), 'X') 형식으로 큐에 저장

#     h, w = map(int, input().split())
#     buildings = []
#     candidates = {} # 갈 수는 있지만, 현재 키가 없어서 못가는 위치 - 나중에 키를 찾으면 큐로 이동
#     visited = [[False for _ in range(w)] for _ in range(h)]
#     for i in range(h):
#         floor = list(input())
#         if i == 0 or i == h-1: # 맨 위 or 맨 아래
#             for j in range(w):
#                 f = floor[j]
#                 if f == '.' or f == '$':
#                     queue.append(((i, j), f))
#                 elif f in h_alphs: # 대문자
#                     if f not in doors:
#                         doors[f] = []
#                     doors[f].append((i, j))
#                 elif f in l_alphs: # 소문자
#                     if f not in keys: keys.add(f)
#                     queue.append(((i, j), '.'))
#         else:
#             for j in range(w):
#                 f = floor[j]
#                 if f in h_alphs: # 대문자
#                     if f not in doors:
#                         doors[f] = []
#                     doors[f].append((i, j))

#                 if j == 0 or j == w-1: # 맨 앞이거나 맨 뒤
#                     if f == '.' or f == '$':
#                         queue.append(((i, j), f))
#                     elif f in l_alphs: # 소문자
#                         if f not in keys: keys.add(f)
#                         queue.append(((i, j), '.'))
        
#         buildings.append(floor)

#     words = list(input())
#     for word in words:
#         if word == '0': break
#         if word not in keys: keys.add(word)
    
#     for key in keys:
#         # print(f"key: {key}")
#         idx = l_alphs.index(key)
#         if h_alphs[idx] in doors: # 대문자 처리
#             for x, y in doors[h_alphs[idx]]:
#                 buildings[x][y] = '.'
#                 if x == 0 or x == h-1:
#                     queue.append(((x, y), '.'))
#                 elif y == 0 or y == w-1:
#                     queue.append(((x, y), '.'))
    
#     # print(f"buildngs: {buildngs}")
#     # print(f"queue: {queue}")
#     # print(f"keys: {keys}")
#     # print(f"doors: {doors}")
    
#     ############# 처음 starting 끝남 ##############

#     total = 0 # 우리가 구해야 하는 값
#     dx = [-1, 0, 1, 0]
#     dy = [0, -1, 0, 1]

#     # 처음 시작하는 부분 visited 처리
#     for tp in queue:
#         cx, cy = tp[0]
#         visited[cx][cy] = True

#     while queue:
#         # print(f"queue: {queue}")
#         # print(f"candidates: {candidates}")
#         tp = queue.popleft() # ((x, y), '.')
#         cx, cy = tp[0]
#         val = tp[1] # '.' or '$'
#         if val == '$':
#             total += 1
#         for i in range(4):
#             nx, ny = cx + dx[i], cy + dy[i]
#             if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
#                 nval = buildings[nx][ny]
#                 if nval == '.' or nval == '$':
#                     visited[nx][ny] = True
#                     queue.append(((nx, ny), nval))
#                 elif nval in h_alphs: # 대문자라는 것은 -> 아직 해당 키가 발견되지 않았다는 뜻
#                     if nval not in candidates:
#                         candidates[nval] = []
#                     candidates[nval].append((nx, ny))
#                 elif nval in l_alphs: 
#                     if nval not in keys: # 처음 발견한 키
#                         keys.add(nval)
#                         idx = l_alphs.index(nval)
#                         if h_alphs[idx] in doors:
#                             for x, y in doors[h_alphs[idx]]:
#                                 buildings[x][y] = '.'
                        
#                         if h_alphs[idx] in candidates:
#                             for posx, posy in candidates[h_alphs[idx]]:
#                                 visited[posx][posy] = True
#                                 queue.append(((posx, posy), '.'))
                        
#                     visited[nx][ny] = True
#                     queue.append(((nx, ny), '.'))
                    
                        
#     print(total)

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
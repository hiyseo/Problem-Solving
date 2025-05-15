# 보물섬 지도에서 각각의 L에 대하여
# BFS로 전파
# 한번의 전파에서 가장 큰 값 vs max

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def find_treasure():
    global max
    while res:
        # print(f"res: {res}")
        x, y, cnt = res.popleft()
        max = max if max > cnt else cnt
        # print(f"x: {x}, y: {y}, cnt: {cnt}")
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                if treasure_map[nx][ny]=='L':
                    visited[nx][ny]=True
                    res.append((nx, ny, cnt+1))

N, M = map(int, input().split())
treasure_map = []

# print(visited)
for i in range(N):
    treasure_map.append(list(input()))

max = float('-inf')
for i in range(N):
    for j in range(M):
        if treasure_map[i][j]=='L':
            res = deque()
            visited = [[False for _ in range(M)]for _ in range(N)]
            res.append((i, j, 0))
            visited[i][j]=True
            find_treasure()
            # print(f"=== DONE SEARCHING ===")

if max == float('-inf'):
    print(0)
else: print(max)

### 테스트케이스 ###
# 3 3
# LLL
# LLL
# LLL
# 5

# 4 4
# LLWL
# LWLL
# LLWL
# LWLL
# 5

# 4 4
# LWLL
# LLLW
# LLWW
# LLLL
# 7

# 4 4
# LLWL
# LWLL
# LLWL
# LLLL
# 10

# 4 4
# LLLL
# LWWL
# LWWL
# LLLL
# 7

# 7 7
# WLLLLLW
# LWLWLWW
# LLLWLWW
# LWWWLWW
# LLLLLWW
# LWWWWWW
# WWWWWWW
# 10
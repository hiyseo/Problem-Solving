N, M = map(int, input().split())
MAP = []
VISITED = []
TOTAL = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for _ in range(N):
    lst = list(map(int, input().split()))
    # lst2 = [0 for _ in range(M)]
    MAP.append(lst)
    # VISITED.append(lst2)

def print_map(list):
    for i in range(N):
        print(list[i])

def count_map(list):
    total=0
    for i in range(N):
        for j in range(M):
            if list[i][j] == 0:
                total+=1
    return total

def propagation(x, y, VISITED):
    VISITED[x][y]=1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M:
            if MAP[nx][ny]==0 and VISITED[nx][ny] == 0:
                MAP[nx][ny]=3
                propagation(nx, ny, VISITED)

## propagation testing ##
# MAP[0][2]=1
# MAP[4][2]=1
# MAP[3][4]=1

def map_propagation():
    VISITED = [[0 for _ in range(M)] for _ in range(N)]
    # print(VISITED)
    for i in range(N):
        for j in range(M):
            # print(f"i: {i}, j: {j}")
            if MAP[i][j]==2 and VISITED[i][j]==0:
                propagation(i, j, VISITED)
    TOTAL.append(count_map(MAP))
    for i in range(N):
        for j in range(M):
            # print(f"i: {i}, j: {j}")
            if MAP[i][j]==3:
                MAP[i][j]=0

def make_wall(cnt):
    if cnt==3:
        # print(print_map(MAP))
        # print("START PROPAGATION")
        map_propagation()
        return
    for i in range(N):
        for j in range(M):
            if MAP[i][j]==0:
                MAP[i][j]=1
                # print(f"i: {i}, j: {j}")
                make_wall(cnt+1)
                MAP[i][j]=0

# print_map(MAP)
# print("---------------------")
# print_map(VISITED)
# print("---------------------")
# print(TOTAL)

# print("processing.......")
make_wall(0)
print(max(TOTAL))
NUM = int(input())
for _ in range(NUM):
    M, N, K = map(int, input().split())
    BACHU = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        BACHU[y][x]=1

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    total = 0

    def search(x, y):
        # print(f"x: {x}, y: {y} visited")
        BACHU[y][x]=0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<M and 0<=ny<N and BACHU[ny][nx]==1:
                search(nx, ny)

    for i in range(N):
        for j in range(M):
            if BACHU[i][j]==1:
                # print(f"x: {j}, y: {i} searched")
                search(j, i)
                total+=1

    print(total)
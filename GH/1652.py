# def check_x(lst) -> int:
# 가로로 누울 자리를 계산하는 함수

# def check_y(lst) -> int:
# 세로로 누울 자리를 계산하는 함수

def check_x(lst) -> int:
    res = 0
    for i in range(N):
        flag = 0
        for j in range(N-1):
            if lst[i][j] == "." and lst[i][j+1] == "X": 
                if flag==1:
                    res+=1
                    flag = 0
            if lst[i][j] == lst[i][j+1] == ".":
                if j==N-2: res+=1
                flag = 1
                # print(f"res: {res}")
                # break
    return res

def check_y(lst) -> int:
    res = 0
    for j in range(N):
        flag = 0
        for i in range(N-1):
            if lst[i][j] == "." and lst[i+1][j] == "X":
                if flag==1:
                    res+=1
                    flag = 0
            if lst[i][j] == lst[i+1][j] == ".":
                if i==N-2: res+=1
                flag = 1
                # print(f"res: {res}")
                # break
    return res

global N 
N = int(input())
room = []
for i in range(N):
    room.append(list(input()))

X = check_x(room)
Y = check_y(room)
print(X, Y)

# 테스트케이스
# 3
# ..X
# ...
# ...
# 3 3

# 3
# X.X
# .X.
# X.X
# 0 0

# 1
# X
# 0 0

# 1
# .
# 0 0

# 2
# XX
# XX
# 0 0

# 2
# ..
# .X
# 1 1

# 5
# .....
# ..X..
# X...X
# ..X..
# .....
# 7 6

# 6
# X..X..
# ..X...
# .X..XX
# X.....
# ..XX..
# .X....
# 9 10
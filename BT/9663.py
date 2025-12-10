N = int(input())

col = [0 for _ in range(N)] # 해당 열에 퀸이 있는지
diag1 = [0 for _ in range(2*N)] # 우하향 대각선 - row & col 합계가 일정
diag2 = [0 for _ in range(2*N)] # 우상향 대각선 - row & col 차이가 일정

answer = 0

def dfs(row):
    '''
    row 어느 곳에 퀸을 둘지 검사하는 함수
    '''
    global answer

    if row == N:
        answer += 1
        return
    
    for c in range(N): # 모든 column에 대해서 검사
        if not col[c] and not diag1[row+c] and not diag2[N-(row-c)]: # 해당 칸의 열, 대각선에 모두 퀸이 없을때
            col[c] = diag1[row+c] = diag2[N-(row-c)] = 1
            dfs(row+1)
            col[c] = diag1[row+c] = diag2[N-(row-c)] = 0
    
dfs(0)
print(answer)


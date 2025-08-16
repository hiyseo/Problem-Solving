# 스도쿠는 매우 간단한 숫자 퍼즐이다. 9×9 크기의 보드가 있을 때, 각 행과 각 열, 그리고 9개의 3×3 크기의 보드에 1부터 9까지의 숫자가 중복 없이 나타나도록 보드를 채우면 된다. 

# 위 그림은 참 잘도 스도쿠 퍼즐을 푼 경우이다. 
# 각 행에 1부터 9까지의 숫자가 중복 없이 나오고, 각 열에 1부터 9까지의 숫자가 중복 없이 나오고, 각 3×3짜리 사각형(9개이며, 위에서 색깔로 표시되었다)에 1부터 9까지의 숫자가 중복 없이 나오기 때문이다.
# 하다 만 스도쿠 퍼즐이 주어졌을 때, 마저 끝내는 프로그램을 작성하시오.

# 입력
# 9개의 줄에 9개의 숫자로 보드가 입력된다. 아직 숫자가 채워지지 않은 칸에는 0이 주어진다.

# 출력
# 9개의 줄에 9개의 숫자로 답을 출력한다. 답이 여러 개 있다면 그 중 사전식으로 앞서는 것을 출력한다. 즉, 81자리의 수가 제일 작은 경우를 출력한다.

### 수도코드 ###
# 검사 3가지
# 1. 가로
# 2. 세로
# 3. 3*3
# 해당 검사 수행 -> 가능한 숫자 목록들 중 작은 것부터 -> 숫자 놓고 -> 다음 칸으로(재귀) -> 숫자 제거
import sys

LST = [list(map(int, input())) for _ in range(9)]
checklists = []
for i in range(9):
    for j in range(9):
        if LST[i][j]==0: checklists.append((i, j))

def print_lst():
    """
    LST 출력하는 함수
    """
    for i in range(9):
        for j in LST[i]:
            print(j, end='')
        print()
    

def is_valid(x: int, y: int, target: int) -> bool:
    """
    target을 lst[x][y]에 넣을 수 있는지 검사
    """
    if target in LST[x]:
        return False
    
    for i in range(9):
        if target == LST[i][y]:
            return False

    for i in range((x//3)*3, (x//3)*3+3):
        for j in range((y//3)*3, (y//3)*3+3):
            if target == LST[i][j]: 
                return False
    
    return True

def solve(idx: int):
    if idx == len(checklists):
        print_lst()
        sys.exit(0)

    x, y = checklists[idx]
    for num in range(1, 10):
        if is_valid(x, y, num):
            LST[x][y] = num
            solve(idx+1)
            LST[x][y] = 0

# print()
# print("="*9)
# print()

solve(0)

### 테스트케이스 1 ###
# 103000509
# 002109400
# 000704000
# 300502006
# 060000050
# 700803004
# 000401000
# 009205800
# 804000107

### 정답 ###
# 143628579
# 572139468
# 986754231
# 391542786
# 468917352
# 725863914
# 237481695
# 619275843
# 854396127
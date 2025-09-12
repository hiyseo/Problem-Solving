### 수도코드 ###
# 전체 배열을 입력받고, 구간 검사??
# 시간복잡도: O(N^3)
# top down, bottom up 방식이 있을 것 같은데
# top down으로 가보자

def check(sx: int, sy: int, ex: int, ey: int) -> tuple:
    """
    start ~ end-1 구간까지 모든 요소가 같은지 검사하는 함수
    """
    flag = True
    s = MAP[sx][sy]
    for i in range(sx, ex):
        if not flag: break
        for j in range(sy, ey):
            if MAP[i][j] != s:
                flag = False
                break
    return (flag, s)

def fold_paper(sx: int, sy: int, n: int):
    """
    n만큼 종이접기 수행 후 유효한 개수 리턴
    """
    global res1, res2
    # print(f"sx: {sx}, sy: {sy}, n: {n}, res1: {res1}, res2: {res2}")
    if n<1: return
    n = n//2
    ta, tb, tc, td = check(sx, sy, sx+n, sy+n), check(sx+n, sy, sx+2*n, sy+n), check(sx, sy+n, sx+n, sy+2*n),check(sx+n, sy+n, sx+2*n, sy+2*n)
    if not ta[0]:
        fold_paper(sx, sy, n)
    else:
        if ta[1] == 0: res1+=1
        else: res2+=1

    if not tb[0]:
        fold_paper(sx+n, sy, n)
    else:
        if tb[1] == 0: res1+=1
        else: res2+=1

    if not tc[0]:
        fold_paper(sx, sy+n, n)
    else:
        if tc[1] == 0: res1+=1
        else: res2+=1

    if not td[0]:
        fold_paper(sx+n, sy+n, n)
    else:
        if td[1] == 0: res1+=1
        else: res2+=1
    

N = int(input())
MAP = []
res1, res2 = 0, 0 #res1: 하얀색, res:2 파란색

for _ in range(N):
    MAP.append(list(map(int, input().split())))
# print(f"MAP: {MAP}")

fold_paper(0, 0, N)
if res1 == 0:
    res2 = 1
elif res2 == 0:
    res1 = 1

print(res1)
print(res2)

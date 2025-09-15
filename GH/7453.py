### 수도코드 ###
# 1 <= n <= 4000
# A, B, C, D의 각 숫자들의 합이 0이 되는 순서쌍의 개수
# 브루트포스 -> 4000 * 4000 * 4000 * 4000
# A, B & C, D 묶음으로 처리하고 (합) 각각 정렬 후 비교하면?

# 딕셔너리 삽입 / 탐색이 여러번 -> 파이썬 해시 오버헤드가 누적
# 정렬 후 투포인터

n = int(input())
A, B, C, D = [], [], [], []
res = 0
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

lst_ab, lst_cd = [], []
for i in range(n):
    for j in range(n):
        lst_ab.append(A[i] + B[j])
        lst_cd.append(C[i] + D[j])

lst_ab.sort()
lst_cd.sort()

left, right = 0, len(lst_cd)-1
while left < len(lst_ab) and right >= 0:
    s = lst_ab[left] + lst_cd[right]
    if s == 0:
        val_ab, val_cd = lst_ab[left], lst_cd[right]
        cnt_ab, cnt_cd = 0, 0
        while left < len(lst_ab) and lst_ab[left] == val_ab:
            left+=1
            cnt_ab+=1
        while right >=0 and lst_cd[right] == val_cd:
            right-=1
            cnt_cd+=1
        res += cnt_ab*cnt_cd
    elif s < 0:
        left+=1
    else:
        right-=1

print(res)
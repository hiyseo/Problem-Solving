n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

# 1. A+B, C+D의 모든 조합 합 구하기 (O(n^2))
AB, CD = [], []
for i in range(n):
    for j in range(n):
        AB.append(A[i] + B[j])
        CD.append(C[i] + D[j])

# 2. 정렬 (O(n^2 log n))
AB.sort()
CD.sort()

# 3. 투포인터 탐색 (O(n^2))
res = 0
i, j = 0, len(CD) - 1
while i < len(AB) and j >= 0:
    s = AB[i] + CD[j]
    if s == 0:
        # 같은 값 개수 세기
        ab_val = AB[i]
        cd_val = CD[j]
        cnt_ab = cnt_cd = 0

        while i < len(AB) and AB[i] == ab_val:
            cnt_ab += 1
            i += 1
        while j >= 0 and CD[j] == cd_val:
            cnt_cd += 1
            j -= 1
        res += cnt_ab * cnt_cd

    elif s < 0:
        i += 1
    else:
        j -= 1

print(res)
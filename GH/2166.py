# 문제
# 2차원 평면상에 N(3 ≤ N ≤ 10,000)개의 점으로 이루어진 다각형이 있다. 이 다각형의 면적을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. 다음 N개의 줄에는 다각형을 이루는 순서대로 N개의 점의 x, y좌표가 주어진다. 좌표값은 절댓값이 100,000을 넘지 않는 정수이다.

# 출력
# 첫째 줄에 면적을 출력한다. 면적을 출력할 때에는 소수점 아래 둘째 자리에서 반올림하여 첫째 자리까지 출력한다.

N = int(input())
lst_x, lst_y = [], []
total = 0

for _ in range(N):
    x, y = map(int, input().split())
    lst_x.append(x)
    lst_y.append(y)

lst_x.append(lst_x[0])
lst_y.append(lst_y[0])

# print(f"lst_x: {lst_x}")
# print(f"lst_y: {lst_y}")


for i in range(N):
    tmp = (lst_x[i]*lst_y[i+1] - lst_x[i+1]*lst_y[i])
    total+=tmp

total = 0.5*abs(total)
print(round(total, 1))



### 테스트케이스 ###
# 4
# 0 0
# 0 10
# 10 10
# 10 0

# 100.0
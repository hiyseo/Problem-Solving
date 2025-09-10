### 수도코드 ###
# 2 <= N <= 100000
# 가장 처음에 드는 생각은, O(N^2) -> 시간복잡도 10^10 (시간 초과)
# 오른차순으로 정렬되어 있으므로,
# left, right 투포인터로 인덱스 이동하면서 검사

# 왼쪽 한칸 이동
# 오른쪽 한칸 이동
# 양쪽 한칸씩 이동

N = int(input())
numbers = list(map(int, input().split()))
MIN = float('inf')
res1, res2 = 0, 0
left, right = 0, N-1

while left < right:
    num1, num2 = numbers[left], numbers[right]
    gap = abs(num1 + num2)

    MIN = MIN if MIN < gap else gap

    if MIN == gap: # MIN이 업데이트 되면
        res1, res2 = num1, num2

    gap1 = abs(numbers[left+1] + numbers[right])
    gap2 = abs(numbers[left] + numbers[right-1])

    if gap1 >= gap2:
        right -= 1

    elif gap1 < gap2:
        left += 1

    else:
        left += 1
        right -= 1

print(res1, res2)


### 테스트케이스 ###
# 5
# -99 -10 -5 1 10
# 답: 0

# 7
# -100 -80 -10 1 9 10 50
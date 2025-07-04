# 상근이와 선영이는 학교 숙제로 로봇을 만들고 있다. 로봇을 만들던 중에 구멍을 막을 두 레고 조각이 필요하다는 것을 깨달았다.
# 구멍의 너비는 x 센티미터이고, 구멍에 넣을 두 조각의 길이의 합은 구멍의 너비와 정확하게 일치해야 한다. 
# 정확하게 일치하지 않으면, 프로젝트 시연을 할 때 로봇은 부수어질 것이고 상근이와 선영이는 F를 받게 된다. 구멍은 항상 두 조각으로 막아야 한다.
# 지난밤, 상근이와 선영이는 물리 실험실에 들어가서 레고 조각의 크기를 모두 정확하게 재고 돌아왔다. 구멍을 완벽하게 막을 수 있는 두 조각을 구하는 프로그램을 작성하시오.

# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
# 각 테스트 케이스의 첫째 줄에는 구멍의 너비 x (1 ≤ x ≤ 20, x는 정수)가 주어진다. x의 단위는 센티미터이다.
# 다음 줄에는 물리 실험실에 있는 레고 조각의 수 n이 주어진다. (0 ≤ n ≤ 1000000)
# 다음 n개의 줄에는 레고 조각의 길이 ℓ이 주어진다. ℓ은 양의 정수이며, 단위는 나노미터이다. 블록의 길이는 10 센티미터 (100000000 나노미터)를 넘지 않는다.

# 각 테스트 케이스마다 한 줄에 하나씩, 구멍을 완벽하게 막을 수 있는 두 조각이 없다면 'danger'를 출력한다. 막을 수 있는 경우에는 'yes ℓ1 ℓ2'를 출력한다. (ℓ1 ≤ ℓ2)
# 정답이 여러 개인 경우에는 |ℓ1 - ℓ2|가 가장 큰 것을 출력한다.

# 예제 입력 1 
# 1
# 4
# 9999998
# 1
# 2
# 9999999

# 예제 출력 1 
# yes 1 9999999

### 수도코드 ###
# 구멍의 너비(x) 입력 (1 ≤ x ≤ 20)
# nano_x = x*=10000000
# l1, l2, mx_gap 선언
# flag = 0 (1: yes, 0: no)
# 레고 조각의 수(n) 입력 (0 ≤ n ≤ 1000000)
# legos = []
# lego = int(input())
# if lego<nano_x: legos.append(lego)
# legos 안에 2요소의 합이 nano_x라면 -> 이거를 어떻게 할지!!
# mx_gap 값 비교 후 간격이 더 크다면, l1, l2, mx_gap 업데이트
# flag == 1이라면, 'yes l1 l2' 출력
# flag == 0이라면, 'danger' 출력

# 문제 - 시간 복잡도에서 걸림


# 해결 방법
# 레고 조각의 수 - 최대 100,0000
# O(nlogn)으로 해결해야함
# First Try: set()을 사용, 시간복잡도: O(n)-> 메모리 부족
# Second Try: 정렬 && 투포인터, 시간복잡도: O(nlogn + n) -> O(nlogn)


while True:
    try:
        x = int(input())
        nano_x = x*(10**7)
        l1, l2 = -1, -1
        flag = 0 # 1: yes 0: danger
        n = int(input())
        legos = [int(input()) for _ in range(n)]

        legos.sort() #O(nlogn)
        left, right = 0, n-1
        while left < right:
            curr_sum = legos[left] + legos[right]
            if curr_sum == nano_x:
                l1, l2 = legos[left], legos[right]
                flag = 1
                break
            elif curr_sum < nano_x:
                left+=1
            else:
                right-=1
        if flag == 1: print(f"yes {l1} {l2}")
        else: print("danger")
    except:
        break

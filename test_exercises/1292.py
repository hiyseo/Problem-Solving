# 1000개 배열 생성
# 구간에서의 합 구하기

def generate_list(limit)->list:
    sequence = []
    N=1
    while len(sequence)<limit:
        sequence.extend([N]*N)
        N+=1
    return sequence[:limit]

lst = generate_list(1000)
A, B = map(int, input().split())
# print(f"A: {A}, B: {B}")
print(sum(lst[A-1:B]))

# 이진탐색 -> 숫자가 정렬되어 있을때 시간복잡도 O(logN)
def find_position(n)->int:
    left, right = 1, 1000
    while left<right:
        mid = (left+right)//2
        if mid*(mid+1)//2 >= n:
            right = mid
        else:
            left = mid+1
    return left
    
print(find_position(7))
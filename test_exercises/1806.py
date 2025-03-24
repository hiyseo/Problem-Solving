# N, S 입력
# numbers = [숫자 입력 받음]
# start = 0, end = 0, sum = 0, min_len = float('inf)
# end 확장하면서 sum 저장
# sum > S 라면
# start 줄임

N, S = map(int, input().split())
# print(f"N: {N}, S: {S}")
numbers = list(map(int, input().split()))
# print(f"numbers: {numbers}")
start, end, sum = 0, 0, 0
min_len = float('inf')

while end<N:
    # print(f"start: {start}, end: {end}")
    sum+=numbers[end]
    end+=1
    while sum >= S:
        min_len = min(min_len, end-start)
        # print(f"min_len: {min_len}")
        sum-=numbers[start]
        start+=1

if min_len == float('inf'): print(0)
else: print(min_len)
N = int(input())
DP_min = []
DP_max = []

def min_two(a, b):
    if a<=b:
        return a
    else:
        return b
    
def max_two(a, b):
    if a>=b:
        return a
    else:
        return b

def min_three(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= c and b <= a:
        return b
    else:
        return c

def max_three(a, b, c):
    if a>=b and a>=c:
        return a
    elif b>=c and b>=a:
        return b
    else:
        return c

for i in range(N):
    if i==0:
        lst = list(map(int, input().split()))
        DP_min.append(lst)
        DP_max.append(lst)
    else:
        prev_a, prev_b, prev_c = DP_min.pop()
        # print(f"prev_a: {prev_a}, prev_b: {prev_b}, prev_c: {prev_c}")
        prev_A, prev_B, prev_C = DP_max.pop()
        # print(f"prev_A: {prev_A}, prev_B {prev_B}, prev_C: {prev_C}")
        cur_a, cur_b, cur_c = map(int, input().split())
        # print(f"cur_a: {cur_a}, cur_b: {cur_b}, cur_c: {cur_c}")
        min_first, min_mid, min_last = min_two(prev_a, prev_b)+cur_a, min_three(prev_a, prev_b, prev_c)+cur_b, min_two(prev_b, prev_c)+cur_c
        max_first, max_mid, max_last = max_two(prev_A, prev_B)+cur_a, max_three(prev_A, prev_B, prev_C)+cur_b, max_two(prev_B, prev_C)+cur_c
        DP_min.append([min_first, min_mid, min_last])
        DP_max.append([max_first, max_mid, max_last])
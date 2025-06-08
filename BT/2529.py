N = int(input())
signs = list(input().split())
used = [False for _ in range(10)]
max_val = ''
min_val = ''
# print(f"signs: {signs}")

def is_valid(a, b, sign) -> bool:
    if sign == '<':
        return a<b
    elif sign == '>':
        return a>b

def find_numbers(depth, curr):
    global max_val, min_val
    # print(f"depth: {depth}, curr: {curr}")
    # print(f"used: {used}")
    if depth==N+1: # 마지막까지 오면
        # print(f"DEPTH is {N+1}!! CHECKING MAX & MIN")
        # print(f"max_val: {max_val}, min_val: {min_val}, curr: {curr}")
        if max_val: max_val = max_val if int(max_val) > int(curr) else curr
        else: max_val = curr

        if min_val: min_val = min_val if int(min_val) < int(curr) else curr
        else: min_val = curr
        # print(f"max_val: {max_val}, min_val: {min_val}")
        return
    for i in range(len(used)):
        if curr:
            lst = list(curr)
            # print(f"lst: {lst}")
            l = len(lst)
            prev, next = int(lst[l-1]), i
            curr_sign = signs[l-1]
            if not used[i] and is_valid(prev, next, curr_sign):
                # print(f"prev: {prev}, next: {next}, curr_sign: {curr_sign}")
                used[i] = True
                # print(f"inserting {i}!!")
                find_numbers(depth+1, curr+str(i))
                used[i] = False
        else:
            used[i] = True
            find_numbers(depth+1, curr+str(i))
            used[i] = False

find_numbers(0, '')
print(f"max_val: {max_val}")
print(f"min_val: {min_val}")

# input
# 2
# < >

# output
# 897 - 최대
# 021 - 최소

# input
# 9
# > < < < > > > < <

# output
# 9567843012 - 최대
# 1023765489 - 최소
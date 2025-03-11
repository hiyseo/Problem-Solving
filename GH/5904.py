N = int(input())
moo_list = []
moo_list.append(3) # s(0)
while True:
    cur = len(moo_list)
    if N<=moo_list[cur-1]:
        # print(moo_list)
        # print(f"cur: {cur}")
        break
    next_moo = moo_list[cur-1]*2+(cur+3)
    moo_list.append(next_moo)
    # print(f"next_moo: {next_moo}")

def find_index(num) -> int:
    for i in range(len(moo_list)):
        if num<=moo_list[0]:
            return 0
        elif num>moo_list[i-1] and num<=moo_list[i]:
            return i

# Find the lowest moo
def find_moo(num) -> int:
    # print("=====================")
    # print(f"num: {num}")
    index = find_index(num) # num이 위치한 index 찾기
    # print(f"index: {index}")
    if index==0: # s(0)인 경우
        if num == 1:
            return print("m")
        else:
            return print("o")
        
    pre_val = moo_list[index-1]
    next = pre_val+index+3 # 이전값+가운데값
    # print(f"pre_val: {pre_val}")
    
    if num > pre_val and num <= next: # moooooooooo (가운데 값)
        if num-pre_val == 1:
            return print("m")
        else:
            return print("o")
    else:
        # print(f"next: {next}")
        return find_moo(num-next)

find_moo(N)
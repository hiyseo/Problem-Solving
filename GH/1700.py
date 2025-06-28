# 멀티탭 구멍 개수(N), 전기용품 사용회수(K) 입력
# 전기용품 사용순서 리스트(orders) 선언
# 사용 중인 리스트(used) 선언
# res = 0
# remained = K
# orders[i]가 used에 있는지 확인 -> 있다면 cotinue, 없다면 아래 실행
# remained > 0이라면, used.append(orders[i]) & remained-=1
# remained <= 0이라면, 가장 오래 사용되지 않을 전기용품 선택 & 교체, res +=1

# select 알고리즘
# 빈 리스트(res) 선언
# lst1에서 하나씩 선택 후, target = lst1[i]
# lst2에서 target이 처음 나오는 위치(j) 저장
# res.append((i, j))
# 모든 res[1] 중에서 가장 수가 큰 res[0] 반환

def select(lst1, lst2):
    # print(f"selecting...")
    ret = 0
    max = float('-inf')
    for i in range(len(lst1)):
        flag = 0 # 1이면 같은 숫자 발견, 0이면 발견 못함
        target = lst1[i]
        for j in range(len(lst2)):
            if target == lst2[j]:
                flag = 1
                max = max if max > j else j
                if max == j:
                    # print(f"finding max: {max}")
                    ret = i
                break
        if flag == 0: # 뒤에 해당 전자기기가 사용되지 않는 경우
            ret = i
            break
    # print(f"max: {max}, ret: {ret}")
    return ret



N, K = map(int, input().split())
orders = list(map(int, input().split()))
# print(f"orders: {orders}")
used = []
res, remained = 0, N
for i in range(len(orders)):
    curr = orders[i]
    # print(f"curr: {curr}")
    if curr in used: continue
    else:
        # print(f"remained: {remained}, used: {used}")
        if remained > 0:
            used.append(curr)
            remained-=1
        else:
            if i<len(orders)-1:
                tmp = []
                for j in range(i+1, len(orders)):
                    tmp.append(orders[j])
                idx = select(used, tmp)
                # print(f"deleting {used[idx]}...")
                del used[idx]
                used.append(curr)
                # print(f"appending {curr}...")
            res+=1
            # print(f"res: {res}")

print(res)
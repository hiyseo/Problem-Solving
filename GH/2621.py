def c_1(lst) -> int:
    res = []
    for i in range(len(lst)):
        res.append(lst[i][1])
    return max(res)+900

def c_2(a) -> int:
    return 800 + a

def c_3(a, b) -> int:
    return 10*a+b+700

def c_4(lst) -> int:
    res = []
    for i in range(len(lst)):
        res.append(lst[i][1])
    return max(res)+600

def c_5(lst) -> int:
    res = []
    for i in range(len(lst)):
        res.append(lst[i][1])
    return max(res)+500

def c_6(a) -> int:
    return 400+a

def c_7(a, b) -> int:
    return 10*a+b+300

def c_8(a) -> int:
    return 200+a

def c_9(lst) -> int:
    res = []
    for i in range(len(lst)):
        res.append(lst[i][1])
    return max(res)+100

def check_continuous(lst) -> bool:
    lst.sort()
    for i in range(len(lst)-1):
        if lst[i+1] == lst[i]+1: continue
        else: return False
    return True

cards = []
num_cards = []
color_cards = []
dict_color = {}
dict_num = {}
for _ in range(5):
    color, number = map(str, input().split())
    x = (color, int(number))
    # print(f"color: {color}, number: {number}")
    cards.append(x)

for i in range(len(cards)):
    c = cards[i][0]
    if c not in dict_color: dict_color[c] = 1
    else: dict_color[c]+=1

for i in range(len(cards)):
    n = cards[i][1]
    if n not in dict_num: dict_num[n] = 1
    else: dict_num[n]+=1

for key in dict_color:
    color_cards.append(key)

for key in dict_num:
    num_cards.append(key)

# print(f"num_cards: {num_cards}")
# print(f"color_cards: {color_cards}")
# print(f"dict_color: {dict_color}")
# print(f"dict_num: {dict_num}")

flag_color, flag_num = 0, 0
# flag_color = 1: 5개 모두 같음
# flag_num = 1: 연속적, 2: 4개 숫자 같음, 3: 3개 & 2개 같음, 4: 3개 같음, 5: 2개 & 2개 같음, 6: 2개 같음
ret_num1, ret_num2 = 0, 0

if len(color_cards) == 1: flag_color = 1

if len(num_cards) == 5 and check_continuous(num_cards): flag_num = 1
elif len(num_cards) == 2:
    for key in dict_num:
        if dict_num[key]==4:
            flag_num = 2
            ret_num1 = key
        if dict_num[key]==3:
            flag_num = 3
            ret_num1 = key
        if dict_num[key]==2:
            flag_num = 3
            ret_num2 = key
elif len(num_cards)==3:
    tmp = []
    for key in dict_num:
        if dict_num[key] == 3:
            flag_num = 4
            ret_num1 = key
        if dict_num[key] == 2:
            tmp.append(key)
    if len(tmp)==2:
        flag_num = 5
        ret_num1, ret_num2 = max(tmp), min(tmp)
elif len(num_cards)==4:
    for key in dict_num:
        if dict_num[key] == 2:
            flag_num = 6
            ret_num1 = key
else: flag_num = 0

# print(f"flag_color: {flag_color}, flag_num: {flag_num}, ret_num1: {ret_num1}, ret_num2: {ret_num2}")

res = []
if flag_color == 1 and flag_num == 1: res.append(c_1(cards))
if flag_num == 2: res.append(c_2(ret_num1))
if flag_num == 3: res.append(c_3(ret_num1, ret_num2))
if flag_color == 1 and flag_num != 1: res.append(c_4(cards))
if flag_color != 1 and flag_num ==1: res.append(c_5(cards))
if flag_num == 4: res.append(c_6(ret_num1))
if flag_num == 5: res.append(c_7(ret_num1, ret_num2))
if flag_num == 6: res.append(c_8(ret_num1))
else: res.append(c_9(cards))

print(max(res))


### 테스트 케이스 ###
# B 1
# B 2
# B 3
# B 4
# B 5
# 905

# B 2
# R 2
# Y 2
# G 2
# B 5
# 802

# B 3
# R 3
# G 3
# Y 2
# B 2
# 732

# B 3
# B 2
# B 6
# B 7
# B 1
# 607

# B 3
# B 3
# B 3
# B 2
# B 2
# 732 vs 603

# B 2
# R 3
# G 6
# Y 4
# B 5
# 506

# B 4
# R 4
# Y 4
# B 3
# G 2
# 404

# B 5
# Y 5
# R 2
# G 2
# G 7
# 352

# B 5
# G 5
# R 4
# Y 1
# G 3
# 205
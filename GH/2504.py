letters = list(input())
STACK = []
FLAG = 1
for letter in letters:
    # print(f"FLAG: {FLAG}")
    if FLAG == 0:
        break
    # print(f"letter: {letter}")
    if letter=="(" or letter=="[":
        STACK.append(letter)
        # print(f"STACK: {STACK}")
    elif letter==")":
        total = 0
        temp = []
        while True:
            if len(STACK)==0:
                FLAG = 0
                break
            top = STACK.pop()
            # print(f"top: {top}")
            if top=="(":
                if len(temp)==0:
                    total=2
                else:
                    for num in temp:
                        total+=num
                    total = total*2
                # print(f"total: {total}")
                STACK.append(total)
                # print(f"STACK: {STACK}")
                break
            elif top==")" or top=="[" or top=="]": # 잘못된 문자열인 경우
                FLAG = 0
                break
            else: # top이 숫자인 경우
                temp.append(top)
    elif letter=="]":
        if len(STACK)==0:
            FLAG = 0
            break
        total=0
        temp=[]
        while True:
            if len(STACK)==0:
                FLAG = 0
                break
            top=STACK.pop()
            # print(f"top: {top}")
            if top=="[":
                if len(temp)==0:
                    total=3
                else:
                    for num in temp:
                        total+=num
                    total = total*3
                # print(f"total: {total}")
                STACK.append(total)
                # print(f"STACK: {STACK}")
                break
            elif top=="(" or top==")" or top=="]":
                FLAG = 0
                break
            else:
                temp.append(top)
# print(f"FLAG: {FLAG}, STACK: {STACK}")
for letter in STACK:
    if letter == "(":
        FLAG = 0
    elif letter =="[":
        FLAG = 0
if FLAG ==0:
    print(0)
else:
    # print(STACK)
    # print(f"sum: {sum(STACK)}")
    print(sum(STACK))
N = int(input())
switch = list(map(int, input().split()))
num_student = int(input())

def switch_action(index, lst) -> list:
    if lst[index]==0:
        lst[index]=1
    else:
        lst[index]=0
    # print(f"switching index: {index}, lst: {lst}")
    return lst

def switch_man(start, lst) -> list:
    for i in range(len(lst)):
        if (i+1)%start==0:
            switch_action(i, lst)
    return lst

def switch_woman(start, lst) -> list:
    start = start-1
    switch_action(start, lst)
    # print(f"lst: {lst}")
    count = 0
    while True:
        if count==0: left, right = start - 1, start + 1
        else: left, right = left - 1, right + 1
        # print(f"left: {left}, right: {right}")
        if left<0 or right>len(lst)-1:
            break
        elif lst[left]==lst[right]:
            switch_action(left, lst)
            switch_action(right, lst)
            count+=1
        else:
            break
    return lst

for i in range(num_student):
    sex, start = map(int, input().split())
    # print(f"sex: {sex}, start: {start}")
    if sex==1:
        switch_man(start, switch)
    elif sex==2:
        switch_woman(start, switch)

for i in range(len(switch)):
    if len(switch)<=20:
        if i==len(switch)-1:
            print(switch[i])
        else:
            print(switch[i], end=' ')
    else:
        if (i+1)%20==0:
            print(switch[i])
        elif i==len(switch)-1:
            print(switch[i])
        else:
            print(switch[i], end=' ')
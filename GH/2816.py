def move_down():
    global cursor
    if cursor < N-1:
        # print(f"cursor moving down: {cursor} to {cursor+1}")
        cursor += 1
        # print(f"cursor: {cursor}")
        res.append(1)
    # else: print("out of range")

def move_up():
    global cursor
    if cursor > 0:
        # print(f"cursor moving up: {cursor} to {cursor-1}")
        cursor -= 1
        res.append(2)
        # print(f"cursor: {cursor}")
    # else: print("out of range")

def swap_down():
    global cursor
    if cursor < N-1:
        # print(f"swapping {channels[cursor]} & {channels[cursor+1]}")
        channels[cursor], channels[cursor+1] = channels[cursor+1], channels[cursor]
        cursor += 1
        res.append(3)
        # print(f"cursor: {cursor}")
    # else: print("out of range")

def swap_up():
    global cursor
    if cursor > 0:
        # print(f"swapping {channels[cursor]} & {channels[cursor-1]}")
        channels[cursor], channels[cursor-1] = channels[cursor-1], channels[cursor]
        cursor -= 1
        res.append(4)
        # print(f"cursor: {cursor}")
    # else: print("out of range")

def switch(target, pos):
    global cursor
    # if cursor < target and target > pos: swap_down()
    # elif cursor > target and target < pos: swap_up()
    if cursor < target: move_down()
    elif cursor > target: move_up()
    else:
        while cursor < pos: swap_down()
        while cursor > pos: swap_up()
    # print(f"channels: {channels}")

N = int(input())
channels = [input() for _ in range(N)]
res = []
cursor = 0

for i in range(2):
    if i==0:
        # print(f"======= KBS1 =======")
        # cursor = 0
        target_index = channels.index("KBS1")
        target_pos = 0
        while True:
            target_index = channels.index("KBS1")
            # print(f"target_index: {target_index}, target_pos: {target_pos}")
            if target_index == target_pos: break
            switch(target_index, target_pos)
    else:
        # print(f"======= KBS2 =======")
        # cursor = 1
        target_index = channels.index("KBS2")
        target_pos = 1
        while True:
            # print(f"target_index: {target_index}, target_pos: {target_pos}")
            target_index = channels.index("KBS2")
            if target_index == target_pos: break
            switch(target_index, target_pos)

for i in range(len(res)):
    if i == len(res)-1: print(res[i])
    else: print(res[i], end='')
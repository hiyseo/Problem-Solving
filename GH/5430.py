from collections import deque

N = int(input())
for _ in range(N):
    function = list(map(str, input()))
    n = int(input())
    
    if n != 0:
        lst = input().strip("[]").split(",")
        lst = deque(int(x) for x in lst)
    else:
        lst = input().strip("[]")
        lst = deque(lst)

    reverse_flag = False
    error_flag = False

    def AC(lst, action, reverse_flag, error_flag):
        if action == "R":
            reverse_flag = not reverse_flag
        elif action == "D":
            if len(lst) == 0:
                print("error")
                error_flag = True
                return lst, reverse_flag, error_flag
            else:
                if reverse_flag:
                    lst.pop()
                else:
                    lst.popleft()
        return lst, reverse_flag, error_flag

    for char in function:
        lst, reverse_flag, error_flag = AC(lst, char, reverse_flag, error_flag)
        if error_flag:
            break

    if not error_flag:
        if reverse_flag:
            lst.reverse()
        print("[" + ",".join(map(str, lst)) + "]")

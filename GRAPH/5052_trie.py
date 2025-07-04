# 노드 연습
# 각 노드는
# 1. children이 있고 children은 딕셔너리
#   예를 들어 91, 92가 있다면
#   9: 1(노드), 2(노드)
# 2. 마지막인지 나타내는 is_end

class Trie_node():
    def __init__(self):
        self.children = dict()
        self.is_end = False
    
    def insert(self, number):
        node = self
        for digit in number:
            if node.is_end: # 다른 누군가의 마지막인 경우
                return False
            if digit not in node.children:
                node.children[digit] = Trie_node()
            node = node.children[digit]
        if node.children: # 끝났는데도 children이 있는 경우
            return False
        node.is_end = True
        return True

t = int(input())
for _ in range(t):
    n = int(input())
    numbers = [input().strip() for _ in range(n)]
    
    root = Trie_node()
    flag = 1 # 1: YES, 0: NO
    
    numbers.sort()
    for number in numbers:
        if not root.insert(number):
            flag = 0
            break
    
    print("YES" if flag else "NO")

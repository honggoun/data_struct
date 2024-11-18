import random

class TreeNode():
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

memory = []
rootbook = None
rootAuth
bookAry = [
    ["어린왕자", "생텍쥐베리"],
    ["이방인", "까뮈"],
    ["부활", "톨스토이"],
    ["신곡", "단테"],
    ["돈키호테", "세르반테스"],
    ["동물농장", "조지오웰"],
    ["데미안", "헤르만헤세"],
    ["파우스트", "괴테"],
    ["대지", "펄벅"]
]
random.shuffle(bookAry)  # shuffle without assignment

# 트리의 첫 번째 노드를 설정합니다
node = TreeNode()
node.data = bookAry[0][0]
rootbook = node
memory.append(node)

# 나머지 책들을 트리에 삽입합니다
for book in bookAry[1:]:
    name = book[0]
    node = TreeNode()
    node.data = name

    current = rootbook
    while True:
        if name < current.data:  # name이 작으면 왼쪽으로
            if current.left is None:
                current.left = node
                break
            current = current.left
        else:  # name이 크거나 같으면 오른쪽으로
            if current.right is None:
                current.right = node
                break
            current = current.right

    memory.append(node)
print("책 이름 트리 구성 완료")

ndoe = TreeNode()
node.data = bookAry[0][1]
rootAuth = node
memory.append(node)

for book in bookAry[1:]:
    name = book[1]
    node = TreeNode()
    node.data = name

      
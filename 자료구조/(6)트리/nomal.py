class Node():
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

memory = []
root = None
nameAry = ["블랙핑크","레드벨벳","마마무","에이핑크","걸스데이","트와이스"]

node = Node()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:]:
    node = Node()
    node.data = name
    current = root
    while True:
        if name < current.data:
            if node.left == None:
                node.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right
    memory.append(node)

print("이진 탐색트리 구성 완료")


findname = "마마무"

current = root
while True:
    if findname == current.data:
        print(findname)
        break
    if findname < current.data:
        if current.left == None:
            print(findname,"이 없음")
            break
        current = current.left
    else:
        if current.right == None:
            print(findname,"이 없음")
            break
        current = current.right

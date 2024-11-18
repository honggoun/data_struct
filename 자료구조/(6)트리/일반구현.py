class Treenode():
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

#데이터 생성 및 추가#
memory = []
root = None
nameAry = ["블랙핑크","레드벨벳","마마무","걸스데이","트와이스"]

node = Treenode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:]:
    node = Treenode()
    node.data = name
    current = root
    while True:
        if name<current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right
    memory.append(node)
print("이진트리 구현 완료")

#데이터 찾기#
findname = "마마무"

current = root
while True:
    if findname == current.data:
        print(findname,"를 찾음")
        break
    elif findname < current.data:
        if current.left == None:
            print(findname,"이 트리에 없음")
            break
        current = current.left
    else:
        if current.right == None:
            print(findname,"가 트리에 없음")
            break
        current = current.right

#데이터 삭제#
deletname = "마마무"

current = root
parent = None
while True:
    if deletname == current.data:
        if current.left == None and current.right == None:
            if parent.left == current:
                parent.left = None
            else:
                parent.right = None
            del(current)
        elif current.left != None and current.right == None:
            if parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left
            del(current)
        elif current.left == None and current.right != None:
            if parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right
            del(current)
        print(deletname,"이 삭제됨")
        break
    elif deletname < current.data:
        if current.left == None:
            print(deletname,"이 트리에 없음")
            break
        parent = current
        current = current.left
    else:
        if current.right == None:
            print(deletname,"이 트리에 없음")
            break
        parent = current
        current = current.right
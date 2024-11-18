#이진트리 생성#
# class TreeNode():
#     def __init__(self):
#         self.left=None
#         self.right=None
#         self.data=None

# node1 = TreeNode()
# node1.data="화사"

# node2 = TreeNode()
# node2.data = "솔라"
# node1.left = node2

# node3 = TreeNode()
# node3.data="문별"
# node1.right=node3

# node4=TreeNode()
# node4.data="휘인"
# node2.left = node4

# node5=TreeNode()
# node5.data="쯔위"
# node2.right=node5

# node6=TreeNode()
# node6.data="선미"
# node3.left=node6

# print(node1.data,end=' ')
# print()
# print(node1.left.data,node1.right.data,end=' ')
# print()
# print(node2.left.data,node2.right.data,node3.left.data,end=' ')
# print()

#이진탐색트리의 일반 구현##

class TreeNode():
    def __init__(self):
        self.left=None
        self.right=None
        self.data=None

##전역변수 선언##
memory=[]
root=None
nameAty=['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스']

##메인함수##
node=TreeNode()
node.data=nameAty[0]
root=node
memory.append(node)

for name in nameAty[1:]:
    node = TreeNode()
    node.data=name
    current=root
    while True:
        if name<current.data:
            if current.left == None:
                current.left = node
                break
            current=current.left
        else:
            if current.right==None:
                current.right=node
                break
            current=current.right
        memory.append(node)

print('이진 탐색 트리 구성 완료!')

findName=input("탐색 할 데이터를 입력하시오->")

current=root
while True:
    if findName == current.data:
        print(findName,"을 찾음")
        break
    elif findName < current.data:
        if current.left==None:
            print(findName,"이 트리에 없음")
            break
        current=current.left
    else:
        if current.right==None:
            print(findName,"이 트리에 없음")
            break
        current=current.right

#이진트리 순회 구현#
# def preorder(node):
#     if node==None:
#         return
#     print(node.data,end='->')
#     preorder(node.left)
#     preorder(node.right)

# def inorder(node):
#     if node==None:
#         return
#     inorder(node.left)
#     print(node.data,end='->')
#     inorder(node.right)

# def postorder(node):
#     if node==None:
#         return
#     postorder(node.left)
#     postorder(node.right)
#     print(node.data,end='->')

# print("전위순회:",end=' ')
# preorder(node1)
# print("끝")

# print("중위순회:",end=' ')
# inorder(node1)
# print("끝")

# print("후위순회:",end=' ')
# postorder(node1)
# print("끝")

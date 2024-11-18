class Node():
    def __init__(self):
        self.data = None
        self.link = None

node1 = Node()
node1.data = "다현"
node1.link = node1

#노드 연결

node2 = Node()
node2.data = "정연"
node1.link = node2
node2.link = node1

node3 = Node()
node3.data = "쯔위"
node2.link = node3
node3.link = node1  

node4 = Node()
node4.data = "사나"
node3.link = node4
node4.link = node1

node5 = Node()
node5.data = "지효"
node4.link = node5
node5.link = node1

#노드 삽입(쯔위,사나 사이에 홍권)
newnode = Node()
newnode.data = "홍권"
node3.link = newnode
newnode.link = node4

#중간 데이터 삭제(사나 삭제)
newnode.link = node5
del(node4)


#노드 출력
current = node1
head = current
print(current.data,end=' ')
while current.link != head:
    current = current.link
    print(current.data,end=' ')